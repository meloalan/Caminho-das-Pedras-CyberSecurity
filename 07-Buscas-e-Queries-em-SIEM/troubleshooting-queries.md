# Troubleshooting: consulta vazia ou ampla demais

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](performance.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](labs/README.md)

## Vazio não significa ausência de atividade

```mermaid
flowchart TD
    N0["Sem resultado"]
    N1["Há dados no período correto?"]
    N2["A fonte está chegando?"]
    N3["O campo existe e tem o tipo esperado?"]
    N4["O valor foi observado?"]
    N5["O filtro e a precedência estão corretos?"]
    N6["A sintaxe corresponde ao mecanismo?"]
    N7["Resultado ou lacuna documentada"]
    N0 e1@--> N1
    N1 e2@--> N2
    N2 e3@--> N3
    N3 e4@--> N4
    N4 e5@--> N5
    N5 e6@--> N6
    N6 e7@--> N7
    e1@{ animation: fast }
    e2@{ animation: fast }
    e3@{ animation: fast }
    e4@{ animation: fast }
    e5@{ animation: fast }
    e6@{ animation: fast }
    e7@{ animation: fast }
```

![Diagnóstico de consulta vazia e consulta ampla](../assets/images/07-buscas-queries/troubleshooting.svg)

Volte a uma amostra conhecida. Teste um filtro por vez, na mesma janela. Confira tabela/índice, permissões, retenção e origem. Compare campo ausente com valor vazio. Uma data fictícia fixa não aparece em últimas 24h meses depois. Um evento que existe no endpoint pode não estar indexado.

## Quando retorna demais

```mermaid
flowchart TD
    N0["Milhões de eventos"]
    N1["Período amplo demais?"]
    N2["Dataset inclui fontes irrelevantes?"]
    N3["Falta condição ou parênteses?"]
    N4["Campo representa a entidade correta?"]
    N5["Agregação responde melhor?"]
    N6["Selecionar campos e medir custo"]
    N0 e1@--> N1
    N1 e2@--> N2
    N2 e3@--> N3
    N3 e4@--> N4
    N4 e5@--> N5
    N5 e6@--> N6
    e1@{ animation: fast }
    e2@{ animation: fast }
    e3@{ animation: fast }
    e4@{ animation: fast }
    e5@{ animation: fast }
    e6@{ animation: fast }
```

Não coloque limite arbitrário e declare solução. Primeiro determine se a pergunta exige eventos ou resumo. Preserve capacidade de voltar ao detalhe.

| Sintoma | Hipótese | Teste |
| --- | --- | --- |
| KQL coluna inexistente | Outro schema/ambiente | getschema ou amostra autorizada |
| SPL stats vazio | Alias ausente ou multivalorado | table _raw e campos relevantes |
| AQL 4625 não aparece | QID confundido com Event ID | Comparar payload e LabEventID |
| Wazuh sucesso não aparece | Busca apenas em alerts | Conferir archives e indexação |
| Campo keyword não existe | Suposição sobre mapping | Ler mapping real |
| Contagem inflada | Duplicação ou many to many | Comparar IDs e cardinalidade |
| Timeline invertida | Ingestão usada como ocorrência | Conferir relógios e fuso |
| Top parece completo | Limite de hits/buckets | Total, paginação e indicadores de truncamento |

## Experimento controlado

Use E09, que não contém SourceIP. Uma query exigindo origem preenchida exclui a criação de conta. Isso não é falha da linguagem: é filtro incompatível com a pergunta. Registre a intenção do filtro e por que ele deve ser retirado ou aplicado apenas a outro tipo de evento.

## Entrega

Salve consulta inicial, amostra de controle, alterações uma a uma, resultado e causa. Nunca publique payload real com segredos ou informações pessoais. A [saúde do SIEM](../06-SIEM-na-Pratica/siem-health.md) explica problemas de coleta; aqui o foco é separar erro de consulta de lacuna de dados.

## Checkpoint

**Qual primeiro teste diante de zero linhas?**

<details>
<summary>Ver resposta</summary>

Validar uma amostra conhecida na fonte, dataset e período corretos, depois acrescentar filtros um a um.

</details>

[← Tópico anterior](performance.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](labs/README.md)
