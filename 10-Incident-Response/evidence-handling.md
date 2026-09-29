# Tratamento de evidências

[← Contenção](containment.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Erradicação →](eradication.md)

Evidência permite sustentar ou refutar hipótese e explicar decisões. Uma coleta precisa ser autorizada, proporcional, protegida e documentada. Logs exportados para triagem não são automaticamente uma aquisição forense formal. Se houver potencial de processo jurídico, regulatório, disciplinar ou de privacidade, acione especialistas e siga política, orientação jurídica e requisitos de jurisdição.

## Preservar e proteger

- Registre fonte, proprietário, período, query ou método de exportação, operador, horário e fuso.
- Preserve o original quando possível e trabalhe em cópia. Documente transformações, filtros, conversões e limitações.
- Restrinja acesso por necessidade, criptografe armazenamento e use transferência aprovada.
- Registre integridade por mecanismo aprovado, por exemplo hash criptográfico, quando adequado. Hash ajuda a detectar alteração do arquivo, mas não prova origem, completude nem autenticidade do evento.
- Mantenha cadeia de custódia de acordo com política aplicável: identificador, quem transferiu, quem recebeu, quando, onde e finalidade.
- Minimize dados pessoais e conteúdo sem relação com o caso. Não publique evidência real em repositório ou portfólio.

## Evidência volátil e ações urgentes

Algumas ações podem alterar sessão, memória, processo ou estado do sistema. Em situação urgente, segurança e continuidade podem exigir contenção imediata. Quando o tempo e a autoridade permitirem, envolva DFIR antes de ação que possa destruir informação volátil. Se agir primeiro, documente a condição, a urgência, quem autorizou, quais dados podem ter sido alterados e que fontes alternativas permaneceram.

Não realize aquisição ou intervenção em sistema real sem escopo e autorização explícitos. Este material não ensina coleta forense especializada nem substitui treinamento e procedimento de resposta a incidentes.

## Registro de item

| Campo | Exemplo fictício |
| --- | --- |
| ID | `EVID-LAB-004` |
| Descrição | Exportação sintética de eventos do IdP para o caso `CASE-LAB-101`. |
| Origem e dono | IdP de laboratório, custodiante LAB. |
| Período/fuso | 2026-09-29 00:00 a 02:00 UTC. |
| Coletor/método | Analista LAB, exportação somente leitura do conjunto fictício. |
| Integridade | SHA-256 de exemplo gerado no exercício; não representa autenticidade da origem. |
| Armazenamento/acesso | Diretório didático controlado, acesso restrito ao grupo LAB. |
| Transferências | Sem transferência no exercício. |
| Limitações | Dataset incompleto e criado para treinamento. |

## Cadeia de custódia

A cadeia registra manuseio, transferência e armazenamento para permitir revisão. A forma exigida varia com finalidade, política e jurisdição. Não invente assinatura ou controle que não ocorreu. Se uma etapa não foi registrada, identifique a lacuna e peça avaliação especializada antes de afirmar admissibilidade ou integridade forense.

---

[← Contenção](containment.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Erradicação →](eradication.md)
