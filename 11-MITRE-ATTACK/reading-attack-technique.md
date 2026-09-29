# Como ler uma página de técnica

[← Índice do módulo](README.md) · [Técnicas](techniques.md) · [Dados para detecção](attack-to-telemetry.md)

## Leia além do título e do ID

Ao examinar uma página ATT&CK atual, use a descrição e examine metadados, plataformas, relações, referências, detecção e mitigação. O título pode ajudar a localizar um objeto, mas não sustenta sozinho um mapeamento.

1. Confirme o domínio e a versão. Técnica Enterprise e técnica Mobile podem ter escopos diferentes.
2. Leia a descrição para delimitar que comportamento entra no objeto e o que fica fora.
3. Verifique plataformas e subtécnicas. Não infira uma subtécnica só por uma fonte de log.
4. Examine exemplos documentados e referências primárias. Exemplo publicado não prova o que ocorreu num caso local.
5. Veja relações e status. Procure objetos revogados, substituídos ou atualizados.
6. Examine a seção de detecção e os objetos de Detection Strategy e Analytics relacionados, se publicados.
7. Consulte mitigação como possibilidade de reduzir risco, não como detecção.
8. Registre a data e a versão usada no mapeamento.

## Fato, hipótese e limite

| Categoria | Exemplo de formulação |
| --- | --- |
| Fato local | O registro do provedor indica a criação do objeto de identidade às 14:05 UTC. |
| Interpretação | O evento é consistente com comportamento de criação de conta. |
| Mapeamento | T1136.003 é candidato se o objeto e o escopo cloud forem confirmados. |
| Hipótese de objetivo | Persistência é plausível, mas exige contexto. |
| Limitação | Os logs disponíveis não identificam o fluxo que iniciou a criação. |

## Referência atual

Consulte a página oficial de [T1136, Create Account](https://attack.mitre.org/techniques/T1136/) e as subtécnicas atuais antes de completar o exercício. Não assuma que capturas antigas, blogs ou layers antigas refletem o objeto vigente.
