# Lab 05: Criação de processo com Sysmon

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-04-user-creation.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-06-detection-rule.md)

> Pergunta: qual processo executou e quais relações são observáveis?

## Objetivo e pré-requisitos

Entender Sysmon 1 e os limites de linhagem/rede. Leia [Sysmon e WEF](../sysmon-wef.md). O [Lab 03 anterior](../../12-Labs-Praticos/03-Sysmon-EventID-1/README.md) oferece uma execução benigna. Sysmon, canal e coleta precisam estar configurados antes de esperar dados.

## Execução

1. Localize Sysmon 1, conferindo provider além do ID.
2. Registre host, usuário, pai, imagem, comando, início e ProcessGuid.
3. Relacione ao LogonId quando disponível, preservando escopo do host.
4. Compare o Sysmon 3 fictício com o mesmo ProcessGuid e protocolo TCP.
5. Explique por que o comando benigno de data não basta para explicar a comunicação posterior.
6. Escolha dados adicionais necessários sem executar tráfego suspeito.

## Caminhos de pesquisa

Wazuh usa canal eventchannel e dados win.*; Splunk precisa do input/extrações Sysmon; QRadar precisa do caminho WinCollect/DSM compatível; Sentinel usa WindowsEvent no percurso WEF do módulo. SecurityEvent=1 não substitui esse contrato.

## Resultado esperado

No dataset, `-NoExit` mantém o PowerShell aberto após consultar a data, permitindo ações posteriores que a linha de criação não descreve. O dataset oferece uma relação explícita de ProcessGuid entre processo e comunicação, porém não explica a finalidade. PID sozinho seria uma chave fraca. Uma prática real que executa apenas Get-Date não precisa gerar Sysmon 3; não force o resultado a coincidir com a ficção.

## Entrega

Árvore com campos e tabela de fatos/limites. Critério de conclusão: distinguir criação de processo, atividade posterior e intenção, além de lembrar que Sysmon 3 cobre TCP/UDP, não todo ICMP.

## Resultado obtido

Preencha após sua execução: percurso, versão quando aplicável, evidência, divergências e limitações. Não marque configuração de produto como validada com base apenas na análise offline.

## Checkpoint

**Qual evidência sustenta sua entrega?**

<details>
<summary>Ver resposta</summary>

Registre fonte, janela, consulta ou cálculo, resultado e limite. Uma descrição do que deveria ocorrer não substitui resultado obtido.

</details>

[← Tópico anterior](lab-04-user-creation.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-06-detection-rule.md)
