# Cobertura real e dívida de detecção

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](mitre-mapping.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](detection-health.md)

## Uma cadeia de dependências

Cobertura depende de telemetria + implantação + campos + lógica + validação + ambiente. Basta uma peça faltar para que um comportamento permaneça invisível. A matriz deve distinguir “mapeado”, “implementado”, “testado” e “observável”.

![Cobertura depende de população, fonte, campos e testes](../assets/images/08-detection-engineering/cobertura.svg)

## Matriz fictícia de laboratório

| Comportamento | Fonte | Telemetria | Regra | Testada | Cobertura declarada |
| --- | --- | --- | --- | --- | --- |
| Criação de conta | Security 4720 | Contrato definido, coleta real pendente | Baseline experimental | Seleção em fixture | Somente comportamento dos dados artificiais |
| Processo Office → PowerShell | Process creation | Mapping a validar | Sigma experimental | Parser; casos esperados descritos | Sem porcentagem operacional comprovada |
| Falhas → sucesso | Security 4625/4624 | Dados sintéticos do módulo 07 | Lógica de referência Python | Tempo, identidade e qualidade | Mesmo contrato e população do fixture |
| Rede após processo | Sysmon 3 | Depende de sensor/configuração | Proposta composta | Investigação do fixture | Não afirmar cobertura de endpoints |

## Denominador antes do percentual

Exemplo separado e fictício: de dez endpoints de escopo definido, sete enviam Sysmon 1 no período observado. Implantação observada é 7/10 = 70%; três não foram confirmados. Isso não significa detectar 70% dos ataques nem cobrir 70% de uma técnica. Ainda é preciso verificar campos, lógica e testes nos sete.

Diferencie inventário, população elegível, exclusões e fonte observada. Se o inventário está desatualizado, o denominador é incerto. Registre data e responsável em vez de produzir precisão aparente.

## Três lacunas diferentes

| Situação | Próximo trabalho |
| --- | --- |
| Técnica relevante sem telemetria | Priorizar fonte, auditoria ou aceitar risco explicitamente |
| Telemetria presente sem lógica | Desenvolver hipótese e caso de uso |
| Regra existente nunca testada | Validar antes de declarar capacidade |

## Dívida operacional

Regra sem owner, documentação incompleta, query antiga, campo removido, exceção sem validade, volume impraticável e mapping incorreto acumulam risco. Transforme cada dívida em item com impacto, dependência, responsável e condição de encerramento. Priorize pelo risco e pela capacidade afetada, não pelo número de arquivos.

**Entrega:** copie a matriz para seu portfólio e preencha com dados fictícios ou de laboratório próprio revisados. Inclua uma lacuna de fonte, uma de lógica e uma de validação. Declare explicitamente onde não há prova de implantação.

## Checkpoint

**Sete de dez hosts enviando logs é recall de 70%?**

<details>
<summary>Ver resposta</summary>

Não. É uma medida de implantação observada naquele inventário e período. Recall exige conhecer casos positivos e quantos foram identificados.

</details>

[← Tópico anterior](mitre-mapping.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](detection-health.md)
