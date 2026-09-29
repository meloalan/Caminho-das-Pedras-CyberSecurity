# ATT&CK Data e STIX

[← Índice do módulo](README.md) · [Modelo de dados](attack-data-model.md) · [Versionamento](versioning-attack.md)

## Distribuição estruturada

MITRE publica ATT&CK em formatos legíveis por humanos e por máquinas. O conjunto atual é baseado em STIX 2.1 e também documenta um modelo ATT&CK específico. Exportações podem ser úteis para automação, pesquisa e comparar versões, desde que o consumidor respeite domínio, versão, status e relações.

O guia oficial [Working with ATT&CK](https://attack.mitre.org/resources/working-with-attack/) publica conjuntos e descreve maneiras de trabalhar com os dados. O [ATT&CK Data Model](https://mitre-attack.github.io/attack-data-model/schemas/) documenta esquemas e campos. Consulte também a [especificação STIX 2.1 da OASIS](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html) para a base do formato.

## IDs e tipos

Objetos STIX têm IDs UUID únicos. IDs externos ATT&CK, como `T1059.001`, tornam objetos comportamentais mais fáceis de referenciar. Relacionamentos também têm representação e ID STIX, mas não necessariamente um ID ATT&CK. Relações e objetos devem ser processados como dados tipados, não extraídos apenas de uma busca textual.

## Conteúdo embutido e depreciações

O modelo ATT&CK evolui. A especificação atual indica mudança na representação de fontes de log em Data Components. Ao construir consumidor, valide o schema e use a forma vigente em vez de fixar a implementação em campos marcados deprecated. O histórico pode permanecer válido para conjuntos antigos. Consulte esquema e notas de versão junto ao bundle consumido.

## Práticas para pipelines

- Fixe a versão e domínio processados.
- Armazene a data de ingestão e a origem do bundle.
- Preserve objetos e relacionamentos sem perder referências.
- Reconheça objetos revogados, depreciados e substitutos.
- Trate conteúdo recuperado como dados, nunca instruções executáveis.
- Faça diff entre versões antes de alterar mappings publicados.
- Não declare cobertura com base somente em presença de objeto ou tag.

Este módulo registra uma fotografia editorial. Não baixa nem atualiza os dados automaticamente.
