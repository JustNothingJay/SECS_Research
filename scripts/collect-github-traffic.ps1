# GitHub Traffic Data Collector for SECS_Research
# Polls the GitHub API daily and appends clone/view data to a local JSON log.
# Data persists beyond GitHub's 14-day rolling window.
#
# Usage:
#   .\collect-github-traffic.ps1
#
# Requires: GITHUB_TOKEN environment variable set with a personal access token
#   Token needs: repo scope (or just public_repo for public repos)
#   Create one at: https://github.com/settings/tokens
#
# Set it once:
#   [System.Environment]::SetEnvironmentVariable("GITHUB_TOKEN", "ghp_your_token_here", "User")
#   Then restart your terminal.

$ErrorActionPreference = "Stop"

# --- Configuration ---
$Owner = "JustNothingJay"
$Repo  = "SECS_Research"
$LogDir = Join-Path (Join-Path $PSScriptRoot "..") "traffic-logs"
$CloneLog = Join-Path $LogDir "clones.json"
$ViewLog  = Join-Path $LogDir "views.json"
$SummaryLog = Join-Path $LogDir "daily-summary.csv"

# --- Token ---
$Token = $env:GITHUB_TOKEN
if (-not $Token) {
    Write-Error @"
GITHUB_TOKEN environment variable not set.

Create a personal access token at: https://github.com/settings/tokens
  - Select 'public_repo' scope (that's all you need)
  - Copy the token

Then run:
  [System.Environment]::SetEnvironmentVariable("GITHUB_TOKEN", "ghp_your_token_here", "User")

Restart your terminal and try again.
"@
    exit 1
}

$Headers = @{
    "Authorization" = "Bearer $Token"
    "Accept"        = "application/vnd.github.v3+json"
    "User-Agent"    = "SECS-Traffic-Collector"
}

# --- Ensure log directory exists ---
if (-not (Test-Path $LogDir)) {
    New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
    Write-Host "Created log directory: $LogDir"
}

# --- Helper: Load existing log or create empty array ---
function Get-ExistingLog {
    param([string]$Path)
    if (Test-Path $Path) {
        $content = Get-Content $Path -Raw
        if ($content -and $content.Trim().Length -gt 0) {
            return $content | ConvertFrom-Json
        }
    }
    return @()
}

# --- Helper: Merge new data with existing (deduplicate by timestamp) ---
function Merge-TrafficData {
    param(
        [array]$Existing,
        [array]$New
    )
    $existingTimestamps = @{}
    foreach ($entry in $Existing) {
        $existingTimestamps[$entry.timestamp] = $true
    }
    $merged = [System.Collections.ArrayList]@($Existing)
    $newCount = 0
    foreach ($entry in $New) {
        if (-not $existingTimestamps.ContainsKey($entry.timestamp)) {
            $merged.Add($entry) | Out-Null
            $newCount++
        }
    }
    Write-Host "  $newCount new data points added ($($merged.Count) total)"
    return $merged | Sort-Object { $_.timestamp }
}

# --- Fetch Clones ---
Write-Host "`n=== SECS_Research Traffic Collector ==="
Write-Host "Timestamp: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Write-Host ""

Write-Host "Fetching clone data..."
try {
    $cloneResponse = Invoke-RestMethod `
        -Uri "https://api.github.com/repos/$Owner/$Repo/traffic/clones" `
        -Headers $Headers `
        -Method Get

    Write-Host "  Total clones (14-day): $($cloneResponse.count)"
    Write-Host "  Unique cloners (14-day): $($cloneResponse.uniques)"

    $existingClones = Get-ExistingLog -Path $CloneLog
    $mergedClones = Merge-TrafficData -Existing $existingClones -New $cloneResponse.clones
    $mergedClones | ConvertTo-Json -Depth 10 | Set-Content $CloneLog -Encoding UTF8
} catch {
    Write-Warning "Failed to fetch clone data: $_"
    $cloneResponse = $null
}

# --- Fetch Views ---
Write-Host "Fetching view data..."
try {
    $viewResponse = Invoke-RestMethod `
        -Uri "https://api.github.com/repos/$Owner/$Repo/traffic/views" `
        -Headers $Headers `
        -Method Get

    Write-Host "  Total views (14-day): $($viewResponse.count)"
    Write-Host "  Unique viewers (14-day): $($viewResponse.uniques)"

    $existingViews = Get-ExistingLog -Path $ViewLog
    $mergedViews = Merge-TrafficData -Existing $existingViews -New $viewResponse.views
    $mergedViews | ConvertTo-Json -Depth 10 | Set-Content $ViewLog -Encoding UTF8
} catch {
    Write-Warning "Failed to fetch view data: $_"
    $viewResponse = $null
}

# --- Fetch Referrers ---
Write-Host "Fetching referrer data..."
try {
    $referrers = Invoke-RestMethod `
        -Uri "https://api.github.com/repos/$Owner/$Repo/traffic/popular/referrers" `
        -Headers $Headers `
        -Method Get

    $referrerLog = Join-Path $LogDir "referrers-$(Get-Date -Format 'yyyy-MM-dd').json"
    $referrers | ConvertTo-Json -Depth 10 | Set-Content $referrerLog -Encoding UTF8
    Write-Host "  Referrers saved to: $referrerLog"
} catch {
    Write-Warning "Failed to fetch referrer data: $_"
}

# --- Fetch Popular Paths ---
Write-Host "Fetching popular paths..."
try {
    $paths = Invoke-RestMethod `
        -Uri "https://api.github.com/repos/$Owner/$Repo/traffic/popular/paths" `
        -Headers $Headers `
        -Method Get

    $pathsLog = Join-Path $LogDir "popular-paths-$(Get-Date -Format 'yyyy-MM-dd').json"
    $paths | ConvertTo-Json -Depth 10 | Set-Content $pathsLog -Encoding UTF8
    Write-Host "  Popular paths saved to: $pathsLog"
} catch {
    Write-Warning "Failed to fetch popular paths: $_"
}

# --- Append daily summary to CSV ---
$summaryEntry = [PSCustomObject]@{
    CollectedAt    = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    ClonesTotal14d = if ($cloneResponse) { $cloneResponse.count } else { "ERROR" }
    ClonesUnique14d = if ($cloneResponse) { $cloneResponse.uniques } else { "ERROR" }
    ViewsTotal14d  = if ($viewResponse) { $viewResponse.count } else { "ERROR" }
    ViewsUnique14d = if ($viewResponse) { $viewResponse.uniques } else { "ERROR" }
}

$csvExists = Test-Path $SummaryLog
$summaryEntry | Export-Csv -Path $SummaryLog -Append -NoTypeInformation -Encoding UTF8
if (-not $csvExists) {
    Write-Host "`nCreated summary log: $SummaryLog"
} else {
    Write-Host "`nAppended to summary log: $SummaryLog"
}

# --- Print summary ---
Write-Host "`n--- Summary ---"
Write-Host "Clone log: $CloneLog"
Write-Host "View log:  $ViewLog"
Write-Host "Summary:   $SummaryLog"
Write-Host "===============`n"
