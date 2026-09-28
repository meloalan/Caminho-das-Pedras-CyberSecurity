# Onze laboratórios de Detection Engineering

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](../referencias.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-01-da-hipotese-aos-dados.md)

## Escolha o percurso

Comece sem código no Lab 01. Depois use os fixtures locais para examinar seleção, tempo e tuning. A etapa de produto é opcional para executar a prática local, mas necessária antes de declarar implementação validada naquele SIEM. Não é preciso instalar quatro plataformas.

| Lab | Entrega principal |
| --- | --- |
| [01: Da hipótese aos dados](lab-01-da-hipotese-aos-dados.md) | Uma especificação de uma página com hipótese e evidência contrária. |
| [02: Primeira detecção: conta criada](lab-02-primeira-deteccao.md) | Template completo, casos esperado/obtido e status experimental. |
| [03: Threshold: 3, 5 ou 10?](lab-03-threshold.md) | Tabela de limiares, população, perdas e decisão justificada. |
| [04: Ordem, chave e janela](lab-04-correlacao-temporal.md) | Matriz temporal com quatro bordas, atraso e estratégia operacional proposta. |
| [05: Processo, pai e contexto](lab-05-process-creation.md) | Regra experimental, mapa de campos, casos esperados e runbook de contexto. |
| [06: Tuning: 100 para 30](lab-06-tuning.md) | Relatório de tuning com diff, métricas, risco e rollback. |
| [07: Encontre o que a exceção esconde](lab-07-false-negatives.md) | Contraexemplo mínimo, teste de regressão e exceção documentada. |
| [08: Sigma: seleção, pipeline e revisão](lab-08-sigma.md) | Regra validada estruturalmente, tabela de mapping e review. |
| [09: Positivo, negativo e qualidade](lab-09-testing.md) | Matriz com comandos, esperado/obtido e limites de teste. |
| [10: Mudança revisável em Git](lab-10-detection-as-code.md) | Diff, comentário de review, changelog e rollback proposto. |
| [11: Detecção completa e caso composto](lab-11-ciclo-completo.md) | Especificação, queries vinculadas, regra candidata, ATT&CK justificado, severidade/confiança, FP/FN, matriz, tuning, runbook, versão e lacunas. |

## Dados disponíveis

- [Casos de conta](../../detections/tests/account-cases.json): registros normalizados e saídas esperadas.
- [Cem candidatos de tuning](../../detections/tests/tuning.jsonl): positivos/negativos artificiais, sem dados pessoais reais.
- [Casos de processo](../../detections/tests/process-cases.json): três cadeias com expectativas de seleção.
- [Dataset do módulo 07](../../07-Buscas-e-Queries-em-SIEM/labs/dados/README.md): eventos de 24/09/2026 UTC e histórico, com inventário.
- [Investigação do módulo 07](../../07-Buscas-e-Queries-em-SIEM/investigacao.md): queries e pivôs para o caso final.

Fixtures não são exports nativos de SIEM nem devem ser inseridos diretamente em SecurityEvent. Tipos e nomes didáticos são documentados no [catálogo de detecções](../../detections/README.md).

## Comandos na raiz do repositório

```sh
python -B -m unittest discover -s detections/tests -v
python detections/tools/evaluate.py
```

Não há rede, deploy ou geração ofensiva nesses comandos. Para o parser Sigma e YAML, siga [Detection as Code](../detection-as-code.md). Preserve resultados locais e declare que não demonstram execução em KQL, SPL, CRE ou Wazuh.

## Modelo de evidência

Pergunta, versão, fixture, população, janela, consulta/lógica, esperado, obtido, diferenças, limites e próximo teste. Quando houver plataforma, registre produto, versão, parser, mapeamento, agendamento e exemplo do alerta.

## Checkpoint

**Preciso instalar os quatro SIEMs para começar?**

<details>
<summary>Ver resposta</summary>

Não. Comece pela hipótese e pelos testes locais. Use um produto disponível quando quiser validar integração, sem afirmar execução nas outras plataformas.

</details>

[← Tópico anterior](../referencias.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-01-da-hipotese-aos-dados.md)
