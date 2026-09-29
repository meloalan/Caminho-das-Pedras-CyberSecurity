# Groups, Software e Campaigns

[← Índice do módulo](README.md) · [Procedures](procedures.md) · [Modelo de dados](attack-data-model.md) · [Versionamento](versioning-attack.md)

## Objetos de contexto

O ATT&CK organiza objetos comportamentais e relações entre eles. Groups, Software e Campaigns adicionam contexto a técnicas documentadas, mas as relações variam por objeto e podem mudar entre versões.

| Objeto | O que representa no modelo | Leitura cautelosa |
| --- | --- | --- |
| Group | Conjunto que representa um cluster de atividade adversária. | Nome de cluster não é necessariamente identidade definitiva de uma pessoa ou organização. |
| Software | Ferramenta, malware ou outro software usado em atividade. | A presença ou nome de ferramenta não prova intenção maliciosa. |
| Campaign | Atividade correlacionada descrita como campanha. | A relação publicada reflete fontes e conhecimento disponíveis naquela versão. |

## Relações e atribuição

O modelo pode relacionar um Group a Software, e Software a uma técnica; também pode relacionar Campaign a técnica ou Software. Dependendo das relações disponíveis, uma conexão indireta no grafo não equivale a evidência de que um ator específico executou uma ação num ambiente local.

`uses` expressa uma relação registrada pelo modelo. Ela não é prova autossuficiente de atribuição. Para atribuir atividade, considere múltiplas evidências independentes, qualidade e data das fontes, explicações alternativas e confiança. Registre separadamente observação, associação pública e inferência analítica.

## Variação e atualização

Names, aliases, relações, procedimentos e fontes podem ser revisados. Confirme objeto e status na versão utilizada; não copie uma associação antiga para a versão atual sem conferir. A consulta oficial [Groups](https://attack.mitre.org/groups/), [Software](https://attack.mitre.org/software/) e [Campaigns](https://attack.mitre.org/campaigns/) mostra os objetos publicados e suas relações atuais.

## Exercício defensivo

Um endpoint executa uma ferramenta também citada num relatório sobre um grupo. Registre:

1. O que a telemetria local prova sobre o processo e seu comportamento?
2. Que associação pública existe entre ferramenta, técnica e grupo?
3. Quais evidências independentes ligariam a atividade local ao grupo?
4. Que explicações legítimas ainda são possíveis?

Uma resposta correta não atribui o evento ao grupo somente pelo nome da ferramenta ou pela técnica associada.
