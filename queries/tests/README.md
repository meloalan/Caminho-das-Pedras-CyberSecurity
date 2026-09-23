# Teste sintético de correlação

[← Voltar para página principal](../../README.md)

Abra [correlacao-sintetica.kql](correlacao-sintetica.kql), copie o arquivo completo para um editor KQL compatível e execute. Não requer ingestão: o `let SecurityEvent = datatable(...)` sombreia a tabela real apenas nesta consulta. Nenhuma tentativa de autenticação é gerada.

## Como funciona

O conjunto contém 59 eventos fictícios. `OffsetMinutes` posiciona cada evento em relação a `now()`; os nomes de conta identificam cenários e os IPs pertencem ao bloco de documentação. Depois de construir os dados, o arquivo executa a mesma lógica da [query operacional](../kql/04-falhas-seguidas-sucesso.md).

| Conta/cenário | Resultado esperado | Motivo |
| --- | --- | --- |
| positivo | Uma linha, FailureCount = 5 | Cinco falhas válidas antes do sucesso |
| limite-inclusivo | Uma linha, FailureCount = 5 | Falha exatamente dez minutos antes é incluída |
| quatro-falhas | Nenhuma linha | Abaixo do limiar |
| sucesso-anterior | Nenhuma linha | Sucesso não vem depois das falhas |
| fora-da-janela | Nenhuma linha | Falhas mais antigas que dez minutos |
| ip-diferente | Nenhuma linha | Origem do sucesso difere |
| mesmo-instante | Nenhuma linha | Uma falha coincide com o sucesso, restam quatro anteriores |
| ip-vazio | Nenhuma linha | Filtro exclui chave sem origem |
| host-diferente | Nenhuma linha | Destino do sucesso difere |
| tipo-diferente | Nenhuma linha | Tipo de logon do sucesso difere |

Esperado: **duas linhas ao todo**, independentemente da ordem entre timestamps iguais. A matriz foi conferida logicamente; a execução KQL no serviço ainda está pendente.

## Interpretação e melhoria

O cenário positivo seria também compatível com um usuário legítimo errando a senha. O teste valida a seleção temporal e as chaves, não a classificação de ameaça. Acrescente duplicatas, formatos alternativos de conta e atraso de ingestão antes de transformar a query em regra agendada. Esses dados não são evidência de um ataque nem de um laboratório executado.

TODO: adicionar evidência real do laboratório
