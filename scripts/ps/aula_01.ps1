Get-Service -Name "Bytebank Interface Service" -ComputerName "SRV01"

#------------#

#Armazenando em uma variável
$servico = Get-Service -Name "Bytebank Interface Service" -ComputerName "SRV01"
$servico.Status

#------------#

#Para o serviço e reinicia
if ($servico.Status -eq "Running") {
    $servico.Stop()
    $servico.Start()
} else {
    echo "Serviço não estava executando!"
}
