# Lab 06: Processos, pais e comandos

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-05-correlacao-temporal.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-07-pivot.md)

## Objetivo

Comparar duas execuções sem chamar PowerShell de malicioso.

## Cenário

Uma sessão interativa e uma tarefa usam o mesmo executável.

## Dados

E06, E12 e E13; H01 é referência histórica curta. Todos os nomes, hosts, horários e endereços são fictícios. Dia atual do exercício: 24/09/2026 UTC.

[Dataset e tipos](dados/README.md) · [Eventos JSONL](dados/eventos.jsonl) · [Inventário](dados/inventario.csv).

## Perguntas

1. Quais são parent, child, comando, usuário, host e horário?
2. Por que E06 pode permanecer aberto?
3. E12 e E13 representam necessariamente duas execuções?
4. PID pode ligar eventos de hosts distintos?

## Dicas

Compare Sysmon 1 com 4688, preserve provider e confira ProcessGuid quando disponível.

## Solução comentada

<details>
<summary>Ver solução depois de pensar</summary>

E06: explorer → powershell, alan.lab, WIN-LAB01, 08:08, -NoExit. E12: taskeng → powershell, svc.lab, WIN-LAB02, 09:00, Get-Date. E13 é observação 4688 da mesma criação descrita em E12. São dois Sysmon ProcessCreate atuais, não três execuções inferidas por soma das fontes. O pai e o comando orientam perguntas sobre finalidade e autorização.

</details>

## Tradução e execução

Use os exemplos completos de [Strings, caminhos e regex com contexto](../strings-e-regex.md) e o [contrato de schemas](../campos-e-schemas.md).

| Percurso | O que registrar |
| --- | --- |
| KQL | Tabela real ou datatable sintético; filtros, colunas e operadores usados |
| SPL | Índice/source, aliases validados, tempo, stats/streamstats quando necessário |
| AQL | Propriedades DSM, unidade de eventcount e intervalo; sequência validada separadamente |
| Wazuh/indexer | Índice/mapping, corpo DSL, relógio e completude dos documentos/buckets |
| Offline | Seleção dos IDs, cálculo e raciocínio, sem afirmar execução nos produtos |

## Limitações

Não há hashes no fixture. PID pode ser reutilizado. A ausência de campo não autoriza inventar valor.

## Entrega e próximo passo

Preencha pergunta, campos, janela, consulta ou raciocínio, resultado esperado, resultado obtido e diferenças. Registre qual plataforma foi executada. Inclua hipótese alternativa e próximo teste. Avance pelo link ao final.

## Checkpoint

**O que precisa acompanhar o resultado?**

<details>
<summary>Ver resposta</summary>

Fonte/schema, janela, método, evidência obtida e limitações. O resultado esperado do roteiro não substitui sua execução.

</details>

[← Tópico anterior](lab-05-correlacao-temporal.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-07-pivot.md)
