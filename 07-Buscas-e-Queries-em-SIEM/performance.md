# Performance: medir custo sem mudar a pergunta

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](queries-para-deteccoes.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](troubleshooting-queries.md)

## Eficiência precisa preservar a resposta

Reduzir período, fonte e campos pode ajudar, mas também excluir evidências. Comece pelo menor escopo que responde à pergunta e amplie com motivo. Não existe uma regra física universal de otimização para todos os mecanismos.

| Decisão | Por que pode ajudar | O que medir |
| --- | --- | --- |
| Janela menor | Menos dados candidatos | Duração e eventos tardios excluídos |
| Dataset correto | Evita índices/tabelas irrelevantes | Cobertura por fonte |
| Filtro seletivo | Reduz população antes de operações caras | Contagem antes/depois |
| Menos campos | Reduz transporte/memória em certas etapas | Tamanho e chaves preservadas |
| Agregação apropriada | Resume o resultado necessário | Cardinalidade de grupos |
| Join limitado | Evita explosão many to many | Linhas e chaves dos dois lados |
| Regex controlada | Evita varreduras desnecessárias | Padrão, tempo e falsos matches |

## Diferenças entre mecanismos

KQL possui otimizador e recomendações próprias; filtros temporais e de string seletivos precisam respeitar tipo/índices. SPL pode truncar sort/subsearch/join ou atingir memória. AQL depende de armazenamento, propriedades extraídas/indexadas e distribuição dos dados. No OpenSearch/indexer, muitos shards, alta cardinalidade e buckets podem aumentar custo; terms.size não é limite do número de eventos examinados.

Shards e partições distribuem dados e trabalho. Não aumente sua quantidade como solução automática: cada unidade tem overhead. Configuração de cluster não faz parte deste exercício; investigue com o administrador e documentação da versão.

## Um experimento comparável

1. Registre query, janela, população, tempo de execução e limites reportados.
2. Faça uma mudança, como substituir substring por igualdade quando a intenção realmente permitir.
3. Compare resultados, incluindo diferenças e ausências.
4. Repita em condição controlada, observando cache e concorrência.
5. Aceite a otimização apenas quando a resposta necessária e a completude forem preservadas.

## Erro típico

Adicionar head 100 antes de stats pode deixar a consulta rápida e a contagem errada. Reduzir terms.size altera exibição de buckets, não resolve automaticamente custo da busca. Desabilitar controles de custo para rodar uma regex ampla também não é uma otimização.

## Referências e prática

[Boas práticas KQL](https://learn.microsoft.com/en-us/kusto/query/best-practices) e [aggregations OpenSearch](https://docs.opensearch.org/latest/aggregations/) oferecem detalhes específicos. No lab, compare contagem de todos os registros com a de uma amostra de cinco linhas; explique por que a velocidade não compensa a mudança de pergunta.

## Checkpoint

**Uma query mais rápida é necessariamente melhor?**

<details>
<summary>Ver resposta</summary>

Não. Ela precisa manter semântica, cobertura e precisão suficientes, sem esconder truncamento ou perda de contexto.

</details>

[← Tópico anterior](queries-para-deteccoes.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](troubleshooting-queries.md)
