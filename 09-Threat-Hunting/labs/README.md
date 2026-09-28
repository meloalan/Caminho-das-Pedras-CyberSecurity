# Laboratórios de Threat Hunting

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](../referencias.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](dados/README.md)

## Percurso

Onze labs progressivos e um laboratório final. Comece sem SIEM; depois escolha uma plataforma se quiser praticar ingestão e pesquisa. Os [dados](dados/README.md) são sintéticos e têm limitações intencionais. A trilha anterior ensinou consulta; aqui cada consulta serve a uma pergunta investigativa.

| Lab | Entrega |
| --- | --- |
| [1: Escrevendo hipóteses sem SIEM](lab-01-escrevendo-hipoteses.md) | Hunt Plan com sete elementos: hipótese, alternativa, dados, sustentação, enfraquecimento, escopo e saída. |
| [2: Validando telemetria antes de procurar](lab-02-validando-telemetria.md) | Matriz de cobertura com fonte, campo, período, controle positivo e efeito da lacuna. |
| [3: Falhas, sucesso e hipóteses concorrentes](lab-03-authentication-hunt.md) | Tabela de seleção, chave de correlação e duas conclusões: sequência observada; intenção inconclusiva. |
| [4: Conta criada e atividade posterior](lab-04-account-hunt.md) | Mapa de identidade e linha do tempo com dependência explícita do inventário. |
| [5: Processos e relação parent-child](lab-05-process-hunt.md) | Matriz de execuções priorizadas com evidência, alternativa e próximo pivot. |
| [6: Da conta ao grafo de entidades](lab-06-pivoting.md) | Grafo com rótulos de relação, IDs e uma lista de associações recusadas. |
| [7: Baseline e raridade sem veredito automático](lab-07-baseline-rarity.md) | Ranking justificado, baseline versionada, denominador e limitações. |
| [8: Do IOC ao comportamento](lab-08-ioc-to-behavior.md) | Ficha IOC, mapa de pivots e conclusão limitada, sem consulta a serviços externos. |
| [9: Timeline com dados embaralhados](lab-09-timeline.md) | Timeline com fatos, relações, limites e eventos excluídos por escopo. |
| [10: Uma pergunta em quatro contratos](lab-10-multisiem-hunt.md) | Matriz de tradução, resultado esperado e campo separado para resultado obtido. |
| [11: Transferindo o achado para engenharia](lab-11-hunt-to-detection.md) | Parte preenchida do template de detecção, matriz de teste e pacote de evidências do hunt. |
| [Final: Laboratório final: investigação e relatório](lab-final-investigacao-completa.md) | Sete artefatos de portfólio: plano, journal, timeline, mapa de pivots, IOC to Behavior, relatório e candidata/justificativa de não automatizar. |

## Como avaliar

Confira hipótese testável, cobertura, escopo, chaves, alternativas e conclusão. Uma resposta inconclusiva bem sustentada é melhor que uma acusação sem evidência. As soluções comentadas ficam recolhidas para permitir tentativa independente.

## Ambiente e resultado

Editor de texto e leitura de JSON/CSV bastam. Python é opcional para conferir o conjunto anterior. Nenhum lab precisa de logs reais, malware, exploração ou credential dumping. Resultados esperados são referências didáticas; documente separadamente seus resultados obtidos.

## Portfólio

Reúna Hunt Plan, Journal, timeline, mapa de pivots, IOC to Behavior, relatório e transferência para detecção. Preserve a declaração de dados fictícios e os limites; não use esses artefatos como comprovação de atendimento de um incidente real.

## Checkpoint

**Preciso instalar quatro SIEMs para concluir o módulo?**

<details>
<summary>Ver resposta</summary>

Não. O lab multisiem compara contratos e permite escolher uma plataforma. A análise offline deve ser declarada como tal, sem simular execução em produtos.

</details>

[← Tópico anterior](../referencias.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](dados/README.md)
