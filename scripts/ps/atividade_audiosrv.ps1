#Armazena o serviço em uma variável
$servico = Get-Service AudioSRV

#Para o serviço
$servico.stop()

#Inicia o serviço
$servico.start()