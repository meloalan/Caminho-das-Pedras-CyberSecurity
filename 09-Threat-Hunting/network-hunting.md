# Rede e DNS: relações que os dados permitem

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](identity-hunting.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](multisiem-hunting.md)

## Perguntas de rede

| Campo | Pergunta | Limite |
| --- | --- | --- |
| Origem/destino e portas | Quem se comunicou com quem? | NAT/proxy pode mudar identidade aparente |
| Protocolo e ação | Foi permitido, bloqueado ou apenas observado? | Porta não garante protocolo de aplicação |
| Bytes e duração | Qual volume e duração observados? | Ausentes em Sysmon do fixture; não inferir exfiltração |
| Domínio/DNS | Quem consultou qual nome e qual resposta? | Consulta pode falhar; cache e DoH alteram observabilidade |
| Processo | Qual execução iniciou a conexão? | Exige identificador compatível ou fonte endpoint |

Porta incomum não equivale a ataque. Porta 443 também não garante legitimidade ou identifica conteúdo. Firewall, proxy, NDR e flows possuem unidades e limites distintos.

## DNS e primeira observação

Um domínio raro merece perguntar: primeira observação em qual janela e população? Quantos hosts? Qual processo? Houve resposta e conexão compatível? Domínio recém-observado internamente não prova domínio novo no registro público.

E07 consulta updates.example.test e E08 conecta a um IP pela mesma execução. Sem resposta DNS, não existe evidência da resolução entre os dois. Um grafo correto mantém duas arestas saindo do processo.

## Periodicidade e beaconing

Compare intervalos, destino, host, processo, volume e duração quando disponíveis. Atualizadores, agentes e monitoramento também geram periodicidade. Três intervalos iguais numa janela curta são evidência fraca para distinguir causas. Agregação, atraso e amostragem podem fabricar regularidade.

N08/N09/N10 no suplemento registram conexões da mesma execução para 203.0.113.40 a cada cinco minutos. C02 documenta um exercício autorizado de monitoramento para essa execução. Isso enfraquece a hipótese de finalidade indevida no cenário, mas não cria uma allowlist global do destino.

## Próximo pivot

Procure a execução, seu pai, identidade, baseline e configuração de aplicação. Depois expanda o destino para outros hosts, separando NAT e contexto. Não trate o IP de documentação como infraestrutura real a consultar. Os [hunts 07 e 08](hunts.md) desenvolvem processo/conexão e DNS/processo.

## Checkpoint

**Regularidade temporal prova canal de comando e controle?**

<details>
<summary>Ver resposta</summary>

Não. É um padrão observável com alternativas legítimas. É necessário contexto do processo, finalidade, conteúdo quando disponível e cobertura.

</details>

[← Tópico anterior](identity-hunting.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](multisiem-hunting.md)
