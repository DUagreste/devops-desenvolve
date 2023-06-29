.\reiniciaServicoSrv01.bat

echo $env:path

$env:path

$env:path.GetType()

$env:path.Split(';')

$env:path | Get-Member

Get-Alias

Get-Command

Get-Command -Name *rename*

Get-Help Name rename-item

Rename-Item C:\Scripts\script.bat C:\Scripts\script_migrando.bat -WhatIf

Rename-Item C:\Scripts\script.bat C:\Scripts\script_migrando.bat 

Update-Help

Get-Command -noun alias

Get-Help new-alias

new-alias -Name="rename" rename-item

get-alias rename

rename C:\Scripts\script.bat C:\Scripts\script_migrando.bat 