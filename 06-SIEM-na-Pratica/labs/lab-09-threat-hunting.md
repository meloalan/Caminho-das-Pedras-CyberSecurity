# Lab 09: Threat hunting e raridade

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-08-investigation.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](../../07-KQL/README.md)

> Pergunta: o que posso descobrir sem começar por um alerta?

## Objetivo e pré-requisitos

Executar um hunt pequeno baseado em hipótese. Leia [hunting](../threat-hunting.md) e use o conjunto completo, sem top N ocultando registros. O tamanho reduzido permite conferir cada contagem manualmente.

## Execução

1. Escreva a hipótese: “há combinações de autoridade, usuário e host pouco frequentes nas falhas do conjunto?”.
2. Selecione apenas 4625 do provider Security.
3. Agrupe por target_domain, target_user e host.
4. Considere raro, somente para o exercício, um grupo com uma observação.
5. Compare com agrupamento só por nome e mostre a perda de semântica.
6. Escolha um grupo e faça um pivô por origem ou contexto de conta de serviço.
7. Declare se o dado permite classificar a atividade e proponha melhoria de cobertura.

## Resultado esperado

Três grupos: LAB/lab-user/WIN-LAB01 com três falhas, OUTRO-LAB/lab-user/WIN-LAB01 com uma e LAB/svc-lab/WIN-LAB02 com uma. Os dois grupos de uma observação são raros nesse dataset, sem conclusão sobre malícia.

## Quatro plataformas

Splunk: stats por três campos e filtro de contagem. QRadar: GROUP BY propriedades e HAVING, respeitando eventcount. Sentinel: summarize por domínio/usuário/host e filtro. Wazuh: conjunto completo paginado ou composite conforme mapping, sem usar top buckets como inventário exato. Use a Roseta para sintaxe e limites.

## Entrega

Hipótese, população, query/intenção, grupos, pivô, resultado e conclusão. Proponha uma detecção apenas se houver comportamento, fonte sustentável e testes. Caso contrário, documente o hunt como investigação pontual.

## Encerramento

Revise seu checklist individual e descreva três conceitos que transferiria para um SIEM desconhecido. O próximo módulo aprofunda KQL; ele não substitui SPL, AQL ou a API do indexer, mas reforça filtros, agregação e correlação.

## Resultado obtido

Preencha após sua execução: percurso, versão quando aplicável, evidência, divergências e limitações. Não marque configuração de produto como validada com base apenas na análise offline.

## Checkpoint

**Qual evidência sustenta sua entrega?**

<details>
<summary>Ver resposta</summary>

Registre fonte, janela, consulta ou cálculo, resultado e limite. Uma descrição do que deveria ocorrer não substitui resultado obtido.

</details>

[← Tópico anterior](lab-08-investigation.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](../../07-KQL/README.md)
