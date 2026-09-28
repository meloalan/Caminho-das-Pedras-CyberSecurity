# Uma pergunta em quatro contratos

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-09-timeline.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-11-hunt-to-detection.md)

## Objetivo

Comparar implementações sem exigir quatro produtos.

## Cenário e dados

O mesmo hunt de falhas/sucesso precisa ser reproduzível em outra plataforma.

Use [multisiem-hunting](../multisiem-hunting.md) e os schemas do módulo 07.

Todos os valores são fictícios. Pré-requisitos: ler o contrato dos dados e o tópico correspondente; editor de texto basta para a trilha offline. Nenhum exercício exige ação ofensiva, criação real de persistência ou implantação de resposta.

## Execução

1. Descreva pergunta, janela e chave antes de escolher sintaxe.
2. Mapeie cada campo entre fixture e KQL/SPL/AQL/DSL.
3. Leia os quatro blocos e identifique índices, aliases e propriedades que precisam existir.
4. Compare alertas versus archives, coalescência, limite de linhas e fuso.
5. Escolha uma plataforma se disponível; registre não executado para as demais.

## Perguntas e dicas

Pode afirmar equivalência porque todas contêm 4624 e 4625? Antes de abrir a solução, anote quais dados sustentam sua resposta e quais permanecem ausentes. Se usar produto, salve query, versão, janela, campos e resultado obtido; se trabalhar offline, registre explicitamente esse modo.

## Solução comentada

<details>
<summary>Ver solução</summary>

As entradas selecionam candidatos, não implementam automaticamente correlação equivalente. Sem aliases/propriedades/mappings, a query não tem o mesmo significado. QRadar pode coalescer; Wazuh alerts pode omitir sucessos; clientes podem truncar. O resultado esperado do fixture não é evidência de execução no produto.

</details>

## Entrega e critério de conclusão

Matriz de tradução, resultado esperado e campo separado para resultado obtido.

Uma entrega completa permite outra pessoa reproduzir os pivots e entender o limite da conclusão. Compare seu resultado com o esperado e explique divergências. Não copie a solução como se fosse evidência de execução em SIEM.

## Checkpoint

**Pode afirmar equivalência porque todas contêm 4624 e 4625?**

<details>
<summary>Ver resposta</summary>

Não. População, tempo, tipos, chave, retenção e pós-processamento também precisam coincidir.

</details>

[← Tópico anterior](lab-09-timeline.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-11-hunt-to-detection.md)
