# Classificar resultados sem esconder falsos negativos

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](severity-and-confidence.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](tuning.md)

## Primeiro defina a condição de interesse

Se a regra promete reconhecer qualquer criação de conta, uma criação autorizada corretamente registrada é uma correspondência verdadeira. Operacionalmente, pode ser chamada de positivo benigno. Se o objetivo declarado é reconhecer criação que exige investigação por ausência de autorização, a mesma conta aprovada é negativa nessa classificação. Não misture as duas perguntas na métrica.

| Resultado | Predição e referência | Exemplo para “requer investigação” |
| --- | --- | --- |
| True Positive | Alerta em caso relevante | Criação que o exercício rotula como não aprovada |
| False Positive | Alerta em caso negativo | Provisionamento aprovado, fora do interesse da lógica |
| True Negative | Sem alerta em caso negativo | Exceção válida de mudança aprovada |
| False Negative | Sem alerta em caso relevante | Conta relevante excluída pelo prefixo svc_ |
| Benign Positive | Comportamento detectado de fato, explicado como legítimo | Baseline 4720 identifica criação autorizada |

Nomenclaturas variam no SOC. Guarde a definição, evidência de classificação e estado inconclusivo. Analista sem contexto não deve ser obrigado a marcar “benigno” para encerrar uma fila.

## Falsos negativos merecem ensaio

A exclusão `svc_*` parece conveniente porque contas de serviço geram volume. Entretanto, qualquer atividade relevante por uma identidade com esse prefixo poderá desaparecer. Nome da conta não é prova de finalidade nem autorização.

No [dataset de tuning](../detections/tests/tuning.jsonl), 70 candidatos usam ator com prefixo svc_. Sessenta são provisionamento aprovado e dez são casos relevantes fictícios. Excluir todos elimina os dois grupos. O [lab 07](labs/lab-07-false-negatives.md) pede um contraexemplo explícito antes de aceitar tuning.

## Erro de dado ou erro de lógica?

Um campo ausente pode impedir correspondência sem que a sintaxe esteja errada. Uma duplicata pode fazer a contagem atingir o limiar. Horário de ingestão usado como horário original pode trocar a ordem. Registre a causa provável e sua evidência; a categoria operacional sozinha não explica o defeito.

| Revisão de triagem | Registro necessário |
| --- | --- |
| Evento realmente ocorreu? | Payload e identificação da fonte |
| Corresponde à condição? | Versão da lógica e comparação de campos |
| É autorizado? | Contexto independente e responsável consultado |
| Existe incerteza? | Dados faltantes e próxima verificação |
| Pode haver caso não alertado? | Teste negativo ou contraexemplo recuperado |

A amostra de alertas permite examinar precisão/classificação, mas não revela todos os falsos negativos do ambiente. Use [validação](detection-validation.md) e declare os limites do ground truth.

## Checkpoint

**Reduzir positivos benignos e reduzir falsos positivos são sempre a mesma coisa?**

<details>
<summary>Ver resposta</summary>

Não. Depende da condição definida e da nomenclatura da equipe. Preserve o comportamento realmente observado e use uma referência de classificação consistente.

</details>

[← Tópico anterior](severity-and-confidence.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](tuning.md)
