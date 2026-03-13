# Zenodo Traffic Data Collector for SECS_Research
# Polls the Zenodo API and appends view/download data to a local JSON + CSV log.
# No auth required — Zenodo stats API is public.
#
# Usage:
#   .\collect-zenodo-traffic.ps1

$ErrorActionPreference = "Stop"

# --- Configuration ---
$Records = @(
    @{ Name = "Biology corpus";          Id = 18896757 },
    @{ Name = "Death + Grothendieck";    Id = 18905785 },
    @{ Name = "Algebra";                 Id = 18906064 },
    @{ Name = "Meta-theory";             Id = 18932890 },
    @{ Name = "Constitutional Constant"; Id = 18995286 },
    @{ Name = "Fine Structure Constant"; Id = 18994393 },
    @{ Name = "Osmotic Derivation";      Id = 19000474 }
)

$LogDir     = Join-Path (Join-Path $PSScriptRoot "..") "traffic-logs"
$StatsLog   = Join-Path $LogDir "zenodo-stats.json"
$SummaryLog = Join-Path $LogDir "zenodo-daily-summary.csv"

# --- Ensure log directory exists ---
if (-not (Test-Path $LogDir)) {
    New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
}

Write-Host "`n=== Zenodo Traffic Collector ==="
Write-Host "Timestamp: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Write-Host ""

$collectedAt = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$allStats = @()

foreach ($rec in $Records) {
    $url = "https://zenodo.org/api/records/$($rec.Id)"
    Write-Host "Fetching $($rec.Name) (record $($rec.Id))..."
    try {
        $response = Invoke-RestMethod -Uri $url -Method Get -Headers @{ "Accept" = "application/json" }

        $views           = $response.stats.views
        $uniqueViews     = $response.stats.unique_views
        $downloads       = $response.stats.downloads
        $uniqueDownloads = $response.stats.unique_downloads

        Write-Host "  Views: $views (unique: $uniqueViews)  Downloads: $downloads (unique: $uniqueDownloads)"

        $entry = [PSCustomObject]@{
            collected_at     = $collectedAt
            name             = $rec.Name
            record_id        = $rec.Id
            version          = $response.metadata.version
            views            = $views
            unique_views     = $uniqueViews
            downloads        = $downloads
            unique_downloads = $uniqueDownloads
        }
        $allStats += $entry

        # Append to CSV
        $csvExists = Test-Path $SummaryLog
        $entry | Export-Csv -Path $SummaryLog -Append -NoTypeInformation -Encoding UTF8 -Force

    } catch {
        Write-Warning "Failed to fetch $($rec.Name): $_"
    }
}

# Overwrite JSON with latest snapshot (full detail)
$allStats | ConvertTo-Json -Depth 10 | Set-Content $StatsLog -Encoding UTF8

Write-Host "`n--- Summary ---"
Write-Host "Stats JSON: $StatsLog"
Write-Host "CSV log:    $SummaryLog"
Write-Host "===============`n"
