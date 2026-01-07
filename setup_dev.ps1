# UET Research Development Setup
# ================================
# This script sets up the development environment with centralized cache
#
# Usage: . .\setup_dev.ps1  (dot-source to keep env vars)

Write-Host "🔧 Setting up UET development environment..." -ForegroundColor Cyan

# Get project root
$ProjectRoot = Split-Path -Parent $PSScriptRoot
if (-not $ProjectRoot) {
    $ProjectRoot = Get-Location
}

# Create centralized cache directory
$CacheDir = Join-Path $ProjectRoot ".cache\pycache"
if (-not (Test-Path $CacheDir)) {
    New-Item -ItemType Directory -Path $CacheDir -Force | Out-Null
    Write-Host "✅ Created cache directory: $CacheDir" -ForegroundColor Green
}

# Set PYTHONPYCACHEPREFIX - all __pycache__ goes here
$env:PYTHONPYCACHEPREFIX = $CacheDir
Write-Host "✅ PYTHONPYCACHEPREFIX set to: $CacheDir" -ForegroundColor Green

# Set PYTHONDONTWRITEBYTECODE to 0 (we DO want bytecode, just centralized)
$env:PYTHONDONTWRITEBYTECODE = ""

# Optionally set up pytest cache too
$PytestCacheDir = Join-Path $ProjectRoot ".cache\pytest"
if (-not (Test-Path $PytestCacheDir)) {
    New-Item -ItemType Directory -Path $PytestCacheDir -Force | Out-Null
}
$env:PYTEST_CACHE_DIR = $PytestCacheDir

Write-Host ""
Write-Host "📁 Cache locations:" -ForegroundColor Yellow
Write-Host "   Python: $env:PYTHONPYCACHEPREFIX"
Write-Host "   Pytest: $env:PYTEST_CACHE_DIR"
Write-Host ""
Write-Host "✅ Development environment ready!" -ForegroundColor Green
Write-Host "   Run Python scripts normally - cache will go to .cache/" -ForegroundColor Cyan
