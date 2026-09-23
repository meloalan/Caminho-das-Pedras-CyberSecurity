# Portas e protocolos

[← Índice do módulo](README.md) · [Página principal](../README.md)

## Conceito

Portas identificam serviços de transporte, mas não confirmam a aplicação. Exemplos convencionais: DNS 53 UDP/TCP, HTTP 80 TCP, HTTPS 443 TCP e também UDP com HTTP/3, SSH 22 TCP, RDP 3389 TCP/UDP.

## Prática orientada

Use `Get-NetTCPConnection` para associar uma conexão local ao processo. Compare serviço esperado, endereço e estado. Evite varreduras de redes alheias.

## Entrega para o portfólio

Tabela de cinco serviços com protocolo, porta convencional e possibilidade de portas alternativas.

## Critério de conclusão

Explique o resultado com suas palavras, registre as limitações e diferencie o que foi observado do que foi inferido. Dados de laboratório devem ser anonimizados antes da publicação.
