# Procedures

[← Índice do módulo](README.md) · [Técnicas](techniques.md) · [Grupos, software e campanhas](software-groups-campaigns.md) · [Modelo de dados](attack-data-model.md)

## Do comportamento geral à instância observada

Uma técnica nomeia uma categoria comportamental. Um procedure descreve como um grupo, software ou campanha foi observado realizando aquele comportamento, conforme documentado em fontes e relações do ATT&CK.

```text
Técnica: Create Account
Subtécnica possível: Local Account, Domain Account ou Cloud Account
Procedure: uma implementação concreta atribuída numa fonte e contexto documentados
```

Não invente procedures a partir de um exemplo didático. Não inclua instruções operacionais para criar persistência. Descreva a ação em nível observável e defensivo, cite a fonte e marque claramente qualquer cenário fictício.

## Observação e procedure não são a mesma coisa

Um alerta local pode mostrar que uma conta foi criada por uma identidade específica. Essa observação é evidência do ambiente em análise. Ela não é automaticamente um procedure já registrado pelo ATT&CK. Um procedure publicado na base é conhecimento contextualizado que pode ser associado a grupo, software ou campanha. Uma observação local deve ser analisada independentemente e só pode apoiar atribuição mediante outras evidências.

| Camada | Exemplo de pergunta |
| --- | --- |
| Observação | O que o evento, processo ou API mostra neste ambiente? |
| Comportamento | Que ação genérica essa evidência sustenta? |
| Técnica ou subtécnica | Qual objeto atual descreve melhor a ação? |
| Procedure documentado | Há uma implementação específica descrita em fonte confiável? |
| Atribuição | Que conjunto independente de evidências liga a atividade a um ator? |

Cada passo é uma inferência adicional. Não pule da técnica para a identidade do adversário.

## Descrever um procedure de modo responsável

Registre fonte primária quando disponível, data e contexto, comportamento observado, plataforma, objetos associados, confiança da fonte e as incertezas. Distinga o que o relatório afirma do que a equipe inferiu. A confiança não deve ser apresentada como escala oficial do ATT&CK se for uma convenção da equipe.

## Exercício

Um relatório público descreve criação de uma conta durante uma intrusão, sem identificar o escopo do diretório. Separe em três notas: comportamento relatado, subtécnica ainda não sustentada e atribuição ainda não sustentada. Explique qual evidência independente resolveria cada lacuna.
