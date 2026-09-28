# Métricas que explicam o trabalho

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](hunt-to-detection.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](TEMPLATE-HUNT.md)

## Contagem com significado

| Métrica | Definição e denominador | Limite |
| --- | --- | --- |
| Hunts concluídos | Encerrados no período, com critério de saída | Quantidade não mede profundidade |
| Proporção inconclusiva | Hipóteses inconclusivas / hipóteses encerradas na coorte | Pode refletir descoberta útil de lacunas |
| Cobertura avaliada | Ativos com fonte/campos testados / ativos elegíveis esperados | Disponibilidade não é cobertura de todas as técnicas |
| Telemetry gaps | Lacunas únicas por fonte, campo e população | Evitar contar a mesma lacuna por query |
| Detection gaps | Manifestações não cobertas com evidência | Ausência de alerta não basta |
| Candidatas aceitas | Candidatas aceitas pela engenharia / candidatas revisadas | Aceita não significa implantada |
| Detecções melhoradas | Mudanças validadas com teste comparativo | Não só regras editadas |
| Findings relevantes | Achados que produziram decisão justificada | Definir relevância antes da contagem |
| Tempo gasto | Esforço por etapa ou pergunta | Não transformar velocidade em meta cega |

## Exemplo fictício

Em dez hipóteses encerradas, três inconclusivas representam 3/10 = 30%. Se oito candidatas foram propostas, quatro revisadas e duas aceitas, a aceitação entre revisadas é 2/4 = 50%; quatro ainda aguardam decisão. Dizer 2/8 sem explicar a coorte mistura pendência com rejeição.

## Incidentes não são a única medida

Medir só incidentes encontrados incentiva exagero de conclusões e evita hunts difíceis com baixa cobertura. Confirmar uma lacuna ou verificar uma detecção existente também tem valor. Para dizer que a detecção cobre adequadamente uma manifestação, exija um teste daquela manifestação no escopo, não apenas a existência da regra.

## Uso na melhoria

Compare coortes e períodos de cobertura semelhante. Registre mudanças de equipe, infraestrutura, retenção e objetivo. Combine números com exemplos de decisões, limitações e ações concluídas. Sem denominador confiável, apresente contagem e explique o limite.

## Checkpoint

**Uma taxa alta de inconclusivos significa hunting ruim?**

<details>
<summary>Ver resposta</summary>

Não necessariamente. Pode mostrar lacunas reais de dados ou perguntas difíceis. Examine causas e melhorias encaminhadas antes de avaliar qualidade.

</details>

[← Tópico anterior](hunt-to-detection.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](TEMPLATE-HUNT.md)
