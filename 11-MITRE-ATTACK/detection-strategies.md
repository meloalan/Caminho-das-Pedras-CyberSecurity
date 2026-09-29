# Detection Strategies, Analytics e Data Components

[← Índice do módulo](README.md) · [Telemetria](attack-to-telemetry.md) · [Mapeamento](detection-mapping.md) · [Cobertura](detection-coverage.md)

## Modelo defensivo atual

No ATT&CK atual, Detection Strategies descrevem abordagens para detectar comportamento, Analytics descrevem lógica analítica mais concreta e orientada a plataforma, e Data Components descrevem tipos de informação observável relevantes. Esses objetos orientam o trabalho. A implementação ainda depende do produto, dos dados e dos testes no ambiente.

| Objeto | Pergunta que ajuda a responder | O que não garante |
| --- | --- | --- |
| Detection Strategy | Que abordagem pode revelar o comportamento? | Cobertura já implantada ou eficaz. |
| Analytic | Que lógica específica pode detectar uma manifestação? | Portabilidade sem adaptação entre plataformas ou esquemas. |
| Data Component | Que informação de evento interessa à detecção? | Coleta, retenção, completude ou normalização na organização. |

Consulte as páginas oficiais de [Detection Strategies](https://attack.mitre.org/detectionstrategies/), [Analytics](https://attack.mitre.org/analytics/) e [Data Components](https://attack.mitre.org/datacomponents/) para ver objetos e relações vigentes. Analytics podem ser específicos a uma plataforma e documentados como implementação de uma estratégia.

## Exemplo atual: criação de conta

Para `T1136`, o conteúdo atual contém estratégias e analytics associados a criação de conta e subtécnicas. Por exemplo, [DET0003](https://attack.mitre.org/detectionstrategies/DET0003/) está ligado à criação de conta de domínio e referencia evidência relevante como User Account Creation e Process Creation em seus analytics. Isso não significa que Event ID 4720 sozinho cubra todo o comportamento, nem que essa lógica seja universal para outros ambientes.

O mapeamento útil liga objeto ATT&CK a fonte concreta:

```text
Strategy relevante
  → analytic aplicável à plataforma
    → Data Components e propriedades exigidas
      → fonte real, configuração, ingestão e retenção
        → lógica local testada e limitações registradas
```

## Migração de Data Sources legados

Data Sources foram depreciados na versão 18. Histórico e relatórios antigos podem continuar a referenciá-los. Para trabalho atual, siga a relação técnica com Detection Strategy, Analytics, Data Components e seus log sources embutidos. Não reescreva referências históricas como se nunca tivessem existido; indique a versão e o estado legado. A fonte oficial [Data Sources](https://attack.mitre.org/datasources/) documenta a depreciação.

## Da estratégia à regra local

Ao adaptar um analytic, documente pré-requisitos, plataforma, esquema esperado, campos, normalização, limiares, exceções, casos negativos, validação e limitações. Preserve referência ATT&CK e versão, mas marque separadamente qualquer adaptação. Uma implementação local não passa a ser oficial por ter o mesmo ID na descrição.

## Exercício

Encontre uma estratégia ligada a uma técnica do laboratório. Compare um analytic associado, os Data Components necessários e sua telemetria local. Escreva quais condições do analytic são reproduzíveis e quais não são. Se a fonte estiver ausente, registre um Telemetry Gap, não uma regra supostamente ineficaz.
