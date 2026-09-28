# Template profissional de detecção

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](anti-patterns.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](referencias.md)

Copie este template para seu projeto e substitua as instruções por decisões e evidências. A estrutura expande o contrato existente; nenhuma seção preenchida por intenção deve ser apresentada como teste executado.

## 1. Identificação e status

ID estável, nome, versão, autor, owner e substituto: preencher. Status: rascunho/experimental/piloto/produção/aposentada conforme workflow local. Não declarar implantação sem evidência.

## 2. Objetivo, hipótese e risco

Descrever comportamento observável, risco, ativos e população. Escrever uma hipótese testável e uma explicação legítima alternativa. Definir o que a detecção não pretende reconhecer.

## 3. Fontes, campos e auditoria

Informar fonte, provedor, canal, tabela/índice, parser e versão. Mapear campo original para campo consultado, tipo e papel. Registrar auditoria, agentes, endpoints cobertos, retenção, relógio e atraso.

## 4. Lacunas de telemetria

Para cada campo ausente, host sem coleta, auditoria desabilitada, parser incompleto ou retenção insuficiente: impacto, evidência, owner, risco aceito e plano de correção. Não preencher lacunas com valores inventados.

## 5. Lógica, query e implementação

Linkar query e regra versionadas. Descrever seleção, agregação, comparação e unidades antes da sintaxe. Distinguir especificação de configuração do produto. Registrar backend/pipeline e dependências.

## 6. Tempo, threshold e correlação

Definir frequência, lookback, atraso tolerado, intervalos inclusivos/exclusivos, limiar, chaves, autoridade, ordem, deduplicação de eventos/alertas, nulos, dados fora de ordem e política de recuperação. Threshold sem unidade é incompleto.

## 7. Entidades e contexto do alerta

Ator versus alvo, host, conta/autoridade, IP/processo quando disponíveis. Definir título, motivo, contagem, janela, eventos relacionados, versão e acesso à evidência. Informar enriquecimento, origem e validade.

## 8. Severidade, confiança e prioridade

Justificar impacto potencial e força da evidência separadamente. Explicar como criticidade, privilégio, exposição e urgência influenciam a prioridade, sem inventar escala universal.

## 9. MITRE ATT&CK

Técnica/subtécnica, URL, versão consultada, comportamento, telemetria, campos, condição e limitações. Registrar por que a associação não equivale a confirmação de ataque ou cobertura total.

## 10. False positives e false negatives

Listar atividades legítimas, positivos benignos e comportamentos relevantes que podem escapar. Definir a condição de interesse usada nas classificações e manter categoria inconclusiva.

## 11. Exceções e validade

Motivo, evidência, escopo exato, owner, criação, expiração, risco, teste e decisão de aprovação. Prever falha do enriquecimento e abuso dentro do escopo permitido.

## 12. Validação e matriz de testes

Registrar fixture, versão, comando/procedimento, esperado e obtido para cada caso abaixo. Diferenciar unidade, parser, integração e piloto.

| Categoria | Entrada e versão | Resultado esperado | Resultado obtido e evidência |
| --- | --- | --- | --- |
| Positivo | Preencher | Definir antes de executar | Pendente |
| Negativo | Preencher | Definir antes de executar | Pendente |
| Limiar N-1/N/N+1 | Preencher | Definir antes de executar | Pendente |
| Bordas temporais | Preencher | Definir antes de executar | Pendente |
| Campo nulo | Preencher | Definir antes de executar | Pendente |
| Duplicata e conflito | Preencher | Definir antes de executar | Pendente |
| Ingestão atrasada | Preencher | Definir antes de executar | Pendente |
| Fora de ordem | Preencher | Definir antes de executar | Pendente |
| Exceção e expiração | Preencher | Definir antes de executar | Pendente |
| Regressão e integração | Preencher | Definir antes de executar | Pendente |

## 13. Performance e volume

Medir duração, recursos, cardinalidade, volume de resultados, alertas agrupados e esforço de investigação na população/período declarados. Comparar antes/depois sem otimizar apenas a queda de alertas.

## 14. Runbook e responsabilidade

Linkar runbook com fonte, entidades, contexto, timeline, autorização, evidência, escalonamento e feedback. Definir quem responde, quem mantém, quem aprova e quem aceita risco. Contenção exige avaliação de impacto.

## 15. Implantação, saúde e rollback

Escopo do piloto, janela de mudança, configuração necessária, verificação de entrega, indicadores de saúde e procedimento de reversão com versão anterior. Informar o que ainda não foi executado.

## 16. Versionamento, changelog e revisão

Registrar commit/versão, data, autor, motivo, teste, review e aprovação. Definir revisão por mudanças e cadência baseada no risco. Conferir necessidade, fonte, campo, técnica, infraestrutura, exceções e volume.

## 17. Critério de aposentadoria

Descrever quando retirar ou substituir; registrar motivo, data, substituição, impacto, dependências e aprovação. Preservar histórico e atualizar cobertura.

TODO: adicionar evidência real do laboratório

## Critério de qualidade

A especificação explica o que detecta, por que existe, risco, população, telemetria, campos, comportamento, testes, limitações, volume, resposta, owner e revisão. Se um desses itens não puder ser demonstrado, registre a lacuna.

## Checkpoint

**O template preenchido com planos equivale a validação?**

<details>
<summary>Ver resposta</summary>

Não. Separe proposta, esperado, execução e evidência. Cada resultado precisa de ambiente, versão e limites.

</details>

[← Tópico anterior](anti-patterns.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](referencias.md)
