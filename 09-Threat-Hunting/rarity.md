# Raridade, frequência e outliers

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](baselining.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](pivoting.md)

## Um critério de prioridade

**Raro não significa malicioso.** Processo, relação parent-child, domínio, usuário em host ou tipo de login incomum merecem contexto. Frequente também não significa legítimo.

| Medida | O que descreve | O que não conclui |
| --- | --- | --- |
| Único | Uma ocorrência na janela observada | Primeira ocorrência histórica absoluta |
| Raro | Baixa frequência na população comparável | Malícia |
| Burst | Concentração temporal | Brute force sem outros dados |
| Periódico | Intervalos semelhantes | Beaconing adversário |
| Outlier | Desvio de uma referência definida | Comprometimento |

## Exemplo de priorização

Uma conta acessava três hosts e aparece em cinquenta hoje. Confirme se houve inventário novo, mudança de função, implantação, duplicação de logs ou coleta ampliada. Depois examine origem, resultado, tipo de logon e ações posteriores. A contagem isolada não decide a causa.

No [Lab 07](labs/lab-07-baseline-rarity.md), uma ferramenta rara aprovada concorre com um processo raro sem contexto suficiente. Priorize pela combinação de risco do ativo, relação de processo, identidade e lacunas. Não use “raro” como rótulo de ameaça no relatório.

## Ordenar sem perder a população

Um ranking top 10 facilita revisão, mas omite o restante. Registre quantas linhas ficaram fora e amplie quando necessário. Valores nulos não devem virar um grupo supostamente normal. Uma nova versão pode alterar hashes e nomes sem alterar finalidade.

Entregável: uma lista priorizada com justificativa, hipótese alternativa e próximo pivot para cada item. Declare a baseline usada e uma condição capaz de mudar a prioridade.

## Checkpoint

**Um processo muito comum pode estar sendo abusado?**

<details>
<summary>Ver resposta</summary>

Sim. Prevalência descreve distribuição, não intenção. Usuário, argumentos, pai, destino e contexto continuam relevantes.

</details>

[← Tópico anterior](baselining.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](pivoting.md)
