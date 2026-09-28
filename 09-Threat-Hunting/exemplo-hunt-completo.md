# HUNT-WIN-001: exemplo preenchido

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](TEMPLATE-RELATORIO-HUNT.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](referencias.md)

## Resumo executivo

Neste cenário inteiramente fictício, observamos três falhas seguidas de sucesso de LAB/alan.lab no WIN-LAB01, com privilégios especiais e PowerShell na sessão declarada. DNS e conexão estão ligados à execução por ProcessGuid. Os registros sustentam a sequência, mas não demonstram uso indevido da identidade. Faltam autorização e comandos interativos posteriores. O outcome é revisão contextual e proposta de melhoria, sem incidente confirmado.

## Identificação e hipótese

Hunt ID HUNT-WIN-001, autor Equipe LAB, data didática 28/09/2026, versão 1.0. Status: completed para a análise offline; conclusão de abuso: inconclusiva. Não houve execução em SIEM real.

Hipótese: uma identidade pode estar sendo utilizada fora da administração esperada após falhas de autenticação. Sustentaria abuso uma cadeia incompatível com função/autorizações corroborada por evidências independentes. Enfraqueceria uma atividade aprovada coerente com sessão, conta, host e finalidade.

Alternativas: erro de digitação, sessão administrativa legítima, automação ou uso indevido. C01 afirma apenas que existe demanda administrativa sem comprovação suficiente para E06, portanto não decide entre elas.

## Escopo e timebox

Período [2026-09-24T08:00:00Z, 10:00:00Z), população de quatro hosts do inventário. Pergunta inicial restrita à conta LAB/alan.lab no WIN-LAB01; outras cadeias analisadas separadamente como contexto. Timebox do exercício: uma sessão de estudo com checkpoint ao final da timeline, ajustável ao estudante. Encerrar com perguntas respondidas ou lacunas documentadas.

## Dados, cobertura e campos

Dataset original [módulo 07](../07-Buscas-e-Queries-em-SIEM/labs/dados/eventos.jsonl), suplemento [eventos-complementares.jsonl](labs/dados/eventos-complementares.jsonl), [cobertura](labs/dados/cobertura.csv) e [contexto](labs/dados/contexto.json). Todos fictícios.

WIN-LAB01 permite os pivots de Security e Sysmon. WIN-LAB02 não fornece rede/DNS da mesma forma no exercício. WIN-LAB03 não cobre a janela; DC-LAB01 cobre identidade. O inventário sozinho não prova coleta. Campos usados: timestamp, provider, event_id, host, domain, user, source_ip, logon_type, logon_id e process_guid.

## Queries e iterações

| Versão | Pergunta / filtro no contrato do fixture | Resultado esperado conferível |
| --- | --- | --- |
| Q01 v1 | Janela, host WIN-LAB01, Security-Auditing, IDs 4624/4625 | E01/E02/E03/E04/E10 |
| Q01 v2 | Separar domínio LAB, user alan.lab, origem e tipo | E01/E02/E03 → E04; E10 excluído por identidade distinta |
| Q02 v1 | Mesmo host e logon_id 0xA100 | E04/E05/E06 |
| Q03 v1 | Mesmo host e ProcessGuid de E06, Sysmon | E06/E07/E08 |
| Q04 v1 | Comparar E09 com a cadeia anterior | Relação causal não demonstrada |

As [consultas de entrada multisiem](multisiem-hunting.md) documentam implementações. Esta tabela relata leitura offline dos fixtures, não execução nessas plataformas. A versão de cada consulta e o dataset devem acompanhar uma reprodução real.

## Timeline e relações

| UTC | Registro | Fato | Grau da relação |
| --- | --- | --- | --- |
| 08:01/02/03 | E01/E02/E03 | Falhas de mesma chave | Candidatas à sequência com E04 |
| 08:05 | E04 | Sucesso; sessão 0xA100 | Identidade/host/origem/tipo compatíveis |
| 08:06 | E05 | Privilégios especiais na sessão | Sessão e host compatíveis |
| 08:08 | E06 | Criação PowerShell | Mesmo host/sessão declarados |
| 08:10 | E07 | Consulta DNS | Mesmo ProcessGuid |
| 08:12 | E08 | Conexão IP:443 | Mesmo ProcessGuid; sem resolução DNS comprovada |
| 08:15 | E09 | Conta criada por admin.lab no DC | Cadeia separada |

## Fatos, inferências e evidências concorrentes

Fato: a execução E06 possui registros DNS/rede relacionados. Inferência: vale revisar o contexto administrativo. Não demonstrado: download, comando interativo específico, comprometimento, movimento lateral ou relação com criação de conta.

N07 e C02 representam outra atividade administrativa delimitada e corroborada no cenário. Ela mostra por que um nome de ferramenta ou conexão periódica não decide intenção. C02 não autoriza E06. E10 é homônimo de outra autoridade. E12/E13 não devem dobrar a contagem da mesma execução.

## Limitações, conclusão e gaps

Não há hashes, resposta DNS, MFA, VPN ou conteúdo da comunicação no caso inicial. Baseline curta não representa toda a história. Zero eventos em WIN-LAB03 não permite conclusão sobre esse ativo. A sequência está sustentada no fixture; a hipótese de uso indevido permanece inconclusiva.

Telemetry gap: command/contexto interativo e cobertura de WIN-LAB03, a encaminhar para responsável de coleta. Detection gap: precisa avaliar a lógica/implantação existente e executar teste antes de afirmar que a sequência não está coberta. Ausência de alerta no exercício não prova esse gap.

## Outcome, recomendações e próximos passos

Solicitar contexto de E06 ao responsável fictício pela mudança, revisar qualidade de coleta, encaminhar sequência candidata para [Detection Engineering](hunt-to-detection.md) com casos legítimos e controles de homônimos. Owner de cada ação deve ser definido na execução real. Nenhuma regra foi implantada e nenhuma identidade foi bloqueada. Reabrir se surgirem evidências novas ou cobertura adicional relevante.

## Checkpoint

**A cadeia de conta criada pode ser incluída no mesmo ataque da autenticação?**

<details>
<summary>Ver resposta</summary>

Não com os dados disponíveis. Ela pode ser investigada como outra cadeia, mas proximidade de horário não comprova um único responsável ou causa.

</details>

[← Tópico anterior](TEMPLATE-RELATORIO-HUNT.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](referencias.md)
