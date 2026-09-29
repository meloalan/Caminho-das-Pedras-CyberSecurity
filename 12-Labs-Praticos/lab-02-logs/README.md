# Lab 02: Entendendo e gerando logs

[← Índice da trilha](../README.md) · [Página principal](../../README.md) · [Lab 01: Preparação](../lab-01-preparacao/README.md) · [Lab 03: Sysmon](../lab-03-sysmon/README.md)

**Pré-requisito:** Lab 01. **Status: roteiro, sem evidências reais anexadas.**

## Objetivo

Gerar mudanças pequenas e autorizadas, localizar os eventos na origem e distinguir o que o registro mostra da interpretação do analista.

## Eventos Windows para reconhecer

| ID | O que registra | Onde procurar e campos úteis | Observação |
| --- | --- | --- | --- |
| 4624 | Logon concluído com sucesso. | Event Viewer, Windows Logs, Security. Account, LogonType, Workstation, IpAddress. | Origem e campos variam com o tipo de logon. |
| 4625 | Falha de logon. | Security. TargetUserName, LogonType, Status, SubStatus, IpAddress. | É gerado no computador onde a tentativa foi feita. Uma falha não significa ataque. |
| 4688 | Processo criado, se auditoria estiver habilitada. | Security. NewProcessName, Creator/Subject, ProcessId, ParentProcessName e CommandLine quando coletado. | CommandLine pode estar desabilitada e conter segredo se for habilitada. |
| 4720 | Objeto de usuário criado. | Security. Subject, TargetUserName, TargetSid e computador. | Pode ser gerado em estação, member server e DC. Não determina conta local ou domínio sem contexto. |
| 4728 | Membro adicionado a grupo global de segurança. | Security, no controlador de domínio. Examine autor, alvo e grupo. | Evento de gestão de grupo, não prova que a alteração foi maliciosa. |
| 4732 | Membro adicionado a grupo local de segurança. | Security no sistema em que o grupo local existe. Examine autor, membro e grupo. | Distinguir de 4728 pelo tipo e escopo do grupo. |

Os nomes e descrições dos eventos vêm da [referência oficial de IDs coletáveis no Sentinel](https://learn.microsoft.com/azure/sentinel/windows-security-event-id-reference), das páginas Microsoft de [4624](https://learn.microsoft.com/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4624), [4625](https://learn.microsoft.com/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4625), [4688](https://learn.microsoft.com/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4688), [4720](https://learn.microsoft.com/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4720) e dos documentos de [auditoria avançada](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration) e [gestão de grupos](https://learn.microsoft.com/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/audit-security-group-management). A geração depende da política de auditoria e do sistema.

## Sequência segura

Execute cada atividade em VM própria, fora de domínio corporativo e com snapshot. Se não tiver certeza da política, use dados sintéticos em vez de alterar política do sistema.

1. **Logon bem-sucedido:** entre manualmente com uma conta de teste no Windows da VM. Encontre 4624 e compare conta, horário e LogonType.
2. **Logon malsucedido:** faça uma única tentativa manual com senha incorreta numa conta de laboratório. Encontre 4625. Não repita até lockout.
3. **Processo:** abra PowerShell e execute apenas `Get-Date`. Se Audit Process Creation estiver habilitada, localize 4688 e confira se CommandLine está presente.
4. **Criação de conta local:** opcional. Só numa VM descartável com snapshot, permissão administrativa e senha temporária. A página antiga [roteiro 4720](../02-EventID-4720/README.md) detalha geração e remoção; confira o nome antes de remover.
5. **Membro de grupo local:** opcional e somente em snapshot descartável. Crie grupo de laboratório sem privilégio, adicione a conta descartável e confira 4732. Não adicione ao grupo Administrators.
6. **Grupo de domínio:** apenas no domínio AD isolado que você criou no [Lab 01](../lab-01-preparacao/README.md), com conta descartável e revisão da política. No Active Directory Users and Computers, crie uma conta de teste e um grupo de segurança global chamado `GG-Lab-Auditoria`; adicione a conta a esse grupo. Registre horário, autor, membro e grupo. O evento 4728 é gerado no controlador de domínio para inclusão num grupo global de segurança. Não faça alterações em diretório de trabalho.
7. **Acesso remoto:** opcional entre duas VMs do segmento privado. Não habilite RDP/SSH na rede bridged ou na Internet. Registre os tipos de logon e a máquina que gerou o evento.
8. **Alteração de arquivo:** crie um arquivo de texto descartável em pasta de teste. No Windows, Object Access auditing precisa de política e SACL apropriadas; no Linux, logging depende da configuração instalada. Ausência do evento é resultado possível.

## Linux e firewall

Em Linux, observe `journalctl` ou `/var/log/auth.log` e `/var/log/secure`, conforme a distribuição e o serviço instalado. Eventos de autenticação podem incluir SSH, sudo e login local; formato e retenção variam. Para firewall, use regras já presentes e logs de laboratório, sem alterar políticas da rede doméstica. Confira o módulo [Linux e Windows](../../03-Linux-e-Windows/README.md) e o de [redes](../../02-Redes/README.md).

### Se 4728 não aparecer

No controlador de domínio de laboratório, confira a política avançada de auditoria em **Account Management > Audit Security Group Management** e habilite auditoria de sucesso. Aplique a política conforme a configuração do domínio e confirme que a subcategoria não está sendo sobrescrita por uma política conflitante. Gere uma única inclusão controlada no grupo descartável e consulte o canal Security do controlador. A política e os eventos de gestão de grupo estão descritos na [documentação Microsoft de auditoria de grupos](https://learn.microsoft.com/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/audit-security-group-management) e [configuração avançada de auditoria](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration). Se ainda não houver registro, anote o gap e confira geração, política, horário e máquina consultada antes de alterar outras configurações.

Para 4732, repita o raciocínio somente em grupo local descartável numa VM isolada. O evento é registrado no sistema que hospeda o grupo local. Não use grupos administrativos para este exercício.

## Investigue o evento, não só o ID

| Pergunta | O que procurar |
| --- | --- |
| Qual máquina gerou o registro? | Campo Computer e origem real do log. |
| Quem iniciou e quem foi afetado? | Subject/Target, conta, SID e tipo de logon. |
| Qual foi o horário? | UTC no XML, fuso da interface e diferença de relógio entre fontes. |
| O que o dado não mostra? | Intenção, autorização, causalidade e evento perdido não são inferidos só pelo ID. |

## Entrega

Preencha a tabela de ID, provedor, canal, política necessária, campos, horário, resultado e limitações. Inclua eventos encontrados apenas se tiver executado o lab. A próxima etapa cobre processo e rede via [Sysmon](../lab-03-sysmon/README.md).
