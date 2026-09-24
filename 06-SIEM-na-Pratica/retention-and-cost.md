# Retenção, volume e custo operacional

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](siem-health.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](wazuh.md)

## Dimensionar a pergunta

Escolha quanto histórico precisa para investigar e quais fontes sustentam detecção. Ingestão, indexação, armazenamento, consulta, recuperação, automação e operação podem gerar custos diferentes. Modelos de licenciamento variam por produto, edição e contrato; este módulo não fixa preços comerciais.

## EPS e GB por dia

EPS significa eventos por segundo. Média ajuda a estimar volume; pico e burst influenciam buffer, capacidade e atraso. Uma média de uma hora esconde rajadas de segundos. Tamanho de evento varia por fonte e enriquecimento.

Exemplo **hipotético**, não benchmark: 500 endpoints, média de 2 eventos/segundo por endpoint e 1.000 bytes por evento.

```text
500 × 2 = 1.000 eventos/segundo
1.000 × 1.000 × 86.400 = 86.400.000.000 bytes/dia
86.400.000.000 / 1.000.000.000 = 86,4 GB/dia (decimal)
86,4 × 30 = 2.592 GB brutos em 30 dias
```

Isso não estima diretamente disco necessário nem preço. Compressão, réplicas, índices, metadados, retenção por camada, reservas e formato cobrado mudam o resultado. Se o pico hipotético for 5.000 EPS durante cinco minutos, o sistema precisa processar ou armazenar a diferença sem perder dados; a média diária sozinha não responde se consegue.

## Camadas e disponibilidade

| Conceito | Pergunta |
| --- | --- |
| Hot | Está prontamente consultável e por quais regras? |
| Warm/cold/histórico | Como pesquisar ou recuperar, com qual atraso? |
| Arquivo | Está preservado, íntegro e acessível sob qual processo? |
| Retenção | Quando cada categoria expira e quem define isso? |
| Indexação | Que estrutura acelera pesquisa e quanto ocupa? |

Os nomes não são equivalentes entre fornecedores. No Splunk, termos de buckets têm significado próprio. Wazuh usa políticas do indexer e arquivos do manager conforme configuração. QRadar tem políticas e armazenamento de Ariel. Sentinel combina tabelas/planos e retenção conforme recursos atuais. Regra de dados recentes não consulta automaticamente todo o histórico guardado.

## Custo operacional também conta

Inclua administração, atualização, backup/recuperação, teste de parser, tuning, investigação, acessos e disponibilidade. Wazuh não ter o mesmo modelo comercial de um SIEM licenciado não elimina hardware e trabalho de manutenção. Dados “baratos” sem qualidade podem custar muito tempo de análise.

## Escolher o que coletar

Priorize dados necessários para casos de uso, investigação e obrigações aplicáveis. Meça valor, volume e lacunas antes de descartar uma fonte. Filtrar cedo pode reduzir custo e tornar uma pergunta futura impossível; guardar tudo sem governança pode prejudicar privacidade e disponibilidade.

## Prática

Estime três cenários com tamanhos e taxas hipotéticas diferentes. Separe volume bruto, retenção, margem de burst, recuperação e custo operacional. Para cloud, planeje orçamento e acompanhamento; alertas de orçamento não bloqueiam automaticamente gastos. Não crie recursos pagos apenas para preencher este exercício.

## Checkpoint

**GB brutos calculados são iguais a disco ou cobrança?**

<details>
<summary>Ver resposta</summary>

Não. Formato, compressão, índices, réplicas, planos e contratos mudam a medida.

</details>

**Por que considerar picos além da média?**

<details>
<summary>Ver resposta</summary>

Rajadas podem saturar buffers e atrasar dados mesmo com volume médio aparentemente adequado.

</details>

[← Tópico anterior](siem-health.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](wazuh.md)
