$nameExpr = @{
    Label = "Nome";
    Expression = { $_.Name }
}
$lengthExpr = @{
    Label = "Tamanho";
    Expression = { "{0:N2}KB" -f ($_.Length / 1KB) }
}
$params = $nameExpr, $lengthExpr

$resultado = 
    Get-ChildItem -Recurse -File |
    Where-Object Name -like "*.jpg" |
    Select-Object $params

if ( $ExportType -eq "html" ){
    $estilos = Get-Content C:\Users\vitor\Scripts\styles.css
    $htmlParams = @{
    Title = "Relatorio"
    Body = "<h1> Relatório de imagens</h1>"
    Head = "<style> $estilos </style>"
  }
    $resultado |
    ConvertTo-Html @htmlParams |
    Out-File C:\tempGui\relatorio.html
} elseif ( $ExportType -eq "json" ){
    $resultado |
    ConvertTo-Json |
    Out-File C:\tempGui\relatorio.json
} elseif ( $ExportType -eq "csv" ){
    $resultado |
    ConvertTo-Csv |
    Out-File C:\tempGui\relatorio.csv
}