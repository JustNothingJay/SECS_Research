# Zenodo Traffic Data Collector for SECS_Research
# Polls the Zenodo Statistics API and appends view/download data to a local JSON log.
# Zenodo provides all-time stats (not rolling), so we snapshot daily for trend tracking.
#
# Usage:
#   .\collect-zenodo-traffic.ps1
#
# No authentication required -- Zenodo stats are public.
# Concept Record ID: 18896027 (resolves to latest version)
# Concept DOI: 10.5281/zenodo.18896027

$ErrorActionPreference = "Stop"

# --- Configuration ---
$ConceptRecId = "18896027"
$LogDir = Join-Path (Join-Path $PSScriptRoot "..") "traffic-logs"
$StatsLog = Join-Path $LogDir "zenodo-stats.json"
$SummaryLog = Join-Path $LogDir "zenodo-daily-summary.csv"

$Headers = @{
    "Accept"     = "application/json"
    "User-Agent" = "SECS-Zenodo-Collector"
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

# --- Resolve latest version from concept record ---
Write-Host "`n=== SECS_Research Zenodo Traffic Collector ==="
Write-Host "Concept: $ConceptRecId (DOI: 10.5281/zenodo.$ConceptRecId)"
Write-Host "Timestamp: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Write-Host ""

Write-Host "Resolving latest version..."
try {
    $versions = Invoke-RestMethod `
        -Uri "https://zenodo.org/api/records/?q=conceptrecid:$ConceptRecId&all_versions=true&sort=mostrecent&size=1" `
        -Headers $Headers `
        -Method Get
    $latestId = $versions.hits.hits[0].id
    Write-Host "  Latest record: $latestId"
} catch {
    Write-Error "Failed to resolve latest version: $_"
    exit 1
}

Write-Host "Fetching Zenodo statistics..."
try {
    $statsResponse = Invoke-RestMethod `
        -Uri "https://zenodo.org/api/records/$latestId" `
        -Headers $Headers `
        -Method Get

    $views = $statsResponse.stats.views
    $downloads = $statsResponse.stats.downloads
    $uniqueViews = $statsResponse.stats.unique_views
    $uniqueDownloads = $statsResponse.stats.unique_downloads
    $version = $statsResponse.metadata.version
    $fileCount = ($statsResponse.files | Measure-Object).Count

    Write-Host "  Version: $version"
    Write-Host "  Views (all-time): $views"
    Write-Host "  Unique views: $uniqueViews"
    Write-Host "  Downloads (all-time): $downloads"
    Write-Host "  Unique downloads: $uniqueDownloads"
    Write-Host "  Files: $fileCount"
} catch {
    Write-Error "Failed to fetch Zenodo stats: $_"
    exit 1
}

# --- Fetch per-file download info ---
Write-Host "Fetching per-file details..."
$fileNames = @()
foreach ($file in $statsResponse.files) {
    $fileNames += $file.key
    $sizeMB = [math]::Round($file.size / 1MB, 2)
    Write-Host "  $($file.key) -- $sizeMB MB"
}

# --- Snapshot entry ---
$snapshot = [PSCustomObject]@{
    collected_at     = Get-Date -Format 'yyyy-MM-ddTHH:mm:ssZ'
    record_id        = $latestId
    version          = $version
    views            = $views
    unique_views     = $uniqueViews
    downloads        = $downloads
    unique_downloads = $uniqueDownloads
    file_count       = $fileCount
    files            = ($fileNames -join "; ")
}

# --- Append to stats log (deduplicate by date) ---
$existingStats = Get-ExistingLog -Path $StatsLog
$today = Get-Date -Format 'yyyy-MM-dd'
$alreadyCollected = $false
foreach ($entry in $existingStats) {
    if ($entry.collected_at -and $entry.collected_at.StartsWith($today)) {
        $alreadyCollected = $true
        break
    }
}

if ($alreadyCollected) {
    Write-Host "`nAlready collected today -- updating entry"
    $updatedStats = @()
    foreach ($entry in $existingStats) {
        if ($entry.collected_at -and $entry.collected_at.StartsWith($today)) {
            $updatedStats += $snapshot
        } else {
            $updatedStats += $entry
        }
    }
    $updatedStats | ConvertTo-Json -Depth 10 | Set-Content $StatsLog -Encoding UTF8
} else {
    $allStats = [System.Collections.ArrayList]@($existingStats)
    $allStats.Add($snapshot) | Out-Null
    $allStats | ConvertTo-Json -Depth 10 | Set-Content $StatsLog -Encoding UTF8
    Write-Host "`nNew snapshot added ($($allStats.Count) total entries)"
}

# --- Append daily summary to CSV ---
$summaryEntry = [PSCustomObject]@{
    CollectedAt      = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    Version          = $version
    ViewsAllTime     = $views
    UniqueViews      = $uniqueViews
    DownloadsAllTime = $downloads
    UniqueDownloads  = $uniqueDownloads
    FileCount        = $fileCount
}

$csvExists = Test-Path $SummaryLog
$summaryEntry | Export-Csv -Path $SummaryLog -Append -NoTypeInformation -Encoding UTF8
if (-not $csvExists) {
    Write-Host "Created summary log: $SummaryLog"
} else {
    Write-Host "Appended to summary log: $SummaryLog"
}

# --- Print summary ---
Write-Host "`n--- Summary ---"
Write-Host "Stats log: $StatsLog"
Write-Host "Summary:   $SummaryLog"
Write-Host "===============`n"
