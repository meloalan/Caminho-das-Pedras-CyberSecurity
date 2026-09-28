# Dados fictícios e resultados verificáveis

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](../README.md) · [↑ Índice do módulo](../../README.md) · [Página principal](../../../README.md) · [Próximo tópico →](../lab-01-escrevendo-hipoteses.md)

## Fontes do exercício

| Arquivo | Conteúdo e papel |
| --- | --- |
| [Dataset original](../../../07-Buscas-e-Queries-em-SIEM/labs/dados/eventos.jsonl) | 22 registros, E01 a E20 e H01/H02 históricos; preservado |
| [Contrato original](../../../07-Buscas-e-Queries-em-SIEM/labs/dados/README.md) | Semântica e limites do módulo 07 |
| [eventos-complementares.jsonl](eventos-complementares.jsonl) | Dez registros N01 a N10, em ordem inversa proposital |
| [cobertura.csv](cobertura.csv) | Sete linhas host/fonte, disponibilidade simulada e retenção |
| [baseline.csv](baseline.csv) | Quatro grupos resumidos, 38 execuções fictícias em sete dias anteriores |
| [contexto.json](contexto.json) | Seis registros administrativos independentes simulados |
| [indicadores.json](indicadores.json) | Dois indicadores reservados com validade explícita |

Não concatene as 38 execuções resumidas com eventos como se fossem 38 registros brutos adicionais. H01/H02 são amostras históricas, não uma reprodução de todo o baseline. Não há hashes de executáveis; qualquer exercício por hash permanece conceitual.

## Contrato

Cada evento tem id exclusivo no fixture, synthetic=true, timestamp ISO UTC, provider, event_id inteiro e host. ID não é EventRecordID nativo. Domain/user representam a conta observada; actor/actor_domain representam o autor de mudança; member/member_sid representam o membro incluído; group/group_sid representam o grupo. Não trocar esses papéis.

Logon_id está normalizado como string hexadecimal; process_id é inteiro decimal. Process_guid é string da execução Sysmon. Task_action/principal/trigger são campos extraídos de TaskContent didático, não um evento XML completo. Service_* descrevem configuração, não prova de início do serviço. Campos ausentes ficam ausentes.

O suplemento não acrescenta IP, SID ou comandos aos registros antigos. C03 fornece uma resolução de inventário explícita para o SID de novo.lab; sem essa resolução, a ligação por identidade seria mais limitada.

## Resultados esperados

| Pergunta | Resposta nos arquivos |
| --- | --- |
| Total de eventos combinados | 32; 30 de 24/09 e dois históricos |
| Dentro de [08:00Z, 10:00Z) de 24/09 | 26 registros; E17/E18/E19 são anteriores e E20 está na borda final |
| Falhas/sucessos no WIN-LAB01, janela principal | E01/E02/E03/E04/E10 |
| Sequência candidata da mesma chave | E01/E02/E03 → E04; três falhas, não quatro |
| Execução Sysmon de E06 | E06/E07/E08 |
| Conta recém-criada com atividade | E09, resolução C03, N01/N02/N03; E14 também envolve o membro |
| Office → PowerShell | N04; não aparece no baseline fornecido |
| Serviço/tarefa criados | N05/N06; sem execução comprovada vinculada |
| Conexões periódicas | N08/N09/N10, intervalos de 300 segundos, mesma execução N07 |
| Fonte sem cobertura na janela | WIN-LAB03; não equivale a host seguro |
| Duas fontes da mesma criação | E12/E13; não contar como duas execuções |

E20 às 10:00 está fora da janela principal. O hunt de limpeza usa explicitamente [09:30Z, 10:30Z). A janela não deve mudar silenciosamente para caber na narrativa.

## Reprodução offline

Abra JSONL/CSV como texto e filtre pelos critérios das páginas. Para os cálculos do conjunto original, a partir da raiz do repositório:

```text
python 07-Buscas-e-Queries-em-SIEM/labs/dados/analisar.py
python -B -m unittest discover -s detections/tests -v
```

O primeiro analisa somente os 22 registros originais; o segundo executa testes do avaliador de detecção do módulo 08, não destes hunts completos nem de um produto. Para o suplemento, confira IDs, chaves e as tabelas de resultados acima. Não é necessário instalar um SIEM.

## Dados seguros e limites

Contas/hosts são fictícios. IPs usam 192.0.2.0/24, 198.51.100.0/24 ou 203.0.113.0/24. Domínio usa .test. Não são endpoints reais para consultar. A disponibilidade de cobertura é um artefato didático, não uma medição de infraestrutura real. Não houve ingestão ou execução destes eventos em produtos.

## Checkpoint

**Por que o evento E20 não aparece na janela principal?**

<details>
<summary>Ver resposta</summary>

O fim é exclusivo às 10:00Z e E20 ocorre exatamente ali. O hunt de limpeza declara outra janela, sem alterar a investigação inicial silenciosamente.

</details>

[← Tópico anterior](../README.md) · [↑ Índice do módulo](../../README.md) · [Página principal](../../../README.md) · [Próximo tópico →](../lab-01-escrevendo-hipoteses.md)
