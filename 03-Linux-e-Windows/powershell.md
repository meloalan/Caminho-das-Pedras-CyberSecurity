# PowerShell

[← Índice do módulo](README.md) · [Página principal](../README.md)

## Conceito

PowerShell trabalha com objetos. `Get-Process | Select-Object Name,Id` seleciona propriedades; `Where-Object` filtra objetos. Execução do PowerShell é comum em administração.

## Prática orientada

Execute `Get-Date`, `Get-Process` e `Get-WinEvent -ListLog Security`. Consulte ajuda antes de modificar o sistema. Compare execução de processo com registro de conteúdo de script, que exige outra telemetria.

## Entrega para o portfólio

Comandos benignos, saída anonimizada e distinção entre Sysmon 1 e logs de script.

## Critério de conclusão

Explique o resultado com suas palavras, registre as limitações e diferencie o que foi observado do que foi inferido. Dados de laboratório devem ser anonimizados antes da publicação.
