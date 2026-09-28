# Sigma: descrição portável, validação específica

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](multisiem-detection.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](detection-as-code.md)

## O que o formato entrega

Sigma descreve determinadas detecções de logs com metadata, fonte e condição. Um backend converte a descrição usando um pipeline de campos e decisões próprias. O YAML não inclui automaticamente coleta, agendamento, estado operacional, incidente, runbook ou aprovação.

A [regra anterior de conta criada](../queries/sigma/windows-account-created.yml) foi preservada como baseline experimental. A nova [regra de cadeia Office para PowerShell](../detections/windows/process-creation/office-powershell.sigma.yml) ilustra múltiplas seleções. Ela marca uma cadeia para revisão, sem afirmar que ferramenta administrativa é malware.

## Estrutura da regra

| Campo | Papel neste exemplo |
| --- | --- |
| title e id | Nome compreensível e UUID estável |
| status e description | Experimental e escopo da correspondência |
| references e author | Origem técnica e autoria |
| date e modified | Datas de criação e alteração real |
| tags | Contexto ATT&CK justificado |
| logsource | Categoria de evento e produto |
| detection | Seleções e expressão lógica |
| falsepositives | Explicações legítimas conhecidas |
| level | Severidade proposta, sujeita ao ambiente |

Nem todos são obrigatórios na especificação. O padrão do projeto pode exigir mais metadata que o mínimo do formato. Use datas e status aceitos pela versão da ferramenta, sem inventar um formato universal para especificações próprias.

## Seleção e condição

```yaml
logsource:
  product: windows
  category: process_creation
detection:
  child:
    Image|endswith:
      - '\powershell.exe'
      - '\pwsh.exe'
  parent:
    ParentImage|endswith:
      - '\winword.exe'
      - '\excel.exe'
  condition: child and parent
```

Este bloco é um fragmento didático. O arquivo completo contém metadata e referências. A lista em Image oferece alternativas; a condição exige que as seleções child e parent correspondam. O pipeline deve mapear a categoria e os campos para a fonte realmente coletada. Sysmon 1 e Windows 4688 não possuem contratos idênticos.

## Conversão não é validação

| Verificação | Exemplo de defeito |
| --- | --- |
| Logsource | Categoria convertida para tabela não coletada |
| Campo e tipo | Image presente no Sigma, mas caminho nativo não mapeado |
| Modificador | Sufixo/caixa convertido com semântica diferente |
| Dados | ParentImage ausente ou truncado |
| Performance | Pesquisa ampla sem tempo ou fonte |
| Contexto | Automação legítima de Office correspondendo |
| Cobertura | Processo gerado em host sem auditoria |

O parser pySigma confere a estrutura da regra, não prova essas propriedades. A conversão conceitual para KQL seria filtrar processo e aplicar sufixos no executável e no pai; para SPL seria buscar a fonte correta e avaliar os campos extraídos. Só gere uma query de backend após escolher pipeline e versão, e compare os mesmos casos positivos e negativos.

## Revisão e entrega

Use os [casos de processo](../detections/tests/process-cases.json): cadeia correspondente, pai diferente e pai ausente. O resultado esperado é seleção, não veredito de ameaça. Documente mapeamento, query gerada, resultado real e limites quando houver ambiente.

Fontes: [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html) e [pySigma](https://github.com/SigmaHQ/pySigma). A validação local é reproduzível em [Detection as Code](detection-as-code.md).

## Checkpoint

**O parser aceitar a regra demonstra cobertura de PowerShell?**

<details>
<summary>Ver resposta</summary>

Não. Demonstra estrutura interpretável. A regra descreve uma cadeia específica; campo, pipeline, fonte, versão e comportamento no backend ainda precisam ser testados.

</details>

[← Tópico anterior](multisiem-detection.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](detection-as-code.md)
