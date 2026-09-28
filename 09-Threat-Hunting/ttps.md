# Táticas, técnicas, procedimentos e custo de mudança

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](iocs.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](behavior-based-hunting.md)

## Vocabulário para formular perguntas

| Conceito | Significado | Cuidado |
| --- | --- | --- |
| Tática | Objetivo adversário | Não é um produto nem uma fase inevitável |
| Técnica | Como um objetivo pode ser alcançado | Depende de contexto para mapear |
| Subtécnica | Forma mais específica de uma técnica | Use somente quando sustentada |
| Procedimento | Implementação concreta observada | Não confundir exemplo com requisito universal |

Criar uma conta pode ser feito por interface, PowerShell, net user ou API. O comportamento é criação de identidade, mas o mapeamento adversário depende da finalidade e do contexto. Uma criação administrativa legítima não vira persistência porque recebeu uma tag.

PowerShell pode implementar T1059.001 quando usado no contexto adversário descrito pelo ATT&CK. Sua presença isolada apenas informa ferramenta/execução. Veja [mapeamento aplicado](hunting-with-attack.md).

## Pyramid of Pain

O modelo de David Bianco organiza hashes, IPs, domínios, artefatos de rede/host, ferramentas e TTPs para discutir o esforço do adversário ao mudar o que é observado. A [referência do autor publicada pela SANS](https://www.sans.org/tools/the-pyramid-of-pain) apresenta esse modelo conceitual.

Não é uma lei universal nem uma escala automática de confiança. Um hash preciso pode ser muito útil; uma hipótese comportamental vaga pode produzir ruído. Observar TTPs pode exigir mais telemetria, análise e manutenção. Diferentes adversários têm custos diferentes para trocar infraestrutura ou procedimento.

## Aplicação

Comece com um indicador, identifique a execução ou relação observada e formule uma hipótese que sobreviva à troca daquele valor. Pergunte quais evidências distinguem o comportamento de uma atividade legítima. Documente limites; não descarte IOCs só porque ficam em outra região da pirâmide.

## Checkpoint

**Um nome de ferramenta define uma técnica?**

<details>
<summary>Ver resposta</summary>

Não. A técnica descreve comportamento com contexto. Uma ferramenta pode implementar vários comportamentos, legítimos ou indevidos.

</details>

[← Tópico anterior](iocs.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](behavior-based-hunting.md)
