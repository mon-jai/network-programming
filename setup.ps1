# https://stackoverflow.com/a/43905715
# Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/mon-jai/network-programming/main/setup.ps1'))

Write-Output "Downloading Python..."

# https://stackoverflow.com/a/73534796
if (
  (Invoke-RestMethod 'https://www.python.org/downloads/') -notmatch 
  '\bhref="(?<url>.+?\.exe)"\s*>\s*Download Python (?<version>\d+\.\d+\.\d+)'
) { throw "Could not determine latest Python version and download URL" }

# https://stackoverflow.com/a/43477248
$ProgressPreference = 'SilentlyContinue'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest -Uri $Matches.url -OutFile "$env:USERPROFILE/python.exe"

Write-Output "Installing Python..."

& "$env:USERPROFILE/python.exe" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0

Write-Output "Setting up VSCode..."

Invoke-WebRequest -Uri "https://raw.githubusercontent.com/mon-jai/network-programming/main/settings.json" -OutFile "C:\Users\LAB1223\AppData\Roaming\Code\User\settings.json"
code --install-extension ms-python.python
code --install-extension formulahendry.code-runner
code --install-extension github.github-vscode-theme

$LanguageList = Get-WinUserLanguageList
$LanguageList.Add("en-US")
Set-WinUserLanguageList $LanguageList -Force
