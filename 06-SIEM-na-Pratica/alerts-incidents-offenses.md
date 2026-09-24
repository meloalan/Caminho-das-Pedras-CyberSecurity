# Alertas, incidents e offenses

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](correlation-rules.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](investigacao.md)

## O objeto do produto e a conclusão do analista

Um evento representa uma ocorrência observada. Uma regra avalia condições. Um alerta chama atenção para um resultado. Um caso organiza trabalho e contexto. A nomenclatura comercial não determina se houve incidente de segurança confirmado.

| Plataforma | Objeto e uso | Limite de interpretação |
| --- | --- | --- |
| Wazuh | Alert com regra, nível, agente e dados | Não contém automaticamente tudo que o host fez |
| Splunk Enterprise | Alert resultante de pesquisa e condição | Não equivale sozinho à investigação do ES |
| Splunk Enterprise Security | Notables/findings e organização de investigação conforme versão | Fluxo e nomes precisam ser verificados no produto implantado |
| QRadar | Offense reúne informações relacionadas segundo regras e indexação | Pode agrupar atividades que exigem revisão de vínculo |
| Sentinel | Incident pode agrupar alertas e entidades | Agrupamento automático não comprova relação causal |

## Uma fila utilizável

Um alerta precisa de objetivo da detecção, referência dos dados, período, entidades, motivo do disparo, contexto disponível e responsável. O analista deve conseguir voltar ao registro que sustenta a condição. Título impactante com zero contexto aumenta retrabalho.

| Campo operacional | Exemplo fictício útil |
| --- | --- |
| Objetivo | Revisar criação de conta Windows fora do processo esperado |
| Evidência | 4720, host WIN-LAB01, ator admin-lab, alvo novo-lab |
| Janela | 2026-09-20, 08:00 a 08:20 UTC |
| Contexto | Autoridade local ainda a confirmar; mudança pendente de verificação |
| Próximo passo | Verificar responsável, grupo recebido e logons posteriores |
| Limite | O 4720 sozinho não mostra privilégio nem utilização |

## Triagem e classificação

Valide fonte, tempo, regra e entidades antes de classificar. Prioridade pode mudar com criticidade, privilégio, alcance e urgência. Atividade autorizada pode ser uma detecção tecnicamente correta. Defina as categorias do processo, incluindo positivo benigno quando utilizado, duplicata, caso conhecido, inconclusivo e falso positivo conforme o objetivo da regra.

Fechar o caso sem registrar motivo remove aprendizado. “Não encontrei mais nada” precisa de janela, fontes, cobertura e consultas. Se a fonte estava parada, isso é uma limitação material, não evidência de segurança.

## Agrupamento, supressão e perda de contexto

Agrupar une sinais num caso; suprimir reduz notificações; deduplicar remove cópias da mesma observação. São decisões diferentes. Agrupar toda atividade de um usuário durante um dia pode juntar hosts e sessões sem relação. Suprimir a conta pode ocultar outra origem relevante. Preserve acesso ao dado subjacente e documente a chave utilizada.

## Automação que ajuda a análise

Comece por etiqueta, atribuição ou enriquecimento de contexto. Defina condição, ordem, escopo, identidade executora, timeout, erros e idempotência. Repetir uma automação sobre o mesmo caso não deve criar comentários ou ações indefinidamente.

No Sentinel, Automation Rules podem coordenar ações sobre alertas/incidents e acionar playbooks quando suportado. Playbooks usam Logic Apps, com conexões, permissões e custos próprios. Em outras plataformas, integrações e SOAR têm contratos diferentes. Teste correspondência e não correspondência; mantenha logs de execução e caminho de desativação. Nenhum lab deste módulo exige bloquear usuário ou isolar máquina automaticamente.

## Prática

Receba o caso 4720 do [Lab 04](labs/lab-04-user-creation.md). Escreva um alerta útil, uma regra de agrupamento justificada e uma automação somente de etiqueta. Teste um segundo host e uma execução repetida. Explique quando a automação não deveria agir.

## Checkpoint

**Incident e offense significam ataque confirmado?**

<details>
<summary>Ver resposta</summary>

Não. São objetos de organização do produto, sujeitos à análise e aos critérios do processo.

</details>

**Supressão e deduplicação são sinônimos?**

<details>
<summary>Ver resposta</summary>

Não. Supressão reduz notificações; deduplicação trata cópias de observações, com chaves próprias.

</details>

[← Tópico anterior](correlation-rules.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](investigacao.md)
