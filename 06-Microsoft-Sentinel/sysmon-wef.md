# Coleta Sysmon com Windows Event Forwarding

[← Sentinel](README.md) · [Página principal](../README.md)

Este caminho alimenta `WindowsEvent`, usado pelas queries 03 e 06. Requer um coletor Windows separado; para começar apenas localmente, use o Event Viewer do Lab 03. Não é necessário configurar WEF para estudar o evento local.

## Arquitetura e pré-requisitos

VM de origem com Sysmon → assinatura WEF → Windows Event Collector (WEC), canal ForwardedEvents → AMA e DCR do conector Windows Forwarded Events → workspace, tabela WindowsEvent.

Use um domínio de laboratório isolado com origem e coletor ingressados, DNS e horário corretos, permissões administrativas para configuração e acesso da conta usada pela assinatura aos eventos da origem. O coletor deve ser elegível para AMA (Azure VM ou servidor habilitado no Azure Arc). Não exponha WinRM na Internet. Um cenário sem domínio exige configurar autenticação/certificados conforme a documentação; não é coberto por este roteiro inicial.

## Configuração orientada

1. Na origem, instale Sysmon com ProcessCreate habilitado e confirme um evento benigno no canal `Microsoft-Windows-Sysmon/Operational`.
2. Prepare a origem para acesso remoto aos eventos e WinRM dentro da rede do lab. No coletor, inicialize Windows Event Collector com `wecutil qc` em terminal elevado. Revise as mudanças de serviço/firewall e limite acesso à rede do exercício.
3. No Event Viewer do coletor, abra Subscriptions e crie uma assinatura **Collector initiated**, adicionando a origem pelo nome de domínio. Use uma identidade do laboratório com permissão de leitura do canal. Teste a conectividade na interface antes de continuar.
4. Na seleção de eventos da assinatura, use o canal Sysmon e o Event ID 1. O XML de seleção equivalente é mostrado abaixo. Use entrega de baixa latência no lab e destino **Forwarded Events**.
5. Execute o comando benigno do Lab 03 na origem. Antes de configurar nuvem, confirme que o evento chegou a **ForwardedEvents** no coletor, preservando provedor e campos. Se falhar, examine o estado da assinatura, DNS, WinRM, firewall e permissões do canal; não avance com coleta local incompleta.
6. Instale a solução que disponibiliza **Windows Forwarded Events** no Content hub do Sentinel. Abra esse conector e crie a DCR associada ao **coletor**, com o workspace de laboratório como destino e coleta do canal ForwardedEvents. Se a interface solicitar XPath no formato `canal!expressão`, use `ForwardedEvents!*[System[Provider[@Name='Microsoft-Windows-Sysmon'] and EventID=1]]`. Confirme AMA ativo e associação da DCR.
7. Gere outro evento e execute a query de conferência abaixo. Exija `Provider` correto e `EventData.Image` preenchido. Se os campos chegarem em outro formato, documente a configuração e ajuste o parser antes de executar o hunt.
8. Após os testes, remova a assinatura, associações/DCR e recursos criados exclusivamente para o lab quando não forem mais necessários. Revise as alterações de WinRM/firewall e custos remanescentes.

```xml
<QueryList>
  <Query Id="0" Path="Microsoft-Windows-Sysmon/Operational">
    <Select Path="Microsoft-Windows-Sysmon/Operational">*[System[EventID=1]]</Select>
  </Query>
</QueryList>
```

O XML acima é o filtro da assinatura WEF, não um arquivo DCR completo. Ele seleciona somente Process Creation. O filtro da DCR opera no canal ForwardedEvents do coletor; não confunda os dois canais.

## Conferência no workspace

```kql
WindowsEvent
| where TimeGenerated >= ago(1h)
| where Provider == "Microsoft-Windows-Sysmon" and EventID == 1
| project TimeGenerated, Computer, Provider, EventID, EventData
| take 10
```

A consulta procura amostras de Sysmon 1: filtra período/provedor/ID, seleciona campos e limita dez linhas. Não detecta ameaça; processos legítimos são esperados. Melhore filtrando o host de origem e comparando horário e ProcessGuid com o evento local. Resultado vazio pode indicar atraso, coleta incorreta ou ausência de eventos.

## Limites e fontes

Evite coletar os mesmos eventos por múltiplas DCRs, o que pode duplicar dados e custos. O conector de Security não substitui esse caminho. Esta arquitetura ainda precisa ser executada e validada no ambiente do usuário.

- [Microsoft: coleta de eventos Windows para Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/connect-services-windows-based)
- [Microsoft: configuração de assinatura iniciada pelo coletor](https://learn.microsoft.com/en-us/windows/win32/wec/creating-an-event-collector-subscription)
- [Catálogo: Windows Forwarded Events e tabela WindowsEvent](https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference)

TODO: adicionar evidência real do laboratório
