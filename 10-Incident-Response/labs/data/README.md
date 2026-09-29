# Dataset fictício de Incident Response

[← Labs](../README.md) · [↑ Módulo 10](../../README.md) · [Página principal](../../../README.md)

`incident-events.jsonl` é um conjunto pequeno, deliberadamente incompleto, para treino de timeline, triagem e scoping. Cada linha é um JSON independente. Nenhum evento descreve uma organização ou pessoa real. Não contém malware, credenciais ou payload ofensivo.

## Convenções

- Entidades usam prefixo `LAB`.
- Domínio usa `example.com`.
- IPv4 usa faixas reservadas para documentação conforme RFC 5737: `192.0.2.0/24`, `198.51.100.0/24` e `203.0.113.0/24`.
- Hashes são rótulos inventados com aparência hexadecimal, não indicadores verificáveis.
- `event_time` e `ingestion_time` podem divergir para demonstrar atraso.
- `source` identifica uma fonte lógica fictícia, sem imitar schema de produto.
- `confidence` descreve confiança de que o registro foi representado corretamente no exercício; não prova comprometimento.
- Campo ausente significa desconhecido ou fora do dataset, não “não ocorreu”.

## Limitações

Dataset não é completo, não cobre todos os sistemas e não sustenta atribuição, conclusão forense, decisão jurídica ou resposta real. Uma consulta sem resultado não prova ausência. Não envie os dados para ferramentas conectadas à produção.
