# Lab 09: Query para apoiar detecção

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-08-threat-hunting.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-10-investigacao-multisiem.md)

## Objetivo

Especificar e testar uma condição antes de agendar regra.

## Cenário

Você deve avaliar mais de dez falhas em cinco minutos e comparar com o cenário existente.

## Dados

Cinco falhas atuais; matriz sintética adicional descrita, sem alterar os originais. Todos os nomes, hosts, horários e endereços são fictícios. Dia atual do exercício: 24/09/2026 UTC.

[Dataset e tipos](dados/README.md) · [Eventos JSONL](dados/eventos.jsonl) · [Inventário](dados/inventario.csv).

## Perguntas

1. Qual é a unidade e chave do agregado?
2. Bins fixos equivalem à janela anterior a agora?
3. O fixture deve gerar resultado com limiar >10?
4. Quais testes negativos impedem falso vínculo?

## Dicas

Escolha a janela antes de traduzir. Mantenha limiar, autoridade e host explícitos.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

O fixture não atende >10, portanto resultado esperado é vazio. Dez também não atende; onze ocorrências únicas na mesma chave/janela atendem. Teste homônimos, fronteiras, duplicatas e campo ausente. KQL/SPL com bins e AQL/DSL com janela corrente ilustram abordagens diferentes; iguale o intervalo antes de comparar.

</details>

## Tradução e execução

Use os exemplos completos de [Queries para apoiar detecções](../queries-para-deteccoes.md) e o [contrato de schemas](../campos-e-schemas.md).

| Percurso | O que registrar |
| --- | --- |
| KQL | Tabela real ou datatable sintético; filtros, colunas e operadores usados |
| SPL | Índice/source, aliases validados, tempo, stats/streamstats quando necessário |
| AQL | Propriedades DSM, unidade de eventcount e intervalo; sequência validada separadamente |
| Wazuh/indexer | Índice/mapping, corpo DSL, relógio e completude dos documentos/buckets |
| Offline | Seleção dos IDs, cálculo e raciocínio, sem afirmar execução nos produtos |

## Limitações

Query testada não cria alerta nem regra madura. Agendamento, atraso e deduplicação ainda exigem implementação.

## Entrega e próximo passo

Preencha pergunta, campos, janela, consulta ou raciocínio, resultado esperado, resultado obtido e diferenças. Registre qual plataforma foi executada. Inclua hipótese alternativa e próximo teste. Avance pelo link ao final.

## Checkpoint

**O que precisa acompanhar o resultado?**

<details>
<summary>Ver resposta</summary>

Fonte/schema, janela, método, evidência obtida e limitações. O resultado esperado do roteiro não substitui sua execução.

</details>

[← Tópico anterior](lab-08-threat-hunting.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-10-investigacao-multisiem.md)
