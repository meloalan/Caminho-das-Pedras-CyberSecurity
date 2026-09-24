# Dashboards que ajudam a operar

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](tuning.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](siem-health.md)

## Uma visualização precisa levar a uma pergunta

Dashboard não é SIEM, detecção ou investigação. Ele organiza indicadores para orientar atenção. Um número sem denominador, intervalo, população e ação pode criar confiança indevida. Uma tela bonita com “zero alertas” é inútil se o coletor está parado.

| Painel | Pergunta operacional | Ação possível |
| --- | --- | --- |
| Saúde das fontes | Quem deveria enviar e parou? | Verificar agente, fila e destino |
| Volume por fonte | O que mudou desde a referência? | Investigar filtro, duplicação ou atividade |
| Atraso | Quanto demora até ficar pesquisável? | Revisar fila, transporte e janelas |
| Autenticação | Como falhas se distribuem por identidade/origem? | Abrir consulta com contexto |
| Endpoints | Quais ativos têm cobertura e quais faltam? | Comparar inventário esperado |
| Detecções | Quais casos de uso geram demanda e resultado? | Revisar lógica, capacidade e tuning |

## Do gráfico ao registro

Um painel deve permitir reproduzir seu filtro, janela e agregação. Se mostra top 10, indique o recorte. Se agrupa usuários, preserve autoridade. Se usa dados normalizados, documente o parser. A tabela resumida precisa de caminho para os eventos de suporte, com acesso apropriado.

## Quatro implementações

Wazuh Dashboard apresenta dados indexados conforme padrões e permissões. Splunk dashboards executam pesquisas e podem depender de extrações, tokens e modelos. QRadar dashboards apresentam métricas e pesquisas do produto, com seus tipos e limites. Sentinel workbooks combinam consultas e visualizações sobre fontes/tabelas disponíveis. Um workbook não habilita coleta que ainda não existe.

## Métricas que enganam

Volume de alertas não mede ataques evitados. Quantidade de regras não mede cobertura. Percentual de endpoints com agente online não comprova todos os canais coletados. Média de atendimento sem definir início/fim e tipo de caso pode esconder backlog antigo.

Para cada indicador, registre unidade, fonte, atraso, população, cálculo, lacuna, responsável e decisão associada. Mostre estados “sem dados” e “zero observado” separadamente. Valores nulos não devem virar zero silenciosamente.

## Prática

Desenhe um dashboard de quatro painéis: última chegada por host esperado, atraso, falhas por origem e fila por idade. Para cada painel, descreva a query em linguagem natural, a unidade e o próximo passo. Teste um host sem qualquer evento, um duplicado e um com atraso. Confira se o gráfico comunica a limitação.

## Checkpoint

**Um top 10 representa todos os ativos?**

<details>
<summary>Ver resposta</summary>

Não. É um recorte que precisa ser rotulado, com acesso ao conjunto completo quando necessário.

</details>

**Zero e sem dados significam a mesma coisa?**

<details>
<summary>Ver resposta</summary>

Não. Zero observado exige cobertura; sem dados pode representar falha de coleta ou consulta.

</details>

[← Tópico anterior](tuning.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](siem-health.md)
