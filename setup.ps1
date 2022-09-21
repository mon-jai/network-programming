// https://stackoverflow.com/a/73534796
if (
  (Invoke-RestMethod 'https://www.python.org/downloads/') -notmatch 
  '\bhref="(?<url>.+?\.exe)"\s*>\s*Download Python (?<version>\d+\.\d+\.\d+)'
) { throw "Could not determine latest Python version and download URL" }

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;
Invoke-WebRequest -Uri $Matches.url -OutFile "$($env:USERPROFILE)/python.exe";
& "$($env:USERPROFILE)/python.exe" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
