# Doze erros que deterioram uma detecção

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](retiring-detections.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](TEMPLATE-DETECCAO.md)

## Reconhecer o erro e escolher uma correção

| Erro | Por que prejudica | Correção verificável |
| --- | --- | --- |
| 1. Qualquer 4625 = High | Confunde registro frequente com impacto e evidência | Definir hipótese, contexto e prioridade |
| 2. Copiar regra sem schema | Campo ou fonte podem não existir | Comparar registro original e mapping |
| 3. Tag MITRE como conclusão | Descreve intenção, não cobertura | Justificar comportamento e teste |
| 4. Dezenas de regras sem owner | Falhas e exceções ficam sem revisão | Definir responsabilidade e inventário |
| 5. Tuning só por exclusões | Menos volume pode esconder positivos | Medir perdas e executar regressão |
| 6. Desligar por volume | Pode eliminar observabilidade necessária | Investigar mudança, duplicação e custo |
| 7. Testar apenas positivos | Não examina alcance excessivo ou cegueira | Incluir negativos e contraexemplos |
| 8. Ferramenta administrativa = malware | Ignora uso autorizado | Considerar cadeia, conta, ativo e finalidade |
| 9. Raridade = ataque | Baseline pode ser curto ou enviesado | Explicar população e hipóteses alternativas |
| 10. Regra sem ação | Consome fila sem orientar decisão | Runbook com próximos passos |
| 11. Não monitorar fonte | Silêncio vira falsa sensação de proteção | Fonte, campos, execução e atraso |
| 12. Nunca revisar legado | Ambiente muda e contrato perde validade | Revisão por risco e mudança |

## Um review aplicado

Proposta: “Excluir qualquer conta admin porque ela dispara muito”. Problemas: substring ampla, conta privilegiada potencialmente comprometida, falta de prazo e ausência de teste negativo. A mudança precisa ser devolvida com pergunta sobre o caso de uso e uma alternativa restrita baseada em evidência.

Uma exceção aceitável pode ainda ter risco residual. Documentar esse risco permite decisão informada; esconder o risco atrás de uma taxa de redução não melhora a detecção.

## Exercício

Escolha dois erros da tabela e escreva um exemplo de defeito, um teste que falharia e uma alteração que o corrigiria. Use os fixtures, sem dados reais. Inclua a condição sob a qual sua própria correção pode falhar.

Volte ao [template](TEMPLATE-DETECCAO.md): se objetivo, dados, teste, ação ou owner estiver vazio, o problema é maior que a sintaxe da query.

## Checkpoint

**Uma regra silenciosa e sem erros conhecidos pode ser considerada boa por padrão?**

<details>
<summary>Ver resposta</summary>

Não. Silêncio precisa ser interpretado com fonte, execução, campos, população, testes e utilidade operacional.

</details>

[← Tópico anterior](retiring-detections.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](TEMPLATE-DETECCAO.md)
