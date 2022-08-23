# $env:path should contain a path to editbin.exe

$ErrorActionPreference = "Stop"

mkdir build_scripts\win_build

git status

if (-not (Test-Path env:LOTUS_VERSION)) {
  $env:LOTUS_VERSION = '0.0.0'
  Write-Output "WARNING: No environment variable LOTUS_VERSION set. Using 0.0.0"
}
Write-Output "Lotus Version is: $env:LOTUS_VERSION"
Write-Output "   ---"

Write-Output "   ---"
Write-Output "Use pyinstaller to create lotus .exe's"
Write-Output "   ---"
$SPEC_FILE = (python -c 'import lotus; print(lotus.PYINSTALLER_SPEC_PATH)') -join "`n"
pyinstaller --log-level INFO $SPEC_FILE

git status

# Change to the CLI directory
Set-Location -Path "dist\daemon" -PassThru

Write-Output "   ---"
Write-Output "Increase the stack for lotus command for (lotus plots create) chiapos limitations"
# editbin.exe needs to be in the path
editbin.exe /STACK:8000000 lotus.exe
Write-Output "   ---"

git status

Write-Output "   ---"
Write-Output "Moving final binaries to expected location"
Write-Output "   ---"
Copy-Item "." -Destination "$env:GITHUB_WORKSPACE\Lotus-win32-x64" -Recurse

Write-Output "   ---"
Write-Output "Windows CLI Binaries complete"
Write-Output "   ---"
