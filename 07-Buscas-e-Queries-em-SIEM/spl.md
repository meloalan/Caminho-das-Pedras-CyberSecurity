# SPL: pesquisa e transformação no Splunk

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](kql.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](aql.md)

## Escolha a população antes do pipe

`index` seleciona o armazenamento pesquisável. `sourcetype` descreve o formato e associa conhecimento de parsing. `source` identifica a entrada/origem configurada. `host` é metadado do evento e pode não ser o Computer original, principalmente com encaminhamento. Neste módulo usamos `lab_host` validado contra o payload.

Os exemplos são SPL clássico, não SPL2. As capacidades de pesquisa do Splunk Enterprise não incluem automaticamente conteúdo/licenciamento do Enterprise Security. Correlações, findings/notables e investigação dependem da edição e versão ES. SOAR é outro componente; uma busca não executa playbooks por si só.

## Ferramentas por finalidade

| Comando | Pergunta que resolve | Limite |
| --- | --- | --- |
| search | Quais eventos correspondem à expressão? | Precedência diferente de where |
| fields | Quais campos manter/remover do processamento? | Pode retirar chave necessária |
| table | Como exibir colunas? | Apresentação no final da busca |
| stats | Qual agregado por grupo? | Colunas fora do agregado desaparecem |
| eventstats | Como anexar agregado aos eventos? | Memória e limite de resultados |
| streamstats | Qual contexto acumulado/janela por linha? | Ordem e limites de janela importam |
| eval | Qual campo derivar? | Nulos e conversões |
| where | Qual predicado sobre valores calculados? | Usa expressões eval |
| sort / head | Qual ordem e quantos resultados? | sort tem limite padrão; sort 0 remove esse limite |
| dedup | Qual representante por combinação? | Não é deduplicação semântica de coleta |
| bin / timechart | Como formar série temporal? | Fronteiras e séries limitadas |
| rex | Que parte do texto extrair? | Regex depende do formato |
| lookup | Que referência acrescentar? | Definição, chave e permissões |
| join | Que conjunto relacionar? | Subsearch e limites podem truncar |
| transaction | Que eventos agrupar como transação? | Custo, memória, eventos incompletos e critérios |

## Percentual sem perder eventos

```spl
index=windows source="XmlWinEventLog:Security" earliest=-24h latest=now EventCode=4625
| stats count AS falhas by lab_host
| eventstats sum(falhas) AS total
| eval percentual=if(total>0,round(100*falhas/total,2),null())
| sort 0 -falhas
| table lab_host falhas total percentual
```

Stats passa de eventos para grupos. Eventstats acrescenta o total a cada grupo. Eval calcula uma proporção com denominador explícito. É percentual de falhas observadas, não de incidentes ou hosts atacados. Grupos sem lab_host precisam ser medidos separadamente para não sumirem do denominador.

## Extração didática, não parser universal

```spl
index=windows source="XmlWinEventLog:Security" earliest=-1h latest=now EventCode=4720
| rex field=_raw "<Data Name='TargetUserName'>(?<alvo_exemplo>[^<]*)</Data>"
| table _time alvo_exemplo _raw
```

Esse rex só demonstra o formato XML com aspas simples mostrado no padrão. XML com aspas duplas, entidades escapadas ou mensagem renderizada exige tratamento apropriado. Prefira extrações do add-on e confira Subject/Target. Um alias não deve transformar campo multivalorado de nomes de conta em alvo único sem evidência.

## Transaction não é solução universal

Comece com stats para resumo, lookup para referência e streamstats para janela ordenada quando adequado. Transaction pode manter muitos eventos em memória e depende de chaves/maxspan/início/fim. Uma transação criada pelo comando não comprova sessão real nem causalidade. Join pode perder linhas por limites do lado direito; declarar isso depois não recupera a completude perdida.

## Prática e referências

Compare `stats count by lab_user` e `eventstats count by lab_user` sobre a mesma amostra: o primeiro reduz linhas; o segundo acrescenta contagem aos eventos. Consulte [stats](https://help.splunk.com/en/splunk-enterprise/search/spl-search-reference/9.4/search-commands/stats), [transaction](https://help.splunk.com/en/splunk-enterprise/search/spl-search-reference/9.4/search-commands/transaction) e [join](https://help.splunk.com/en/splunk-enterprise/search/spl-search-reference/9.4/search-commands/join).

## Checkpoint

**Por que sort 0 deve ser uma decisão consciente?**

<details>
<summary>Ver resposta</summary>

Evita o limite padrão de linhas, mas ordenar toda a população pode ser caro. Restrinja o conjunto sem prejudicar a pergunta.

</details>

[← Tópico anterior](kql.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](aql.md)
