# Validando telemetria antes de procurar

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-01-escrevendo-hipoteses.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-03-authentication-hunt.md)

## Objetivo

Decidir quais partes de uma hipótese podem ser testadas.

## Cenário e dados

O hunt quer relacionar processos e conexões em quatro hosts na janela [08:00Z, 10:00Z).

Use [cobertura.csv](dados/cobertura.csv), [inventário original](../../07-Buscas-e-Queries-em-SIEM/labs/dados/inventario.csv) e [contrato](dados/README.md).

Todos os valores são fictícios. Pré-requisitos: ler o contrato dos dados e o tópico correspondente; editor de texto basta para a trilha offline. Nenhum exercício exige ação ofensiva, criação real de persistência ou implantação de resposta.

## Execução

1. Compare população esperada com host/fonte no CSV.
2. Identifique quais hosts têm Sysmon 1 e quais têm 3/22.
3. Compare retenção com a janela, não apenas presença de agente.
4. Explique o efeito de parser ou campos nulos, mesmo com evento presente.
5. Produza um telemetry gap com responsável a definir e teste de aceite.

## Perguntas e dicas

Retenção de hoje é suficiente para investigar a manhã? Antes de abrir a solução, anote quais dados sustentam sua resposta e quais permanecem ausentes. Se usar produto, salve query, versão, janela, campos e resultado obtido; se trabalhar offline, registre explicitamente esse modo.

## Solução comentada

<details>
<summary>Ver solução</summary>

WIN-LAB01 permite o pivot processo/rede no cenário; WIN-LAB02 possui Sysmon 1, mas não 3/22; WIN-LAB03 não possui Sysmon e sua retenção Security começa às 12:00, depois do período. DC-LAB01 cobre identidade, não uma árvore de processos completa. Zero conexões em WIN-LAB02/03 não refuta comunicação.

</details>

## Entrega e critério de conclusão

Matriz de cobertura com fonte, campo, período, controle positivo e efeito da lacuna.

Uma entrega completa permite outra pessoa reproduzir os pivots e entender o limite da conclusão. Compare seu resultado com o esperado e explique divergências. Não copie a solução como se fosse evidência de execução em SIEM.

## Checkpoint

**Retenção de hoje é suficiente para investigar a manhã?**

<details>
<summary>Ver resposta</summary>

Depende do início efetivo. No WIN-LAB03 começa às 12:00Z, portanto não cobre a janela da manhã.

</details>

[← Tópico anterior](lab-01-escrevendo-hipoteses.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-03-authentication-hunt.md)
