# Do IOC ao comportamento

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-07-baseline-rarity.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-09-timeline.md)

## Objetivo

Usar indicador como ponto de entrada com validade.

## Cenário e dados

Um domínio fictício coincide com uma consulta DNS e um IP da execução está numa lista expirada.

Use [indicadores.json](dados/indicadores.json), E06/E07/E08 e o [hunt 08](../../hunts/network/hunt-08-dns-processo.md).

Todos os valores são fictícios. Pré-requisitos: ler o contrato dos dados e o tópico correspondente; editor de texto basta para a trilha offline. Nenhum exercício exige ação ofensiva, criação real de persistência ou implantação de resposta.

## Execução

1. Confira fonte, confiança, first/last seen e expiração.
2. Localize E07 e recupere execução E06.
3. Examine E08 sem inventar resposta DNS.
4. Explique o efeito da expiração do indicador IP na janela.
5. Escreva uma hipótese comportamental que não dependa do valor exato do IOC.

## Perguntas e dicas

Um match com indicador de confiança baixa comprova comprometimento? Antes de abrir a solução, anote quais dados sustentam sua resposta e quais permanecem ausentes. Se usar produto, salve query, versão, janela, campos e resultado obtido; se trabalhar offline, registre explicitamente esse modo.

## Solução comentada

<details>
<summary>Ver solução</summary>

IOC-LAB-001 é válido no exercício, mas não tem reputação maliciosa real. IOC-LAB-002 expirou antes do hunt; não é indicador ativo. E07/E08 se ligam à execução E06, sem resolução domínio-IP demonstrada. Comportamento e finalidade continuam dependentes de contexto.

</details>

## Entrega e critério de conclusão

Ficha IOC, mapa de pivots e conclusão limitada, sem consulta a serviços externos.

Uma entrega completa permite outra pessoa reproduzir os pivots e entender o limite da conclusão. Compare seu resultado com o esperado e explique divergências. Não copie a solução como se fosse evidência de execução em SIEM.

## Checkpoint

**Um match com indicador de confiança baixa comprova comprometimento?**

<details>
<summary>Ver resposta</summary>

Não. Confirma somente a correspondência do valor no campo pesquisado, sob aquele contrato e período.

</details>

[← Tópico anterior](lab-07-baseline-rarity.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-09-timeline.md)
