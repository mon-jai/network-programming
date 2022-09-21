// https://stackoverflow.com/a/43905715
// Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://gist.githubusercontent.com/mon-jai/f3a21942f2e2334ec12faefc5851c1f3/raw/a9b67d8d95db9906183cecadacd11ccb0f068a2f/setup.ps1'))

// https://stackoverflow.com/a/73534796
if (
  (Invoke-RestMethod 'https://www.python.org/downloads/') -notmatch 
  '\bhref="(?<url>.+?\.exe)"\s*>\s*Download Python (?<version>\d+\.\d+\.\d+)'
) { throw "Could not determine latest Python version and download URL" }

# https://stackoverflow.com/a/43477248
$ProgressPreference = 'SilentlyContinue'

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;
Invoke-WebRequest -Uri $Matches.url -OutFile "$($env:USERPROFILE)/python.exe";
& "$($env:USERPROFILE)/python.exe" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
