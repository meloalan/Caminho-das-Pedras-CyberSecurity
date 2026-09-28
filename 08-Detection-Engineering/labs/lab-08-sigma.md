# Lab 08: Sigma: seleção, pipeline e revisão

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-07-false-negatives.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-09-testing.md)

## Objetivo

Revisar uma regra e planejar conversão.

## Cenário

Você recebeu uma Sigma de cadeia Office/PowerShell para usar num produto diferente.

## Dados e preparação

Use a regra completa e os casos P01-P03; consulte a baseline anterior 4720 para contraste.

Todos os nomes, hosts, horários, tickets e endereços são fictícios. Não gerar eventos em ambiente corporativo. Os [dados e comandos](README.md) indicam arquivos e limitações.

## Perguntas

1. Qual é o logsource?
2. Qual condição combina seleções?
3. Quais campos precisam de mapping?
4. O que o parser não valida?

## Dicas

Não trate YAML educacional de especificação como Sigma. Não publique query convertida sem conferir fonte.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

A regra usa process_creation/windows; child and parent exige ambos. Image e ParentImage precisam corresponder ao schema real. O parser confirma estrutura, não coleta, pipeline, custo ou resultado. Esboce conversão conceitual e registre backend/versão escolhidos antes de converter. Revise explicação legítima e mapeamento ATT&CK sem declarar ataque.

</details>

## Implementação e limites

Use [Sigma: descrição portável, validação específica](../sigma.md) para o contrato técnico. A especificação vem antes do produto. Quando houver ambiente, compare a implementação escolhida com os mesmos casos e registre diferenças de fonte, campos, janela e agrupamento. Resultado esperado não é evidência de execução em SIEM.

## Entrega e próximo passo

Regra validada estruturalmente, tabela de mapping e review. Registre versão, método, esperado, obtido e lacunas. Avance pelo link ao final.

## Checkpoint

**Qual é o logsource?**

<details>
<summary>Ver resposta</summary>

A regra usa process_creation/windows; child and parent exige ambos.

</details>

[← Tópico anterior](lab-07-false-negatives.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-09-testing.md)
