# collect-all-traffic.ps1
# Runs both GitHub and Zenodo traffic collectors in sequence.
#
# Usage:
#   .\collect-all-traffic.ps1

$ErrorActionPreference = "Stop"
$ScriptDir = $PSScriptRoot

Write-Host "=== Collecting all SECS_Research traffic data ===" -ForegroundColor Cyan
Write-Host ""

# --- GitHub ---
Write-Host "--- GitHub Traffic ---" -ForegroundColor Yellow
& "$ScriptDir\collect-github-traffic.ps1"

# --- Zenodo ---
Write-Host "--- Zenodo Traffic ---" -ForegroundColor Yellow
& "$ScriptDir\collect-zenodo-traffic.ps1"

Write-Host "=== All traffic data collected ===" -ForegroundColor Green
