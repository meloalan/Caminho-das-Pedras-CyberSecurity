# Template de Hunt Plan e Notebook

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](hunting-metrics.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](TEMPLATE-RELATORIO-HUNT.md)

## Como usar

Copie este arquivo para seu portfólio de dados fictícios. Preencha os campos abaixo e mantenha pendente o que ainda não executou. Consulte o [exemplo preenchido](exemplo-hunt-completo.md).

## 1. Identificação

Hunt ID, título, autor, data, versão, status de execução e revisor. Não confundir status com conclusão.

**Registro:** a preencher.

## 2. Motivação

Risco, origem da demanda e relevância para os ativos. Referência de inteligência quando aplicável.

**Registro:** a preencher.

## 3. Hipótese

Proposição testável, comportamento esperado, evidência que sustentaria e evidência que enfraqueceria/refutaria.

**Registro:** a preencher.

## 4. Hipóteses alternativas

Administração, aplicação, automação e outras explicações. Qual dado diferencia cada uma?

**Registro:** a preencher.

## 5. Escopo e timebox

Período com fuso e limites inclusivo/exclusivo, população, hosts, contas, fontes, tempo de análise e condição de encerramento.

**Registro:** a preencher.

## 6. Fontes e cobertura

Inventário esperado/observado, retenção, configuração, parsing, perdas, controles positivos, permissões e exportação.

**Registro:** a preencher.

## 7. Campos necessários

Campo nativo e normalizado, tipo, papel, chave de correlação, campos ausentes e efeito sobre a hipótese.

**Registro:** a preencher.

## 8. Queries

Objetivo, query/arquivo e versão, dataset, período, filtros, limites e resultado realmente obtido. Não marcar execução não realizada.

**Registro:** a preencher.

## 9. Resultados e pivots

Observações e IDs; próxima pergunta, entidade, fonte, chave, janela e relação confirmada ou apenas possível.

**Registro:** a preencher.

## 10. Timeline

UTC, fonte, ID, quem, onde, origem/destino, processo e relação. Manter cadeias separadas quando faltar evidência.

**Registro:** a preencher.

## 11. Evidências, observações e inferências

Separar fatos de interpretação. Preservar original, local da cópia e digest quando calculado; registrar transformações.

**Registro:** a preencher.

## 12. Limitações

Telemetria ausente, campos nulos, período curto, coalescência, duplicatas, latência, vieses e perguntas sem resposta.

**Registro:** a preencher.

## 13. Conclusão

Sustentada, parcialmente sustentada, enfraquecida, refutada no escopo ou inconclusiva. Justificar sem exceder as evidências.

**Registro:** a preencher.

## 14. Outcome

Investigação/IR, candidata, tuning, coleta, documentação, nova hipótese ou nenhuma ação adicional. Responsável e aceite.

**Registro:** a preencher.

## 15. Detection Gap e Telemetry Gap

Distinguir lógica ausente de dado ausente. Evidência, impacto, owner e teste de resolução.

**Registro:** a preencher.

## 16. Próximos passos

Ação, responsável, prazo acordado e critério de aceite. Registrar revisão e condição de reabertura.

**Registro:** a preencher.

## Matriz de hipóteses

| Explicação | Evidência a favor | Evidência que enfraquece | Dado faltante | Decisão |
| --- | --- | --- | --- | --- |
| Hipótese principal | A preencher | A preencher | A preencher | Pendente |
| Alternativa legítima | A preencher | A preencher | A preencher | Pendente |

## Registro de consulta e pivot

| Versão / pergunta | Fonte e janela | Query / filtros | IDs / resultado obtido | Chave e próximo passo |
| --- | --- | --- | --- | --- |
| A preencher | A preencher | A preencher | Não executado | A preencher |

## Checkpoint

**Por que deixar resultado obtido como não executado?**

<details>
<summary>Ver resposta</summary>

Para separar roteiro e expectativa de evidência produzida. Uma consulta escrita não comprova execução, cobertura nem resultado.

</details>

[← Tópico anterior](hunting-metrics.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](TEMPLATE-RELATORIO-HUNT.md)
