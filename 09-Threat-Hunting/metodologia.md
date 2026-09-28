# Metodologia: uma pergunta por vez

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](README.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](hipoteses.md)

## Da motivação à decisão

Um hunt pode nascer de inteligência, incidente anterior, vulnerabilidade, mudança de infraestrutura, pesquisa interna, comportamento emergente ou lacuna de detecção. A motivação não confirma a hipótese. Uma vulnerabilidade divulgada, por exemplo, não demonstra exploração em um ativo local.

| Etapa | Decisão e artefato |
| --- | --- |
| 1. Contexto | Que risco justifica o esforço? Registrar origem e relevância local |
| 2. Hipótese | Que comportamento esperamos observar e o que o enfraqueceria? |
| 3. Escopo | População, contas, hosts, período, fontes e condição de saída |
| 4. Telemetria | Fonte e campos capazes de responder à pergunta |
| 5. Cobertura | Conferir inventário, retenção, parsing, perdas e teste positivo |
| 6. Consulta | Uma pergunta concreta, versão, filtros e limites de exportação |
| 7. Análise | Separar observação, inferência e lacuna |
| 8. Pivot | Próxima entidade, chave, fonte e janela justificadas |
| 9. Evidências concorrentes | Procurar mudança aprovada, aplicação ou explicação alternativa |
| 10. Conclusão | Sustentada, enfraquecida, refutada ou inconclusiva no escopo |
| 11. Outcome | Investigação, detecção, tuning, coleta, documentação ou nenhuma ação adicional |

## Consulta progressiva

Comece encontrando contas com falhas, examine sucessos correspondentes, delimite sessões, procure processos e só depois conexões. Uma megaquery pode ocultar nulos, perdas de join e cardinalidade. Guarde também a saída anterior a cada filtro: uma exclusão ampla pode remover o próprio comportamento procurado.

No caso E01 a E08 do [dataset](labs/dados/README.md), a primeira pergunta é sobre autenticação. O processo encontrado produz outra pergunta: a execução é compatível com a administração esperada? Não transforme proximidade temporal em prova de execução remota.

## Condição de encerramento

Encerrar significa ter respondido à pergunta para população X, período Y e fontes Z, ou ter documentado por que isso não foi possível. Timebox é um limite negociado de esforço, não uma quantidade universal de horas. Se um novo ativo ampliar o escopo, registre a decisão, autorização e custo antes de continuar.

## Hunt Plan e detection runbook

Um Hunt Plan começa numa hipótese e define como procurar evidência. Um [runbook de detecção](../08-Detection-Engineering/runbooks.md) começa num alerta e define como analisá-lo. Ambos precisam de contexto, mas têm gatilhos e condições de saída diferentes.

Prática: antes de abrir qualquer ferramenta, preencha hipótese, alternativa, fontes e saída no [template](TEMPLATE-HUNT.md). Se a query não responder à pergunta escrita, ajuste a pergunta ou a consulta e registre a versão.

## Checkpoint

**Quando voltar à hipótese em vez de continuar filtrando?**

<details>
<summary>Ver resposta</summary>

Quando os resultados contradizem a previsão ou a fonte não observa o comportamento. Continuar filtrando para obter a resposta desejada introduz viés.

</details>

[← Tópico anterior](README.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](hipoteses.md)
