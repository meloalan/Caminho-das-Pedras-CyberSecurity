# Escrevendo hipóteses sem SIEM

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](dados/README.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-02-validando-telemetria.md)

## Objetivo

Transformar “PowerShell estranho” em pergunta refutável.

## Cenário e dados

Uma equipe relata PowerShell em uma estação financeira. Não há alerta confirmado nem evidência de intenção.

Leia N04 e a hipótese de administração no [pack 03](../../hunts/process/hunt-03-processo-incomum.md). Neste primeiro lab, basta o cenário textual; não execute consultas.

Todos os valores são fictícios. Pré-requisitos: ler o contrato dos dados e o tópico correspondente; editor de texto basta para a trilha offline. Nenhum exercício exige ação ofensiva, criação real de persistência ou implantação de resposta.

## Execução

1. Escreva comportamento, população e período, sem chamar o usuário de atacante.
2. Proponha alternativa de automação de documento e uma segunda alternativa.
3. Liste dados necessários: pai, comando, identidade, contexto e cobertura.
4. Defina o que sustentaria, o que enfraqueceria e o que não seria observável.
5. Escreva condição de encerramento independente de encontrar uma ameaça.

## Perguntas e dicas

Qual informação faria você mudar de opinião? Antes de abrir a solução, anote quais dados sustentam sua resposta e quais permanecem ausentes. Se usar produto, salve query, versão, janela, campos e resultado obtido; se trabalhar offline, registre explicitamente esse modo.

## Solução comentada

<details>
<summary>Ver solução</summary>

Uma hipótese possível: a relação Office → PowerShell em WIN-LAB01 pode estar fora da finalidade esperada. Comando Get-Date e pai WINWORD não decidem intenção. Aprovação específica e conteúdo da automação ajudariam a diferenciar explicações. Sem esses dados, a finalidade permanece inconclusiva.

</details>

## Entrega e critério de conclusão

Hunt Plan com sete elementos: hipótese, alternativa, dados, sustentação, enfraquecimento, escopo e saída.

Uma entrega completa permite outra pessoa reproduzir os pivots e entender o limite da conclusão. Compare seu resultado com o esperado e explique divergências. Não copie a solução como se fosse evidência de execução em SIEM.

## Checkpoint

**Qual informação faria você mudar de opinião?**

<details>
<summary>Ver resposta</summary>

Uma confirmação independente da finalidade e do escopo, ou uma evidência contraditória. Se nenhuma evidência mudaria a conclusão, a hipótese não está sendo realmente testada.

</details>

[← Tópico anterior](dados/README.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-02-validando-telemetria.md)
