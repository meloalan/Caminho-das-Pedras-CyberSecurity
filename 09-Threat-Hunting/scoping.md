# Escopo, timebox e condição de saída

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](bias-e-raciocinio.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](hunting-telemetry.md)

## Um contrato de investigação

| Dimensão | Exemplo fictício | Limite |
| --- | --- | --- |
| Objetivo | Investigar a sequência de autenticação de LAB/alan.lab | Não avaliar toda a segurança do domínio |
| População | WIN-LAB01, WIN-LAB02, WIN-LAB03 e DC-LAB01 | Inventário esperado não significa coleta comprovada |
| Período | [2026-09-24 08:00Z, 10:00Z) | Eventos anteriores entram apenas como contexto declarado |
| Fontes | Security, Sysmon e contexto administrativo sintético | Sem EDR, VPN ou logs cloud neste fixture |
| Expansão | Nova identidade ligada por SID ou nova execução por GUID | Nome parecido não autoriza associação |
| Saída | Perguntas respondidas ou lacunas registradas e encaminhadas | Não esperar encontrar um incidente |

## Tempo de trabalho e tempo dos eventos

Timebox limita esforço de análise. A janela de eventos limita dados. São medidas diferentes. Negocie tempo conforme risco, volume e capacidade, com checkpoint para parar, ampliar ou encaminhar. Um incidente relevante pode exigir transição para IR antes do encerramento normal.

## Amostragem e custo

“Todos os logs dos últimos 12 meses” pode exceder retenção e orçamento. Comece com uma população justificável. Se usar amostra, registre método, tamanho, vieses e o que ela não representa. Um top 10 não cobre a população inteira.

## Mudança de escopo

Registre: motivo, novos ativos, período, fontes, responsável e impacto. Preserve os resultados da rodada anterior. Não renomeie uma pesquisa incompleta como uma investigação abrangente.

Entregável: uma linha de escopo que outra pessoa consiga aplicar e uma regra de parada que não dependa do resultado desejado.

## Checkpoint

**O que fazer quando surge um host fora da população?**

<details>
<summary>Ver resposta</summary>

Registrar a relação e decidir uma expansão justificada. Se não houver cobertura ou autorização, registrar a limitação e encaminhar.

</details>

[← Tópico anterior](bias-e-raciocinio.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](hunting-telemetry.md)
