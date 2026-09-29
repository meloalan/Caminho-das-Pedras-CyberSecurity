# Lab 13: Dashboards úteis para SOC

[← Índice da trilha](../README.md) · [Página principal](../../README.md) · [Lab 12: ATT&CK](../lab-12-mitre/README.md) · [Projeto Final](../projeto-final-soc/README.md)

## Objetivo

Montar um painel que ajude uma pergunta operacional e encaminhe a investigação. Visual não substitui fonte, query, denominador ou critério.

## Painéis candidatos

| Visualização | Indicador útil | Decisão que apoia | Limite que deve aparecer |
| --- | --- | --- | --- |
| Falhas de autenticação | Contagem por conta, host, hora, LogonType e origem | Quais padrões revisar? | Volume normal, NAT, serviços e coleta ausente. |
| Contas criadas | Evento por ator, alvo, host e mudança aprovada | Quais alterações precisam de contexto? | 4720 não significa abuso; separar local, domínio e cloud. |
| PowerShell | Processos por pai, identidade, host e dados disponíveis | Que relações revisar? | Uso administrativo comum, command line ausente, políticas de coleta. |
| IPs externos | Conexões por processo, destino, destino/porta e período | Que conexão requer pivot? | Geo/reputação não é prova e saída legítima é normal. |
| Alertas por severidade | Fila, idade, estado, owner e falsos positivos conhecidos | Onde há atraso de resposta? | Severidade depende de regras locais; volume sem denominador. |
| Hosts envolvidos | Hosts distintos e estado de agente/coleta | Onde existe lacuna de ingestão? | Ativos sem eventos não aparecem sem inventário de referência. |

## Perguntas antes de publicar um gráfico

- Qual tabela e filtro produzem o indicador?
- A contagem é eventos, usuários, hosts ou alertas distintos?
- Que intervalo, timezone e retenção se aplicam?
- Há comparação com baseline e população total?
- Qual ação alguém toma ao ver a mudança?
- Quais campos vazios ou agentes ausentes escondem atividade?

## Implementação por plataforma

Use visualizações e agregações nativas do SIEM escolhido. Reutilize query dos Labs 05 e 06, explicando as alterações e schema. Mantenha thresholds e paleta acessíveis. Não trate mapa de calor de matriz ATT&CK como score de segurança.

## Entrega

Entregue uma captura redigida, queries, período, definições das métricas, legenda e uma limitação por visualização. O dashboard precisa levar a uma fonte investigável e não expor IP, identidade ou detalhes pessoais.
