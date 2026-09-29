# Avaliação honesta de cobertura

[← Índice do módulo](README.md) · [Mapeamento](detection-mapping.md) · [Navigator](attack-navigator.md) · [Template de avaliação](TEMPLATE-COVERAGE-ASSESSMENT.md)

## Mapeamento não é cobertura

```text
Técnica mapeada ≠ técnica coberta completamente
Todas as células coloridas ≠ ambiente protegido
```

Uma regra etiquetada com T1059.001 pode cobrir apenas um padrão estreito, numa plataforma, com campos específicos. Uma layer representa a avaliação declarada por quem a criou. Ela não prova que a fonte existe nos ativos, que a lógica é eficaz ou que a resposta funciona.

Não use percentual agregado de matriz como objetivo sem definir denominador, escopo, validade, risco e método. Uma taxa pode esconder fontes ausentes, falsos positivos, ativos sem agente, casos não testados e técnicas irrelevantes. Priorize comportamento relevante, exposição, impacto, probabilidade, mitigação disponível, qualidade da telemetria e custo de melhoria.

## Dimensões mínimas

| Dimensão | Registro esperado |
| --- | --- |
| Comportamento | Técnica ou subtécnica e manifestação exata em escopo. |
| Ativos e plataformas | Sistemas aplicáveis e proporção da população relevante com fonte disponível. |
| Telemetria | Fontes, Data Components, campos, configuração, ingestão e retenção. |
| Lógica | Regra, consulta ou analytic e dependências. |
| Validação | Testes positivos e negativos, data e ambiente. |
| Resposta | Triagem, enriquecimento, contenção e responsável. |
| Limitações | Usos legítimos, variantes não observadas e dados ausentes. |
| Estado | Proposta, implementada, validada, degradada ou fora de escopo. Estados são convenção local. |

## Tipos de lacuna

- **Telemetry Gap:** fonte, campo ou cobertura de ativos insuficiente.
- **Detection Gap:** telemetria adequada existe, mas não há lógica útil ou a lógica falha nos testes.
- **Validation Gap:** há regra ou fonte, mas faltam evidências de teste, escopo ou eficácia.
- **Response Gap:** alerta existe, mas triagem, contexto, playbook ou responsável não estão definidos.

Uma mesma técnica pode ter mais de uma lacuna. Classifique com evidência para que a ação correta seja priorizada.

## Prioridade prática

Escolha uma manifestação relevante e limite a avaliação à população realmente importante. Confirme se a fonte está implantada. Teste a lógica. Registre o que passa e o que não passa. Estime impacto com os responsáveis de risco. Abra ações com responsável, prazo e critério de fechamento. Reavalie após mudança de ambiente ou ATT&CK.

## Exemplo

Uma consulta de PowerShell está validada em 80 de 100 endpoints Windows em escopo e exige uma linha de comando que não está disponível nos outros 20. Descreva a cobertura como uma manifestação específica, testada em 80 ativos. Registre Telemetry Gap nos 20 restantes e limite da lógica para execuções que não correspondem ao filtro. Não declare 80% de T1059.001 coberto: outras plataformas e manifestações não estão representadas pelo cálculo.

## Plano de ação

Use o [template de avaliação](TEMPLATE-COVERAGE-ASSESSMENT.md). A camada ATT&CK Navigator pode resumir uma análise, mas o registro detalhado precisa explicar fonte, lógica, distribuição e teste.
