copier -f -r 0e0e368
Remove-Item .venv -Recurse -ErrorAction SilentlyContinue
py -3.10 -m venv .venv --upgrade-deps
. .tools/setup/update.ps1
