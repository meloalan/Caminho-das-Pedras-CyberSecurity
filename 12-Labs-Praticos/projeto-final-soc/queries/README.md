# Queries do projeto

[← Projeto Final](../README.md) · [Página principal](../../../README.md) · [Exemplos para 4720](../../lab-05-detection/README.md) · [Correlação 4625/4624](../../lab-06-brute-force/README.md)

Use `data/events.jsonl` como fixture sintética. Ela segue uma estrutura normalizada didática, não ECS completo nem schema nativo de Sentinel, Splunk ou QRadar. Para cada query, documente mapeamento de campos, tempo, tipo, parser e resultado esperado.

| Tecnologia | Forma | Ajuste necessário |
| --- | --- | --- |
| Sentinel | KQL em SecurityEvent | Ingestão e nomes de coluna; use exemplos do catálogo de queries. |
| Splunk | SPL no índice escolhido | Sourcetype, extrações de campo, timezone e licença. |
| QRadar | AQL mais CRE para correlação | DSM, propriedades customizadas, QID e janela da regra. |
| Elastic | Query DSL / regra EQL | Índice/data stream e mapping ECS. |
| Wazuh | Rules XML e decoder | Versão, decoder EventChannel, regra base e campos extraídos. |

Os exemplos em [Lab 05](../../lab-05-detection/README.md) consultam eventos de criação de conta. O [Lab 06](../../lab-06-brute-force/README.md) documenta a lógica temporal de falhas e sucesso, mais um exemplo KQL com fixtures existentes. Para as outras ferramentas, teste um equivalente com dados de exemplo, inspecione o plano de correlação e mantenha os casos positivos e negativos.
