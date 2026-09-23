# Pendências de evolução

[← Voltar para página principal](README.md)

## Evidência e validação

- [ ] Executar os seis roteiros em ambiente autorizado.
- [ ] TODO: adicionar evidência real do laboratório em cada lab e query.
- [ ] Registrar versões, auditoria efetiva, canais, campos e configuração de coleta.
- [ ] Executar queries em Log Analytics e confrontar saída com eventos originais.
- [ ] Validar limites, duplicatas, nulos, atraso e custo da correlação antes de agendar regra.
- [ ] Converter e testar Sigma no backend escolhido.
- [ ] Preencher resultado obtido e aprendizados somente após execução.
- [ ] Adicionar capturas anonimizadas em assets/images.

## Próximos três labs sugeridos

1. **Adição a grupo privilegiado:** eventos 4732 (grupo local), 4728 (global) e 4756 (universal), distinguindo escopo e mudança autorizada.
2. **PowerShell Script Block Logging:** configurar e investigar 4104, comparar conteúdo de script com Sysmon 1 e revisar dados sensíveis.
3. **Autenticação Entra ID:** ingerir SigninLogs quando disponível, investigar falhas e MFA e comparar esquema com autenticação Windows.

Estes três labs são propostas, ainda não implementados. A prioridade imediata é executar e documentar os seis roteiros já disponíveis.
