# Playbook — Falhas de autenticação

[← Playbooks](README.md) · [Página principal](../README.md)

## Entrada

Alerta ou consulta de 4625; priorizar quando há repetição e sucesso posterior. Use a [query de correlação](../queries/kql/04-falhas-seguidas-sucesso.md).

## Investigação

1. Validar canal, provedor, intervalo UTC e integridade da coleta.
2. Identificar conta alvo, host de destino, IP, LogonType e códigos de falha.
3. Verificar ordem temporal: o sucesso é posterior e tem a mesma chave? Há NAT, proxy ou campos vazios?
4. Consultar mudança autorizada, senha expirada e serviços com credenciais antigas.
5. Buscar atividades posteriores e outros hosts afetados; registrar o que ainda não é conhecido.

## Decisão e escalonamento

Atividade autorizada confirmada: registrar evidência e possível ajuste restrito. Suspeita consistente, conta privilegiada ou impacto: escalar ao responsável com cronologia. Dados insuficientes: manter inconclusivo e solicitar a fonte faltante. Bloqueio ou isolamento exige autoridade operacional e avaliação de impacto.

## Saída

Resumo, entidades anonimizadas, fatos, hipótese, impacto, decisão, responsável e próxima revisão. Preservar evidências brutas em local privado; a publicação deve conter apenas material revisado.
