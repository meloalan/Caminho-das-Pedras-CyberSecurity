# Laboratório final: investigação e relatório

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-11-hunt-to-detection.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](../../10-Incident-Response/README.md)

## Objetivo

Conduzir um hunt completo com explicações concorrentes.

## Cenário e dados

Falhas, sucesso, privilégio, processo, DNS, rede e criação de conta aparecem na mesma manhã, misturados com atividade legítima.

Use todos os [dados fictícios](dados/README.md), [template](../TEMPLATE-HUNT.md) e [relatório](../TEMPLATE-RELATORIO-HUNT.md).

Todos os valores são fictícios. Pré-requisitos: ler o contrato dos dados e o tópico correspondente; editor de texto basta para a trilha offline. Nenhum exercício exige ação ofensiva, criação real de persistência ou implantação de resposta.

## Execução

1. Defina hipótese principal e o que a enfraqueceria.
2. Valide cobertura por host/fonte e retenção.
3. Declare escopo e fim exclusivo, mantendo E20 fora até justificar outro hunt.
4. Registre query inicial e resultado realmente obtido offline ou em produto.
5. Faça pivots por chaves, recusando relações só temporais.
6. Construa timeline com IDs e fontes.
7. Mantenha explicações concorrentes para cada execução.
8. Separe fatos e inferências, especialmente DNS-IP e tarefa-processo.
9. Documente telemetry gaps e detection gaps ainda não comprovados.
10. Conclua por hipótese e escopo, não por uma história única.
11. Escolha outcome com responsável a definir e condição de aceite.
12. Proponha candidata de detecção somente quando justificável.

## Perguntas e dicas

Qual conclusão executiva respeita todos os limites? Antes de abrir a solução, anote quais dados sustentam sua resposta e quais permanecem ausentes. Se usar produto, salve query, versão, janela, campos e resultado obtido; se trabalhar offline, registre explicitamente esse modo.

## Solução comentada

<details>
<summary>Ver solução</summary>

A cadeia E01 a E08 sustenta sequência, com intenção inconclusiva. E09 e N01/N02/N03 são outra cadeia, dependente de C03 para resolução. N07 e conexões têm contexto legítimo C02. N04 pede contexto; N05/N06 não demonstram execução ligada; E20 exige janela própria. Não há evidência suficiente para declarar um ataque único que explique tudo.

</details>

## Entrega e critério de conclusão

Sete artefatos de portfólio: plano, journal, timeline, mapa de pivots, IOC to Behavior, relatório e candidata/justificativa de não automatizar.

Uma entrega completa permite outra pessoa reproduzir os pivots e entender o limite da conclusão. Compare seu resultado com o esperado e explique divergências. Não copie a solução como se fosse evidência de execução em SIEM.

## Checkpoint

**Qual conclusão executiva respeita todos os limites?**

<details>
<summary>Ver resposta</summary>

Há sequências observáveis que merecem revisão contextual e lacunas conhecidas. O conjunto não confirma comprometimento nem permite afirmar ausência de atividade nos ativos sem cobertura.

</details>

[← Tópico anterior](lab-11-hunt-to-detection.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](../../10-Incident-Response/README.md)
