# Tipos de lógica e evolução do sinal

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](telemetry-requirements.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](casos-de-uso.md)

## Escolha pela pergunta

| Tipo | Aplicação | Risco a testar |
| --- | --- | --- |
| Atomic | Um evento de limpeza do Security Log | Manutenção legítima também produz 1102 |
| Threshold | Contagem por identidade em uma janela | Duplicação, rajada legítima ou ataque lento |
| Sequence | Falhas anteriores a sucesso e sinal de sessão | Ordem, atraso, chaves e eventos ausentes |
| Correlation | Identidade, endpoint e rede relacionados | Junção com muitos resultados ou falso vínculo |
| Behavioral | Cadeia fora do padrão definido para um ativo | Baseline incompleto ou mudança administrativa |
| Statistical/anomaly | Distância de uma distribuição histórica | Sazonalidade e mudança de população |

Anomalia ≠ ataque. Um modelo estatístico não corrige automaticamente fonte incompleta, rótulo ruim ou falta de resposta operacional.

## Adicionar condições tem preço

| Evolução didática | Ganho | Possível perda |
| --- | --- | --- |
| Qualquer 4625 | Visibilidade ampla | Volume sem priorização |
| Múltiplos 4625 | Reduz eventos isolados | Atividade de baixa frequência |
| Mesma conta e autoridade | Melhora identidade | Password spraying entre contas |
| Janela curta e mesma origem | Reduz agrupamentos indevidos | Atividade lenta ou distribuída |
| Sucesso posterior | Prioriza uma sequência | Tentativas que não tiveram sucesso |
| Privilégios na sessão | Adiciona contexto | Sessão legítima e ausência do 4672 |
| Processo/rede associados | Aprofunda evidência | Dependência de mais sensores |

Essas são variantes de escopo, não degraus obrigatórios de “melhor detecção”. Uma regra de tentativa sem sucesso continua válida para outro objetivo. Separe o caso de uso em vez de exigir todos os sinais em toda regra.

## Composite detections

Login + privilégio + processo + conexão pode produzir uma investigação rica se os vínculos forem demonstrados. Use host, identidade/autoridade, identificador de sessão e ProcessGuid quando disponível. PID pode ser reutilizado; horário próximo não comprova relação.

Quanto mais sinais obrigatórios, maior a chance de perder casos por atraso ou coleta parcial. Uma alternativa é gerar candidato básico e acrescentar contexto sem fazer dele um filtro eliminatório. Teste latência, cardinalidade e custo antes de decidir.

**Entrega:** escolha dois tipos para o mesmo risco, escreva quais atividades cada um deixa de observar e justifique qual fila receberá cada sinal.

## Checkpoint

**Adicionar 4672 a toda autenticação suspeita sempre aumenta qualidade?**

<details>
<summary>Ver resposta</summary>

Não. Pode priorizar sessões com privilégios especiais, mas também excluir comportamentos relevantes sem esse evento ou sem coleta. 4672 não prova elevação indevida nem mudança de grupo.

</details>

[← Tópico anterior](telemetry-requirements.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](casos-de-uso.md)
