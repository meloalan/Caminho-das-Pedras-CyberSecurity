# ATT&CK muda

[← Índice do módulo](README.md) · [Dados e STIX](attack-data-and-stix.md) · [Anti-patterns](mapping-anti-patterns.md)

## Registro de referência

Uma referência responsável registra:

```text
ID ATT&CK + domínio + versão + data da análise
```

Descrições podem evoluir, técnicas e subtécnicas podem ser acrescentadas ou reorganizadas, relações podem mudar, e objetos podem ser depreciados ou revogados. O modelo defensivo também muda. Um identificador isolado não informa qual descrição ou relações o analista consultou.

## Snapshot utilizado neste módulo

| Campo | Valor |
| --- | --- |
| Domínio principal | Enterprise ATT&CK |
| Versão consultada | 19.2 |
| Data da validação editorial | 2026-09-29 |
| Navegador consultado | ATT&CK Navigator 5.3.2 |
| Atualização automática | Não. Confirme fontes oficiais antes de uso operacional. |

A versão 19.0 introduziu mudanças substanciais, incluindo a revisão da organização de Defense Evasion. A estrutura atual Enterprise distingue **Stealth** (`TA0005`) e **Defense Impairment** (`TA0112`). Atualizações ágeis posteriores revisam conteúdo entre versões principais. Verifique [histórico de versões](https://attack.mitre.org/resources/versions/) e [notas de atualização](https://attack.mitre.org/resources/updates/) antes de reutilizar uma referência.

## Depreciado não é revogado

- **Deprecated:** conteúdo legado continua reconhecível, mas o modelo desencoraja novo uso ou prevê substituição. Exemplo importante: Data Sources foram depreciados na v18; use objetos defensivos atuais para novo trabalho.
- **Revoked:** um objeto foi formalmente revogado e não deve ser tratado como ativo sem conferir o motivo e eventual substituto.
- **Alterado ou dividido:** um conceito pode ser reorganizado e demandar revisão de mappings. Por exemplo, Defense Evasion antigo não deve ser copiado como se fosse uma tática atual única na versão 19.

IDs externos precisam ser interpretados junto ao tipo do objeto. Uma validação do bundle Enterprise vigente encontrou `T1136` tanto como a técnica ativa **Create Account** quanto como uma Mitigation legada chamada **Create Account Mitigation**, marcada depreciada. Não conclua que a técnica está depreciada por coincidência de ID. Consulte o tipo e o status do objeto correto.

O estado e a substituição devem ser verificados no bundle e no histórico da versão correspondente. Uma página atual pode ocultar a interpretação que fazia sentido num relatório histórico. Preserve a versão original e anote a migração.

## Procedimento de revisão

1. Fixe bundle, domínio, release e data de aquisição.
2. Compare IDs, nomes, status, relações e propriedades com a versão usada anteriormente.
3. Verifique substitutos sugeridos sem migrar automaticamente.
4. Atualize páginas, queries e camadas do Navigator em revisão controlada.
5. Revalide evidência e lógica local, pois mudança taxonômica não altera automaticamente os eventos coletados.
6. Registre o que mudou e os impactos nos consumidores.

`attack-version.json` mantém os metadados deste material. É um registro estático e não indica a versão mais recente futuramente.
