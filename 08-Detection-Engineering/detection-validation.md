# Validar a capacidade, não só a sintaxe

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](tuning.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](testing-detections.md)

## Camadas de evidência

| Camada | O que valida | O que permanece aberto |
| --- | --- | --- |
| Estática | YAML, XML, campos esperados e sintaxe estrutural | Dados e execução do produto |
| Unidade | Lógica em entradas controladas | Parser, scheduler e transporte |
| Replay | Resposta a registros conhecidos | Geração/coleta original se não fizerem parte do teste |
| Integração no lab | Evento, coleta, parser, regra e alerta | Representatividade do ambiente real |
| Piloto | Volume, custo, fila e runbook em escopo definido | Outros ativos e condições não observadas |
| Regressão | Casos antigos após uma alteração | Comportamentos ainda não testados |

Uma conversão Sigma que produz texto não demonstra que o backend possui aquele campo. Uma query que retorna registros não demonstra que o scheduler processou o intervalo nem que o alerta chegou ao SOC.

## Matriz mínima

| Caso | Entrada | Esperado |
| --- | --- | --- |
| Positivo | Comportamento conforme contrato | Candidato com contexto |
| Negativo | Atividade semelhante fora da condição | Sem correspondência |
| Limiar | N-1, N, N+1 ocorrências únicas | Fronteira conforme especificação |
| Tempo | Início, fim, instante igual e fora da janela | Limites inclusivos/exclusivos respeitados |
| Nulo | Campo obrigatório ausente | Qualidade sinalizada ou correlação não avaliável |
| Duplicado | Mesmo registro recebido duas vezes | Não inflar a contagem |
| Atraso | Evento chega após a primeira execução | Falta inicial explicitada e política de recuperação testada |
| Fora de ordem | Entrada embaralhada | Ordem pelo relógio definido |

## Prova e evidência

Guarde entrada, versão, comando, saída esperada, saída obtida e divergência. Um teste que falha é informação útil; não altere o esperado só para deixá-lo verde. Diferencie rótulo sintético conhecido, decisão de triagem e comportamento confirmado por investigação.

O replay do avaliador local após atraso funciona porque ele reconsidera o conjunto histórico fornecido. Isso não implementa automaticamente lookback, estado ou deduplicação de alertas em um SIEM. No produto, teste a política de recuperação e uma chave de alerta estável por evento/entidade.

## Validação não exige simular ataque

Dados fictícios, replay controlado e testes unitários já ajudam a examinar lógica. Exercícios Purple Team ou BAS podem avaliar observabilidade em ambiente autorizado, com objetivos, escopo e critérios de parada. O módulo não exige exploração, força bruta ou limpeza de logs reais.

Purple Team conecta emulação autorizada, telemetria, detecção, SOC e feedback. O resultado mais útil pode ser descobrir que a fonte não registra o campo necessário. Registre a limitação em vez de compensá-la com uma conclusão mais forte.

## Checkpoint

**O replay histórico que encontra um evento atrasado prova que o agendamento o recuperará?**

<details>
<summary>Ver resposta</summary>

Não. O produto precisa de janela, tolerância a atraso e estratégia de recuperação compatíveis. Um teste separado deve medir perda e repetição de alertas.

</details>

[← Tópico anterior](tuning.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](testing-detections.md)
