# ATT&CK com evidência e escopo

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](detection-as-code.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](coverage.md)

## Técnica mapeada não é técnica coberta

O mapeamento descreve a intenção adversária que o caso de uso procura observar. Um 4720 autorizado não se torna ataque por carregar uma tag. Para cada associação, escreva comportamento, fonte, campos, condição e o que não é observado.

| Mapeamento candidato | Evidência necessária | Limite |
| --- | --- | --- |
| [T1136.001](https://attack.mitre.org/techniques/T1136/001/), conta local | Criação, autoridade local confirmada e contexto de investigação | Não mede todas as formas de persistência |
| [T1136.002](https://attack.mitre.org/techniques/T1136/002/), conta de domínio | Criação em autoridade de domínio confirmada | Não aplicar somente pelo nome do usuário |
| [T1098](https://attack.mitre.org/techniques/T1098/), manipulação de conta | Mudança de associação/permissão contextualizada | Nem todo grupo concede privilégio; avaliar subtécnica atual pertinente |
| [T1059.001](https://attack.mitre.org/techniques/T1059/001/), PowerShell | Execução e cadeia/argumentos compatíveis com a hipótese | Uso da ferramenta não prova abuso |
| [T1070.001](https://attack.mitre.org/techniques/T1070/001/), limpeza de logs Windows | 1102 e contexto de possível ocultação | Manutenção legítima também pode ocorrer |

Falhas seguidas de sucesso não recebem automaticamente uma subtécnica de brute force: o padrão pode ter causas legítimas e não distinguir adivinhação, spraying ou outras formas de uso de credencial. Mapeie apenas quando a hipótese e a evidência sustentarem o comportamento específico.

## Modelo de justificativa

```text
Técnica/subtécnica e URL/versionamento:
Comportamento que buscamos:
Registro e provedor:
Campos que sustentam a condição:
População observável:
Teste que demonstra reconhecimento:
O que a regra não vê:
Por que a tag não é confirmação de ataque:
```

A regra original de conta criada mantém T1136 genérico porque abrange mais de um escopo. Só refine a subtécnica quando o contrato confirmar autoridade. Preservamos esse cuidado da versão anterior do módulo.

## Estrutura defensiva atual

Conferência documental em 28/09/2026: Data Sources foi descontinuado no ATT&CK v18, em outubro de 2025. O framework passou a usar Detection Strategies e Analytics, com mudanças em Data Components. A [página de Data Sources](https://attack.mitre.org/datasources/) permanece como referência histórica, não como catálogo que continua recebendo novas fontes.

Ao citar referências defensivas, confira a [estratégia de detecção](https://attack.mitre.org/detectionstrategies/) e os componentes atuais vinculados à técnica. Registre a versão consultada; não use um DS antigo como prova de validação de cobertura. Consulte também as [notas da mudança](https://attack.mitre.org/resources/updates/updates-october-2025/).

**Exercício:** uma regra com tag T1059.001 só pesquisa filhos de Office. Escreva três condições fora do escopo: execução por outro pai, host sem coleta e processo cujo campo foi perdido. A tag não cobre essas condições.

## Checkpoint

**Colorir uma técnica no Navigator demonstra cobertura completa?**

<details>
<summary>Ver resposta</summary>

Não. É uma representação de mapeamento. Cobertura exige população, fonte, campos, implantação, testes e limitações explicitamente registrados.

</details>

[← Tópico anterior](detection-as-code.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](coverage.md)
