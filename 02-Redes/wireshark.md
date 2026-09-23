# Wireshark

[← Índice do módulo](README.md) · [Página principal](../README.md)

## Conceito

Capturas mostram pacotes visíveis na interface selecionada. Filtro de captura reduz o que é coletado; filtro de exibição seleciona o que é mostrado. Capturas podem conter dados pessoais e segredos.

## Prática orientada

Capture somente tráfego da VM de teste. Use filtros de exibição `dns`, `tcp.flags.syn == 1` e `http`. Relacione horário, IP e porta sem publicar a captura bruta.

## Entrega para o portfólio

Três observações com filtros e explicação do que a captura não permite concluir.

## Critério de conclusão

Explique o resultado com suas palavras, registre as limitações e diferencie o que foi observado do que foi inferido. Dados de laboratório devem ser anonimizados antes da publicação.
