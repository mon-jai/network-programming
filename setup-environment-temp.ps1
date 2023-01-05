Param([switch]$InstallPython)

# Copyright 2022 Loh Ka Hong | Licensed under MIT

# Throw an statement-terminating error when "the setting is overridden by a policy defined at a more specific scope", https://stackoverflow.com/a/60549569
# Redirect all streams to $null, https://stackoverflow.com/a/6461021
# https://stackoverflow.com/a/68777742
# . { Set-ExecutionPolicy Bypass -Scope Process -Force } *> $null; & ([scriptblock]::Create((irm 'https://raw.githubusercontent.com/mon-jai/network-programming/main/setup-environment.ps1'))) -InstallPython

echo $InstallPython
