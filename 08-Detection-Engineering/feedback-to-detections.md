# Hunting, incidentes e inteligência como entradas

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](runbooks.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](versioning.md)

## De hunt para detecção

Hipótese de hunting → query → achado repetível → padrão → validação → detecção candidata. Nem todo hunt deve virar regra: uma investigação única ou uma busca que exige julgamento manual profundo pode continuar como procedimento de pesquisa.

Antes de automatizar, confira repetibilidade, observabilidade, acionabilidade, volume, contexto e capacidade do SOC. Uma query que exige horas para executar pode ser útil em um hunt e inadequada para uma regra a cada cinco minutos.

## De incidente para nova hipótese

Incidente → timeline → comportamento observado → lacuna → hipótese → capacidade candidata. Pergunte por que a atividade não foi vista: fonte faltante, lógica insuficiente, regra não executada ou sinal ignorado? Cada resposta exige uma melhoria diferente.

Não escreva uma regra que reconhece apenas o nome exato do arquivo daquele caso e a declare cobertura do comportamento inteiro. Esse indicador pode ajudar uma busca imediata, mas a capacidade duradoura exige escopo próprio.

## De inteligência para detecção

Inteligência → indicador/comportamento → relevância ao ambiente → telemetria → hipótese → teste. Verifique procedência, confiança, validade e população. Um IP compartilhado ou domínio expirado pode gerar contexto insuficiente. Um feed não substitui o runbook nem a validação do parser.

## Exemplo de reunião fictícia

SOC relata que as criações de contas já chegam completas, mas sem vínculo com mudança aprovada. Engenharia identifica a necessidade de contexto; identidade fornece registro de mudanças; o responsável define critérios de correspondência. Os testes incluem falta de contexto e uma criação fora da janela, antes de qualquer supressão.

O ganho não é simplesmente “mais uma regra”. É tornar uma decisão reproduzível e reduzir ambiguidade sem ocultar atividade relevante.

## Portfólio proposto

| Projeto | Entrega verificável |
| --- | --- |
| 1. Detection specification | Contrato preenchido e limites |
| 2. Sigma | Regra experimental, mapping e revisão |
| 3. Matriz de testes | Positivo, negativo, limite e qualidade |
| 4. Tuning | Antes/depois, FP/FN e risco |
| 5. Coverage matrix | População, fonte, teste e lacunas |
| 6. Detection as Code | Diff, histórico e rollback proposto |

Todos usam dados fictícios. Declare quais testes foram executados localmente e quais dependem de um produto. Esses artefatos mostram raciocínio, inclusive quando a hipótese é descartada.

## Checkpoint

**Todo achado de incidente deve virar regra agendada?**

<details>
<summary>Ver resposta</summary>

Não. Avalie repetibilidade, dados, contexto, custo e ação. Uma busca pontual, melhoria de coleta ou runbook pode ser a resposta adequada.

</details>

[← Tópico anterior](runbooks.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](versioning.md)
