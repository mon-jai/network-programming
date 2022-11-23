# https://stackoverflow.com/a/43905715
# Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/mon-jai/network-programming/main/setup-environment.ps1'))

Start-Job -Name 'Setup language' -ErrorAction Stop -ScriptBlock {
  # https://stackoverflow.com/a/51374938
  Set-Culture en-US
  Set-WinSystemLocale -SystemLocale en-US
  Set-WinUILanguageOverride -Language en-US

  $languageList = New-WinUserLanguageList en-US
  $languageList.Add('zh-Hant-TW')
  $languageList[1].InputMethodTips.Clear()
  $languageList[1].InputMethodTips.Add('0404:{531FDEBF-9B4C-4A43-A2AA-960E8FCDC732}{4BDF9F03-C7D3-11D4-B2AB-0080C882687E}')
  Set-WinUserLanguageList $languageList -Force

  Write-Host "Setup language completed"
}

Start-Job -Name 'Install and setup Python' -ErrorAction Stop -ScriptBlock {
  $pythonDownloadPath = "$Env:TEMP/python.exe"

  # https://stackoverflow.com/a/73534796
  if (
    (Invoke-RestMethod 'https://www.python.org/downloads/') -notmatch
    '\bhref="(?<url>.+?\.exe)"\s*>\s*Download Python (?<version>\d+\.\d+\.\d+)'
  ) { throw "Could not determine latest Python version and download URL" }

  # https://stackoverflow.com/a/21423159
  Import-Module BitsTransfer
  Start-BitsTransfer $Matches.url $pythonDownloadPath

  Start-Process "$pythonDownloadPath" -ArgumentList "/quiet", "PrependPath=1" -NoNewWindow -Wait
  Remove-Item $pythonDownloadPath

  # https://stackoverflow.com/a/67796873
  & { pip config set global.trusted-host "pypi.org files.pythonhosted.org pypi.python.org" } > $null
  & { python -m pip install --upgrade pip } > $null
  & { pip install -U autopep8 } > $null

  Write-Host "Install and setup Python completed"
}

Start-Job -Name 'Setup VSCode' -ErrorAction Stop -ScriptBlock {
  # https://stackoverflow.com/a/36705460
  # https://stackoverflow.com/a/36751445
  Remove-Item "$Env:USERPROFILE/.vscode/extensions" -Force -Recurse -ErrorAction SilentlyContinue

  $vscode_settings = [pscustomobject]@{
    "[python]"                         = [pscustomobject]@{
      "editor.tabSize" = 4
    }
    "code-runner.clearPreviousOutput"  = true
    "code-runner.executorMap"          = [pscustomobject]@{
      # https://stackoverflow.com/a/53961913
      "python" = "clear; & `"`$env:LocalAppData\Programs\Python\Python311\python`" -u"
    }
    "code-runner.ignoreSelection"      = true
    "code-runner.runInTerminal"        = true
    "code-runner.saveFileBeforeRun"    = true
    "editor.tabSize"                   = 2
    "explorer.confirmDelete"           = false
    "files.associations"               = [pscustomobject]@{
      "*.xml" = "html"
    }
    "http.proxyStrictSSL"              = false
    "python.analysis.typeCheckingMode" = "strict"
    "workbench.colorTheme"             = "GitHub Light Default"
    "workbench.startupEditor"          = "none"
  }

  ConvertTo-Json -InputObject $vscode_settings -OutFile "$Env:APPDATA\Code\User\settings.json"

  & { code --install-extension ms-python.python --force } *> $null
  & { code --install-extension formulahendry.code-runner --force } *> $null
  & { code --install-extension github.github-vscode-theme --force } *> $null

  Write-Host "Setup VSCode completed"
}

Get-Job | Receive-Job -Wait -ErrorAction Stop
Write-Host "Done!"
