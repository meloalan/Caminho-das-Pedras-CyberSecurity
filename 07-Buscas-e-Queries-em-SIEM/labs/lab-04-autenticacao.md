# Lab 04: Investigar falhas e autenticação aceita

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-03-agregacoes.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-05-correlacao-temporal.md)

## Objetivo

Formular hipóteses concorrentes para uma sequência.

## Cenário

Três falhas antecedem um sucesso RemoteInteractive. O objetivo é investigar, sem rotular brute force.

## Dados

E01/E02/E03/E04, com E10/E11 como controles. Todos os nomes, hosts, horários e endereços são fictícios. Dia atual do exercício: 24/09/2026 UTC.

[Dataset e tipos](dados/README.md) · [Eventos JSONL](dados/eventos.jsonl) · [Inventário](dados/inventario.csv).

## Perguntas

1. A chave de conta+autoridade+host+origem+tipo coincide?
2. O sucesso é posterior?
3. Quais explicações legítimas e não autorizadas continuam possíveis?
4. O fixture informa MFA, VPN e aprovação?

## Dicas

Não herde LogonId do sucesso para falhas. Confira o domínio de E10.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

Há três falhas de LAB/alan.lab, WIN-LAB01, 192.0.2.10, LogonType 10, antes do sucesso às 08:05. E10 diverge na autoridade e E11 diverge em vários campos. O padrão é compatível com hipóteses distintas; faltam MFA/VPN, autorização e contexto do titular.

</details>

## Tradução e execução

Use os exemplos completos de [Join não é sinônimo de correlação](../correlacao-e-joins.md) e o [contrato de schemas](../campos-e-schemas.md).

| Percurso | O que registrar |
| --- | --- |
| KQL | Tabela real ou datatable sintético; filtros, colunas e operadores usados |
| SPL | Índice/source, aliases validados, tempo, stats/streamstats quando necessário |
| AQL | Propriedades DSM, unidade de eventcount e intervalo; sequência validada separadamente |
| Wazuh/indexer | Índice/mapping, corpo DSL, relógio e completude dos documentos/buckets |
| Offline | Seleção dos IDs, cálculo e raciocínio, sem afirmar execução nos produtos |

## Limitações

A sequência não comprova causa, invasão ou intenção. Logs adicionais podem mudar a avaliação.

## Entrega e próximo passo

Preencha pergunta, campos, janela, consulta ou raciocínio, resultado esperado, resultado obtido e diferenças. Registre qual plataforma foi executada. Inclua hipótese alternativa e próximo teste. Avance pelo link ao final.

## Checkpoint

**O que precisa acompanhar o resultado?**

<details>
<summary>Ver resposta</summary>

Fonte/schema, janela, método, evidência obtida e limitações. O resultado esperado do roteiro não substitui sua execução.

</details>

[← Tópico anterior](lab-03-agregacoes.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-05-correlacao-temporal.md)
