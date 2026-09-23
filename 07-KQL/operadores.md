# Operadores essenciais

[← Índice do módulo](README.md) · [Página principal](../README.md)

## Conceito

Filtrar cedo reduz o conjunto analisado. Agrupar muda a granularidade: depois de summarize, colunas que não foram agrupadas ou agregadas não permanecem disponíveis.

## Prática orientada

Execute cada exemplo abaixo separadamente e explique como a saída muda.

## Entrega para o portfólio

Tabela de operadores e duas interpretações de resultados.

## Critério de conclusão

Explique o resultado com suas palavras, registre as limitações e diferencie o que foi observado do que foi inferido. Dados de laboratório devem ser anonimizados antes da publicação.

## where

Filtra linhas pelo predicado.

```kql
SecurityEvent
| where TimeGenerated >= ago(24h) and EventID == 4625
```

Falhas recentes; erros de senha legítimos também aparecem. Melhore separando tipos de logon.

## project

Seleciona e ordena colunas.

```kql
SecurityEvent
| where TimeGenerated >= ago(1h)
| project TimeGenerated, Computer, EventID
```

Contexto mínimo; não detecta ameaça. Inclua campos específicos da investigação.

## summarize e bin()

Agrupa eventos em intervalos fixos.

```kql
SecurityEvent
| where TimeGenerated >= ago(24h) and EventID == 4625
| summarize Failures = count() by Computer, bin(TimeGenerated, 5m)
```

Picos de falhas; manutenção pode gerar picos. Bins separam eventos na fronteira; use janela móvel para correlação temporal.

## extend

Cria uma coluna calculada.

```kql
SecurityEvent
| where TimeGenerated >= ago(1h)
| extend HostNormalized = tolower(Computer)
| project Computer, HostNormalized
```

Normaliza caixa do host; não unifica nomes curtos e FQDN. Não é detecção. Melhore com inventário de identidades.

## count

Conta as linhas restantes.

```kql
SecurityEvent
| where TimeGenerated >= ago(1h) and EventID == 4625
| count
```

Volume total de falhas; volume não comprova ataque. Compare baseline e cobertura.

## distinct

Retorna combinações únicas.

```kql
SecurityEvent
| where TimeGenerated >= ago(24h)
| distinct Computer, EventID
```

Inventário de tipos de evento por host. Não detecta hosts totalmente ausentes. Compare inventário esperado.

## sort

Ordena todas as linhas.

```kql
SecurityEvent
| where TimeGenerated >= ago(1h) and EventID == 4625
| sort by TimeGenerated desc
```

Mostra eventos recentes; ordem não implica causalidade. Use chaves de correlação.

## top

Seleciona os primeiros N pela ordenação.

```kql
SecurityEvent
| where TimeGenerated >= ago(24h) and EventID == 4625
| summarize Failures = count() by Computer
| top 5 by Failures desc
```

Cinco hosts com maior volume, inclusive atividade legítima. Outros hosts ficam ocultos; compare proporções e contexto.

## let e ago()

Nomeia um valor e calcula início relativo ao presente.

```kql
let Period = 24h;
SecurityEvent
| where TimeGenerated >= ago(Period)
| where EventID == 4720
```

Criação de contas no período, inclusive autorizadas. Verifique ator e janela de mudança.

## join

Relaciona duas tabelas por uma chave.

```kql
let Hosts = datatable(Computer:string, OwnerRole:string)["LAB-01", "Equipe de testes"];
datatable(Computer:string, EventID:int)["LAB-01", 4625, "LAB-02", 4625]
| join kind=leftouter (Hosts) on Computer
| project Computer, EventID, OwnerRole
```

Enriquecimento sintético, sem detecção: LAB-01 recebe responsável; LAB-02 fica sem correspondência. Melhore com inventário completo e chave única.
