# https://stackoverflow.com/a/43905715
# Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://github.dev/mon-jai/network-programming/blob/main/setup.ps1'))

# https://stackoverflow.com/a/73534796
if (
  (Invoke-RestMethod 'https://www.python.org/downloads/') -notmatch 
  '\bhref="(?<url>.+?\.exe)"\s*>\s*Download Python (?<version>\d+\.\d+\.\d+)'
) { throw "Could not determine latest Python version and download URL" }

# https://stackoverflow.com/a/43477248
$ProgressPreference = 'SilentlyContinue'

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest -Uri $Matches.url -OutFile "$env:USERPROFILE/python.exe"
& "$env:USERPROFILE/python.exe" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0

Invoke-WebRequest -Uri "https://github.dev/mon-jai/network-programming/blob/main/settings.json" -OutFile "C:\Users\LAB1223\AppData\Roaming\Code\User\settings.json"
code --install-extension ms-python.python
code --install-extension formulahendry.code-runner