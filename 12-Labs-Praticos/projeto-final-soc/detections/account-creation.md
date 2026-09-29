# Exemplo de ficha: criação de conta local

**Estado:** exemplo conceitual com fixture sintética. Não foi executado num SIEM.

| Campo | Descrição do exercício |
| --- | --- |
| Nome | Lab, Windows user account creation |
| Hipótese | Criações de conta local em host de laboratório devem ser revisadas com o ator e o alvo. |
| Fonte | Security, Microsoft-Windows-Security-Auditing, Event ID 4720. |
| Campos | Horário UTC, host, SubjectUserName/SID, TargetUserName/SID, tipo de conta confirmado. |
| Query | Filtrar 4720, projetar autor, alvo, host e hora, incluir o evento original. |
| ATT&CK | T1136.001 candidato somente após confirmar escopo local no host independente. ATT&CK Enterprise v19.2, conforme validação do módulo 11. |
| Severidade | Baixa para triagem didática. Uma política de produção exige critérios locais de risco. |
| Falsos positivos | Provisionamento autorizado, suporte, instalação de agente e rotina de manutenção. |
| Tuning | Enriquecer mudança aprovada. Não suprimir globalmente atividade de administradores. |
| Validation | Teste de evento local, evento 4624 negativo e ausência do alvo. Estado pendente para execução real. |
| Owner | Preencher com equipe responsável antes de qualquer uso operacional. |
| Version | 0.1, exemplo não implantado. |

**Limite:** esta lógica seleciona uma classe de evento. Ela não prova uso adversário, cobertura geral de T1136 nem detecção de contas de domínio ou cloud.
