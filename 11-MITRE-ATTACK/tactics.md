# Táticas Enterprise

[← Fundamentos](fundamentals.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Técnicas →](techniques.md)

ATT&CK define tática como o “porquê” tático de uma técnica ou subtécnica, isto é, o objetivo associado ao comportamento. Não significa uma fase obrigatória por que todo incidente deva passar. Uma técnica pode estar associada a mais de uma tática, pois contexto e uso documentado importam.

## Enterprise na versão 19.2

A tabela reflete a lista oficial consultada em 2026-09-29. As perguntas são recursos pedagógicos, não definições formais adicionais.

| ID | Tática atual | Pergunta de orientação |
| --- | --- | --- |
| TA0043 | Reconnaissance | Que informação pode ser coletada para preparar a operação? |
| TA0042 | Resource Development | Que recursos podem ser estabelecidos para apoiar a operação? |
| TA0001 | Initial Access | Como o adversário pode obter um ponto de entrada? |
| TA0002 | Execution | Como código ou comandos podem ser executados? |
| TA0003 | Persistence | Como acesso pode ser mantido? |
| TA0004 | Privilege Escalation | Como pode obter permissões superiores? |
| TA0005 | Stealth | Como pode ocultar ações e parecer atividade normal? |
| TA0112 | Defense Impairment | Como pode quebrar, enfraquecer ou tornar não confiáveis mecanismos defensivos e de monitoramento? |
| TA0006 | Credential Access | Como pode tentar obter credenciais? |
| TA0007 | Discovery | Como pode tentar entender o ambiente? |
| TA0008 | Lateral Movement | Como pode acessar outros sistemas? |
| TA0009 | Collection | Como pode reunir dados relevantes ao objetivo? |
| TA0011 | Command and Control | Como pode se comunicar com sistemas sob controle? |
| TA0010 | Exfiltration | Como dados podem ser removidos do ambiente? |
| TA0040 | Impact | Como sistemas ou dados podem ser manipulados, interrompidos ou destruídos? |

Use os identificadores e nomes da versão atual em novos registros. A matriz não é uma cronologia. A posição de Reconnaissance antes de Initial Access não prova que um caso seguiu todos os passos nessa ordem.

## O que mudou em Defense Evasion

Na Enterprise v19.0, a tática anteriormente chamada **Defense Evasion** foi dividida em duas táticas: **Stealth (TA0005)**, para ocultação e mistura com atividade legítima sem alterar diretamente os controles defensivos, e **Defense Impairment (TA0112)**, para comprometer ou reduzir a efetividade, integridade ou confiança em mecanismos, pipelines e ferramentas de defesa. A antiga TA0005 agora identifica Stealth, portanto nomes e IDs históricos não devem ser copiados sem versão.

Ao migrar um registro antigo, examine o comportamento e a relação atual da técnica. Não renomeie mecanicamente todo mapping antigo de Defense Evasion para uma das novas táticas. Um mapping pode precisar ser dividido, contextualizado, mantido como referência histórica ou retirado.

## Não decorar, interpretar

Comportamento: uma nova conta foi criada.

Pergunta: qual objetivo isso pode servir?

Pode estar associado a persistência, mas criação de conta também pode ser administração legítima, provisionamento de serviço, atividade cloud ou outra mudança aprovada. Um Event ID pode registrar o evento, mas não determina intenção ou objetivo. Para mapear, confirme tipo de conta, ambiente, atividade associada e evidência de contexto. O [lab de Create Account](labs/lab-03-create-account.md) explora essa diferença.

Fontes: [táticas Enterprise](https://attack.mitre.org/tactics/) apresenta os objetos correntes; [notas da v19](https://attack.mitre.org/resources/updates/updates-april-2026/) descrevem a divisão de Defense Evasion.

---

[← Fundamentos](fundamentals.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Técnicas →](techniques.md)
