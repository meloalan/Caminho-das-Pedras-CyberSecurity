# Lab 04: Criação de usuário

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-03-windows-authentication.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-05-sysmon-process-creation.md)

> Pergunta: quem criou qual conta e o que ainda não sabemos?

## Objetivo e pré-requisitos

Investigar 4720 distinguindo Subject e Target. O [Lab 02 anterior](../../12-Labs-Praticos/02-EventID-4720/README.md) oferece criação benigna de conta descartável local em VM própria. Você pode usar somente o dataset sem criar nenhuma conta.

## Execução

1. Localize o registro 4720 e confirme fonte/host/tempo.
2. Identifique admin-lab como ator e novo-lab como alvo na representação fictícia.
3. Determine se a autoridade indica conta local ou domínio.
4. Pergunte se existe mudança autorizada, qual finalidade e quem confirma.
5. Procure evidência separada para grupos recebidos e logons posteriores; marque ausência no dataset como lacuna.
6. Explique por que esse ator diferente não fica ligado automaticamente à sequência de lab-user.

## Quatro ambientes

Wazuh: win.eventdata com subject/target e regra 4720. Splunk: EventCode e aliases lab_actor/lab_user. QRadar: LabEventID, LabActor, LabUser e autoridade validada. Sentinel: SubjectUserName e TargetUserName em SecurityEvent. Os nomes mudam, mas a distinção de papéis permanece.

## Resultado esperado

Uma criação local sintética em WIN-LAB01 às 08:15 UTC. Não há registro de grupo nem uso posterior no conjunto. O mapeamento ATT&CK local pode ser discutido como comportamento de interesse, sem afirmar intenção adversária.

## Entrega

Ficha do caso e matriz de dados presentes/ausentes. Se executar a criação benigna na VM, siga a limpeza do lab original e registre resultado real. Critério de conclusão: não atribuir ao 4720 informações que precisam de outros eventos.

## Resultado obtido

Preencha após sua execução: percurso, versão quando aplicável, evidência, divergências e limitações. Não marque configuração de produto como validada com base apenas na análise offline.

## Checkpoint

**Qual evidência sustenta sua entrega?**

<details>
<summary>Ver resposta</summary>

Registre fonte, janela, consulta ou cálculo, resultado e limite. Uma descrição do que deveria ocorrer não substitui resultado obtido.

</details>

[← Tópico anterior](lab-03-windows-authentication.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-05-sysmon-process-creation.md)
