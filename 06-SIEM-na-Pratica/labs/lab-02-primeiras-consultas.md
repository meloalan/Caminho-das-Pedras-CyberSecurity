# Lab 02: Primeiras consultas

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-01-entendendo-o-pipeline.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-03-windows-authentication.md)

> Pergunta: minha consulta seleciona o que penso que seleciona?

## Objetivo e pré-requisitos

Localizar, contar e agrupar eventos, validando campos e janela. Leia [linguagens](../query-languages.md) e a [Roseta](../traduzindo-entre-siems.md). Não avance com campo desconhecido ou tipo não conferido.

## Execução

1. Defina a população: Security 4625 no intervalo do exercício.
2. Localize uma amostra sem limitar a contagem ao número de linhas exibidas.
3. Filtre lab-user e depois acrescente autoridade e host.
4. Agrupe por usuário e por origem, anotando valores ausentes.
5. Compare a busca de últimas 24 horas com a janela absoluta do dataset.
6. Remova apenas uma condição por vez para diagnosticar resultado vazio, registrando o propósito.

## Caminhos por plataforma

Wazuh usa corpo JSON no indexer com archives e mapping conferidos. Splunk usa SPL e aliases do contrato. QRadar usa AQL com propriedades Lab previamente extraídas. Sentinel usa SecurityEvent com os campos de autenticação. Não execute queries nativas diretamente sobre o JSON didático como se fosse uma tabela nativa.

## Resultado esperado

Offline, existem cinco falhas: quatro têm target_user lab-user, mas uma pertence à autoridade OUTRO-LAB. Filtrar apenas pelo nome mistura identidades. A quinta falha é de svc-lab. Uma consulta absoluta deve incluir 2026-09-20 UTC; uma janela relativa em outra data não tem esse resultado.

## Entrega e limite

Três consultas na plataforma escolhida ou três seleções offline, com intenção, campos, tempo, resultado e explicação. Inclua uma tradução conceitual para as outras três plataformas. Critério de conclusão: explicar por que cinco, quatro e três são contagens de populações diferentes.

## Resultado obtido

Preencha após sua execução: percurso, versão quando aplicável, evidência, divergências e limitações. Não marque configuração de produto como validada com base apenas na análise offline.

## Checkpoint

**Qual evidência sustenta sua entrega?**

<details>
<summary>Ver resposta</summary>

Registre fonte, janela, consulta ou cálculo, resultado e limite. Uma descrição do que deveria ocorrer não substitui resultado obtido.

</details>

[← Tópico anterior](lab-01-entendendo-o-pipeline.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-03-windows-authentication.md)
