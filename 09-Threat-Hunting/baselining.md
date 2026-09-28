# Baseline é referência, não garantia

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](hunting-telemetry.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](rarity.md)

## Comparar populações semelhantes

Uma baseline descreve o que foi observado sob determinadas condições. Atividade indevida persistente também pode entrar no histórico. Uma mudança legítima pode parecer anormal. **Baseline não equivale a comportamento seguro.**

| Dimensão | Pergunta |
| --- | --- |
| Usuário e função | Um administrador e uma pessoa do financeiro têm tarefas comparáveis? |
| Host e tipo de ativo | Servidor de automação e estação de trabalho têm o mesmo papel? |
| Grupo e segmento | A cobertura é semelhante entre as populações? |
| Horário e dia da semana | Há manutenção, fechamento mensal ou sazonalidade? |
| Aplicação | Houve implantação ou mudança de versão? |

## Método reproduzível

Defina período histórico anterior ao período de interesse, unidade de contagem, cobertura elegível e dimensões. Conte execuções, não registros duplicados de Security/Sysmon da mesma execução. Não inclua o dia investigado no histórico sem declarar o efeito sobre a comparação.

O [baseline.csv](labs/dados/baseline.csv) é um resumo fictício de sete dias, não eventos brutos. Traz processo, pai, usuário, host, contagem e primeiro/último observado. Sua população possui apenas dois hosts com Sysmon 1. Portanto um processo em um host tem prevalência observada 1/2, não 1/4 do inventário como se todos fossem observáveis.

## First seen, last seen e prevalência

First seen é a primeira ocorrência **observada dentro do histórico consultado**. Não significa primeira execução na vida do ativo. Last seen também depende de coleta e retenção. Prevalência é o número de entidades distintas com o comportamento dividido pela população elegível observada, quando expresso como proporção.

No fixture, taskeng.exe → powershell.exe para LAB/svc.lab em WIN-LAB02 tem 14 execuções históricas. WINWORD.EXE → powershell.exe em WIN-LAB01 não aparece no resumo. Isso prioriza a segunda relação, mas o histórico curto e os filtros de coleta limitam a comparação.

## Entrega

Registre baseline v1, período, fontes, unidade, população e exceções conhecidas. Liste mudança legítima e comprometimento persistente como limitações. Conecte o resultado à próxima pergunta em [raridade](rarity.md).

## Checkpoint

**Por que não dividir prevalência pelos quatro hosts inventariados?**

<details>
<summary>Ver resposta</summary>

Porque dois não têm a mesma cobertura de processo no exercício. O denominador precisa representar quem poderia ter produzido o observável.

</details>

[← Tópico anterior](hunting-telemetry.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](rarity.md)
