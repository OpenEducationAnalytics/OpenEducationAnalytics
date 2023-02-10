

$cmdName="poetry"
Get-Command $cmdName
if (-Not (Get-Command $cmdName -errorAction SilentlyContinue))
{
    "installing $cmdName"
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    [Environment]::SetEnvironmentVariable("Path", $env:Path + ";%APPDATA%\Python\Scripts", "User")
}
else{
    poetry self update
}
