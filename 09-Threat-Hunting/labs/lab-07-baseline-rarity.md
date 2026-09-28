# Baseline e raridade sem veredito automático

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-06-pivoting.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-08-ioc-to-behavior.md)

## Objetivo

Priorizar com denominador e contexto.

## Cenário e dados

Uma execução rara aprovada concorre com uma relação rara sem contexto administrativo.

Use [baseline.csv](dados/baseline.csv), N04, C06 e [cobertura](dados/cobertura.csv).

Todos os valores são fictícios. Pré-requisitos: ler o contrato dos dados e o tópico correspondente; editor de texto basta para a trilha offline. Nenhum exercício exige ação ofensiva, criação real de persistência ou implantação de resposta.

## Execução

1. Declare o período histórico e a unidade: 38 execuções resumidas, não 38 eventos brutos.
2. Compare inventory.exe raro com Office → PowerShell ausente no resumo.
3. Justifique a população de dois hosts com Sysmon 1.
4. Calcule prevalência observada de uma relação presente em um host dessa população.
5. Proponha próximo pivot e condição para rever a prioridade.

## Perguntas e dicas

Ausente no resumo significa nunca executado? Antes de abrir a solução, anote quais dados sustentam sua resposta e quais permanecem ausentes. Se usar produto, salve query, versão, janela, campos e resultado obtido; se trabalhar offline, registre explicitamente esse modo.

## Solução comentada

<details>
<summary>Ver solução</summary>

Um host em dois elegíveis representa 50% de prevalência observada para a relação definida, não 25% de quatro ativos com cobertura desigual. C06 contextualiza inventory.exe; N04 carece de explicação. A prioridade favorece coletar contexto de N04, sem classificá-lo como malicioso. O resumo de sete dias é limitado.

</details>

## Entrega e critério de conclusão

Ranking justificado, baseline versionada, denominador e limitações.

Uma entrega completa permite outra pessoa reproduzir os pivots e entender o limite da conclusão. Compare seu resultado com o esperado e explique divergências. Não copie a solução como se fosse evidência de execução em SIEM.

## Checkpoint

**Ausente no resumo significa nunca executado?**

<details>
<summary>Ver resposta</summary>

Não. Significa não observado no histórico fornecido, sob a cobertura e os filtros declarados.

</details>

[← Tópico anterior](lab-06-pivoting.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-08-ioc-to-behavior.md)
