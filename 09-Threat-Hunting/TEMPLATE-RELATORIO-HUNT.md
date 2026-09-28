# Template de relatório final

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](TEMPLATE-HUNT.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](exemplo-hunt-completo.md)

## Resumo executivo

Descreva pergunta, população, principal observação, limite e decisão em um parágrafo. Exemplo de tom: “Identificamos uma sequência que merece análise adicional, mas os dados não permitem confirmar uso indevido”. Evite “ataque avançado” quando só há processo incomum.

## Hipótese e escopo

Registre Hunt ID, versão, autor/revisor, motivação, proposição, alternativas, janela UTC, população e condição de encerramento. **A preencher.**

## Fontes de dados e cobertura

Liste fontes esperadas e observadas, controle positivo, retenção, campos e lacunas. Delimite quais ativos não permitem conclusão. **A preencher.**

## Metodologia e achados

Anexe versões das consultas, iterações, filtros e pivots. Separe achado de hipótese. Não omita consultas negativas relevantes. **A preencher.**

## Timeline e evidências

| UTC | ID / fonte | Observação | Relação sustentada | Limite |
| --- | --- | --- | --- | --- |
| A preencher | A preencher | A preencher | A preencher | A preencher |

## Explicações alternativas

Explique o que foi confrontado: mudança autorizada, aplicação, automação, erro de usuário ou outras hipóteses. A aprovação deve corresponder à identidade, ativo, atividade e janela. **A preencher.**

## Limitações e conclusão

Indique o que foi observado, o que não foi observado e o que não poderia ser observado. Declare grau de sustentação da hipótese e por quê. Não generalize do escopo para todo o ambiente. **A preencher.**

## Detection gaps e telemetry gaps

Separe ausência de dados de ausência de lógica. Anexe evidências e critérios para testar a melhoria. **A preencher.**

## Recomendações e outcome

| Ação | Responsável | Prioridade justificada | Prazo acordado | Evidência de aceite |
| --- | --- | --- | --- | --- |
| A preencher | A definir | A justificar | A acordar | Pendente |

Finalize com status de execução, revisão e condição de reabertura. Encaminhe somente as ações autorizadas; o template não executa respostas.

## Checkpoint

**Qual é o erro de escrever “não há ameaça” no resumo?**

<details>
<summary>Ver resposta</summary>

Generaliza além das fontes, da população e do período avaliados. A conclusão deve declarar exatamente o que a evidência permite afirmar.

</details>

[← Tópico anterior](TEMPLATE-HUNT.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](exemplo-hunt-completo.md)
