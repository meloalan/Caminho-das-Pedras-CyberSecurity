# DNS

[← Índice do módulo](README.md) · [Página principal](../README.md)

## Conceito

DNS relaciona nomes a registros como A, AAAA, CNAME e MX. Cache e TTL influenciam respostas. Consulta incomum pode refletir software legítimo; domínio isolado não prova comprometimento.

## Prática orientada

Use `Resolve-DnsName example.com` ou `nslookup example.com`. Compare tipos de registro e TTL. Separe resolução DNS de conectividade com o serviço.

## Entrega para o portfólio

Tabela de consultas e limites: cache, resolvedor utilizado e ausência de visibilidade sobre DNS cifrado.

## Critério de conclusão

Explique o resultado com suas palavras, registre as limitações e diferencie o que foi observado do que foi inferido. Dados de laboratório devem ser anonimizados antes da publicação.
