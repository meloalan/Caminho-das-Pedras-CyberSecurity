# Timeline com dados embaralhados

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-08-ioc-to-behavior.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-10-multisiem-hunt.md)

## Objetivo

Ordenar sem fabricar causalidade.

## Cenário e dados

O suplemento está em ordem inversa; o original mistura horários e histórico.

Use ambos os JSONL descritos em [dados](dados/README.md).

Todos os valores são fictícios. Pré-requisitos: ler o contrato dos dados e o tópico correspondente; editor de texto basta para a trilha offline. Nenhum exercício exige ação ofensiva, criação real de persistência ou implantação de resposta.

## Execução

1. Converta timestamp para UTC e selecione [08:00Z, 10:00Z).
2. Ordene por tempo, preservando ID e fonte.
3. Separe cadeias de autenticação, identidade e processo.
4. Marque E20 fora da janela e histórico H01/H02 fora do dia.
5. Escreva uma observação e uma inferência separadas para cada cadeia.

## Perguntas e dicas

Por que não ordenar por ID? Antes de abrir a solução, anote quais dados sustentam sua resposta e quais permanecem ausentes. Se usar produto, salve query, versão, janela, campos e resultado obtido; se trabalhar offline, registre explicitamente esse modo.

## Solução comentada

<details>
<summary>Ver solução</summary>

Há 26 registros na janela combinada. E17/E18/E19 são anteriores, E20 está no fim exclusivo e H01/H02 são históricos. N05/N06 não comprovam execução posterior N07 por proximidade. E09/N01/N02/N03 formam uma cadeia de identidade com C03, distinta de E04/E06.

</details>

## Entrega e critério de conclusão

Timeline com fatos, relações, limites e eventos excluídos por escopo.

Uma entrega completa permite outra pessoa reproduzir os pivots e entender o limite da conclusão. Compare seu resultado com o esperado e explique divergências. Não copie a solução como se fosse evidência de execução em SIEM.

## Checkpoint

**Por que não ordenar por ID?**

<details>
<summary>Ver resposta</summary>

IDs são identificadores do fixture, não uma garantia temporal. Use timestamp e registre empates/precisão; não deduza causalidade da ordenação.

</details>

[← Tópico anterior](lab-08-ioc-to-behavior.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-10-multisiem-hunt.md)
