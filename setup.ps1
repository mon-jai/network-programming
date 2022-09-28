# https://stackoverflow.com/a/43905715
# Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/mon-jai/network-programming/main/setup.ps1'))


Write-Output "Setting language...";

# https://stackoverflow.com/a/51374938
Set-Culture en-US
Set-WinSystemLocale -SystemLocale en-US
Set-WinUILanguageOverride -Language en-US

$languageList = New-WinUserLanguageList en-US
$languageList.Add('zh-Hant-TW')
$languageList[1].InputMethodTips.Clear()
$languageList[1].InputMethodTips.Add('0404:{531FDEBF-9B4C-4A43-A2AA-960E8FCDC732}{4BDF9F03-C7D3-11D4-B2AB-0080C882687E}')
Set-WinUserLanguageList $languageList -Force

Start-Job {
$pythonDownloadPath = "$env:USERPROFILE/python.exe"

Write-Output "Installing Python..."

# https://stackoverflow.com/a/73534796
if (
  ((New-Object System.Net.WebClient).DownloadString('https://www.python.org/downloads/')) -notmatch
  '\bhref="(?<url>.+?\.exe)"\s*>\s*Download Python (?<version>\d+\.\d+\.\d+)'
) { throw "Could not determine latest Python version and download URL" }
(New-Object System.Net.WebClient).DownloadFile($Matches.url, $pythonDownloadPath)

# https://stackoverflow.com/a/1742758
Start-Process "$pythonDownloadPath" -ArgumentList "/quiet", "InstallAllUsers=0", "PrependPath=1", "Include_test=0" -NoNewWindow -Wait
Remove-Item $pythonDownloadPath

Write-Output "Installing Python... Done"
}

Start-Job {
Write-Output "Setting up VSCode..."

(New-Object System.Net.WebClient).DownloadFile("https://raw.githubusercontent.com/mon-jai/network-programming/main/settings.json", "$env:AppData\Code\User\settings.json")
code --install-extension ms-python.python --force
code --install-extension formulahendry.code-runner --force
code --install-extension github.github-vscode-theme --force

Write-Output "Setting up VSCode... Done"
}

Get-Job | Receive-Job

Write-Output "Done!"
