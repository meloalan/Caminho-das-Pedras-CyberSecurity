# Do comportamento à telemetria

[← Índice do módulo](README.md) · [Técnicas](techniques.md) · [Detection Strategies](detection-strategies.md) · [Data Components](https://attack.mitre.org/datacomponents/)

## Telemetria é a ponte observável

ATT&CK descreve comportamentos. Fontes de dados produzem eventos, registros e atributos que podem ajudar a observar manifestações do comportamento. Um evento nunca deve ser tratado como tradução automática de um ID ATT&CK.

```text
comportamento candidato
        ↓
manifestação na plataforma
        ↓
fonte disponível e habilitada
        ↓
evento e campos coletados
        ↓
normalização, contexto e retenção
        ↓
hunting ou lógica de detecção
```

Uma quebra em qualquer etapa reduz visibilidade. A falta de evento pode resultar de comportamento ausente, auditoria desligada, fonte não implantada, campo omitido, retenção expirada ou falha de ingestão.

## Exemplo: criação de conta

O ATT&CK associa [DC0014 User Account Creation](https://attack.mitre.org/datacomponents/DC0014/) a evidência de criação de usuário. O componente indica uma classe de informação útil. Ele não garante um esquema idêntico nos produtos nem significa que a fonte está coletada no seu ambiente.

No Windows, Event ID 4720 é um registro possível de auditoria de criação de usuário. Para interpretar o tipo de conta, examine host, papel, diretório, identidade alvo e contexto. [Microsoft Learn](https://learn.microsoft.com/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4720) descreve quando esse evento é gerado. Para evidência de processo relacionado, [DC0032 Process Creation](https://attack.mitre.org/datacomponents/DC0032/) pode ser relevante quando a fonte correspondente estiver habilitada.

## Exemplo: PowerShell

[T1059.001](https://attack.mitre.org/techniques/T1059/001/) pode manifestar-se em dados de processo ou registros específicos do PowerShell, dependendo da configuração e plataforma. Process creation e PowerShell logging são fontes diferentes e podem registrar níveis de detalhe diferentes. Confirme quais campos realmente chegam ao SIEM. Sysmon Event ID 1 documenta criação de processo; não garante por si só uma linha de comando completa, conteúdo de script ou intenção.

## Perguntas para inventário

- Que fonte pode observar a manifestação considerada?
- Ela está habilitada e implantada nos ativos relevantes?
- Quais campos estão realmente presentes e normalizados?
- Que funções de host ou identidades precisam de enriquecimento?
- Qual é a retenção, latência e taxa de perda?
- Há diferenças de plataforma ou configuração?
- Como testar o caminho desde a origem até a consulta?

## Nota histórica sobre Data Sources

O ATT&CK marcou Data Sources como depreciados a partir da versão 18. A modelagem defensiva atual usa Detection Strategies, Analytics e Data Components. Fontes e eventos continuam sendo conceitos operacionais úteis, mas não devem ser confundidos com os objetos atuais do modelo ATT&CK. A página de [Data Sources](https://attack.mitre.org/datasources/) explica o status legado.

## Integração

O módulo 06 ajuda a inventariar fontes, ingestão e normalização. O módulo 07 ensina consultas, filtros e correlação. Este módulo relaciona essas capacidades ao comportamento e registra onde a evidência é insuficiente. A escolha do SIEM não muda a semântica da técnica ATT&CK.
