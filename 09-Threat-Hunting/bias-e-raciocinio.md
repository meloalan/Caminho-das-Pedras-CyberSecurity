# Vieses e raciocínio investigativo

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](hipoteses.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](scoping.md)

## Evidência antes da narrativa

| Viés | Erro prático | Contramedida verificável |
| --- | --- | --- |
| Confirmation bias | Buscar somente sinais que apoiam abuso | Escrever antecipadamente evidências que enfraqueceriam a hipótese |
| Anchoring | A primeira ocorrência de PowerShell vira a explicação de tudo | Reavaliar a hipótese após cada fonte nova |
| Availability bias | Supor o incidente recém-noticiado em qualquer ambiente | Comparar relevância local, ativos e comportamento observável |
| Tunnel vision | Ignorar identidades e hosts que não cabem na narrativa | Registrar exclusões e revisar com outra pessoa |

## Aplicação ao caso

E06 registra PowerShell; E07 registra uma consulta DNS; E08 registra uma conexão. A mesma execução está representada, mas não temos comandos interativos posteriores nem resposta DNS. Dizer “baixou malware daquele domínio” adicionaria fatos não disponíveis.

Mantenha quatro colunas no journal: observação, hipótese, evidência discriminante e limite. Não aumente confiança porque várias queries retornaram o mesmo registro. Fontes derivadas de um mesmo evento não são necessariamente corroboradores independentes.

## Teste adversarial do próprio raciocínio

1. Escreva a melhor explicação legítima compatível com o que viu.
2. Escreva a melhor explicação indevida ainda possível.
3. Identifique um dado capaz de diferenciá-las.
4. Se esse dado não existe, registre inconclusivo para a intenção.
5. Peça revisão da conclusão, especialmente quando houver impacto operacional.

Prática: compare “houve uma execução” e “houve abuso”. Marque exatamente qual fonte sustentaria a segunda frase. Uma assinatura válida ou uma ferramenta comum também não garantem legitimidade.

## Checkpoint

**Três dashboards mostrando o mesmo evento triplicam a confiança?**

<details>
<summary>Ver resposta</summary>

Não. É preciso avaliar independência, qualidade e alcance das fontes, não contar visualizações repetidas.

</details>

[← Tópico anterior](hipoteses.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](scoping.md)
