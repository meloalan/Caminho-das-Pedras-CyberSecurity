# Laboratórios de buscas e queries

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](../troubleshooting-queries.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](dados/README.md)

## Um conjunto, várias perguntas

Comece sem SIEM no Lab 01. Depois escolha percurso offline ou uma plataforma disponível. As consultas operacionais exigem ingestão/schema próprios; não é necessário instalar quatro SIEMs ou contratar cloud. O JSON local não é EVTX nem export nativo de qualquer produto.

| Lab | Foco e entrega |
| --- | --- |
| [01: Entendendo campos sem SIEM](lab-01-entendendo-campos.md) | Identificar tipos, papéis e perguntas antes de escrever código. |
| [02: Filtros e precedência](lab-02-filtros.md) | Construir uma população correta sem perder dados silenciosamente. |
| [03: Agregações e denominadores](lab-03-agregacoes.md) | Distinguir evento, grupo, origem distinta e percentual. |
| [04: Investigar falhas e autenticação aceita](lab-04-autenticacao.md) | Formular hipóteses concorrentes para uma sequência. |
| [05: Correlação temporal e casos de borda](lab-05-correlacao-temporal.md) | Verificar anterioridade, janela e completude da chave. |
| [06: Processos, pais e comandos](lab-06-processos.md) | Comparar duas execuções sem chamar PowerShell de malicioso. |
| [07: Pivôs com chaves verificáveis](lab-07-pivot.md) | Passar de processo para DNS/rede e reconhecer onde parar. |
| [08: Hunting e raridade](lab-08-threat-hunting.md) | Testar hipótese e registrar contradições. |
| [09: Query para apoiar detecção](lab-09-detection-query.md) | Especificar e testar uma condição antes de agendar regra. |
| [10: Investigação final multisiem](lab-10-investigacao-multisiem.md) | Produzir perguntas, queries, pivôs, timeline e conclusão proporcional. |

## Dados e resultados reproduzíveis

O [guia dos dados](dados/README.md) documenta 22 registros: vinte do dia investigado e dois históricos. O [analisador local](dados/analisar.py) usa a biblioteca padrão Python, não acessa a rede e não modifica arquivos. Execute a partir desta pasta:

```powershell
python .\dadosnalisar.py
```

O programa imprime contagens, IDs da sequência, eventos do mesmo ProcessGuid e fontes ausentes no inventário. Isso verifica a lógica sobre o fixture, não executa KQL/SPL/AQL/Query DSL.

## Critérios de avanço

Você deve explicar o resultado, apontar uma limitação e reproduzir a seleção dos registros. Antes de habilitar uma regra, valide casos positivos, negativos e fronteiras. Não execute ataques, gere bloqueios nem altere auditoria em ambiente de terceiros para preencher o roteiro.

## Evidência para portfólio

```text
Percurso e versão:
Pergunta:
Dataset/schema/campos:
Janela e fuso:
Query ou cálculo offline:
Resultado esperado:
Resultado obtido e IDs:
Diferenças e interpretação:
Hipótese alternativa e lacunas:
Próximo teste:
```

Use a [Issue individual](https://github.com/meloalan/Caminho-das-Pedras-CyberSecurity/issues/new?template=modulo-07-buscas-queries-siem.md) para acompanhar progresso sem alterar arquivos do projeto. Publique apenas dados sintéticos.

## Checkpoint

**O que o analisador Python valida?**

<details>
<summary>Ver resposta</summary>

O cálculo sobre o dataset local e suas chaves. Não comprova sintaxe executada ou configuração dos quatro SIEMs.

</details>

[← Tópico anterior](../troubleshooting-queries.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](dados/README.md)
