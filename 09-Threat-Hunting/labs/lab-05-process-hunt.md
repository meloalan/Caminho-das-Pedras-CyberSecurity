# Processos e relação parent-child

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-04-account-hunt.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-06-pivoting.md)

## Objetivo

Priorizar execuções e reconhecer duas fontes do mesmo fato.

## Cenário e dados

PowerShell aparece por Sysmon e por Security, com pais e contas diferentes.

Use E06/E12/E13/N04/N07, baseline e contexto. Leia [processos](../process-hunting.md).

Todos os valores são fictícios. Pré-requisitos: ler o contrato dos dados e o tópico correspondente; editor de texto basta para a trilha offline. Nenhum exercício exige ação ofensiva, criação real de persistência ou implantação de resposta.

## Execução

1. Liste execução, host, pai, usuário, comando e fonte.
2. Não conte E12/E13 como duas execuções.
3. Compare N04 com o histórico de mesma população.
4. Diferencie a linha de criação dos comandos que poderiam ocorrer depois.
5. Escreva qual dado falta para confirmar ou enfraquecer a finalidade indevida.

## Perguntas e dicas

Processo raro e comando benigno encerram o caso? Antes de abrir a solução, anote quais dados sustentam sua resposta e quais permanecem ausentes. Se usar produto, salve query, versão, janela, campos e resultado obtido; se trabalhar offline, registre explicitamente esse modo.

## Solução comentada

<details>
<summary>Ver solução</summary>

E12/E13 são registros de uma criação. N04 é parent-child não presente no baseline, com comando benigno e finalidade desconhecida. E06 permanece interativo, logo sua command line não explica tudo que ocorreu depois. N07 tem C02 específico, não extensível aos demais.

</details>

## Entrega e critério de conclusão

Matriz de execuções priorizadas com evidência, alternativa e próximo pivot.

Uma entrega completa permite outra pessoa reproduzir os pivots e entender o limite da conclusão. Compare seu resultado com o esperado e explique divergências. Não copie a solução como se fosse evidência de execução em SIEM.

## Checkpoint

**Processo raro e comando benigno encerram o caso?**

<details>
<summary>Ver resposta</summary>

Nenhum dos dois sozinho. É preciso confrontar hipótese e contexto, mantendo o limite do que foi registrado.

</details>

[← Tópico anterior](lab-04-account-hunt.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-06-pivoting.md)
