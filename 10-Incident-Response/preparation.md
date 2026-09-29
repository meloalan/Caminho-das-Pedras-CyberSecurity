# Preparation: preparação

[← Índice do módulo](README.md) · [Página principal](../README.md) · [Papéis e responsabilidades →](roles-and-responsibilities.md)

Preparação reduz o tempo perdido durante um incidente e esclarece autoridade. Govern, Identify e Protect do CSF 2.0 sustentam a preparação e a redução de risco, mas o trabalho de preparação permanece contínuo.

## Pessoas e processos

- Mantenha contatos primários e suplentes, canal alternativo e verificação de identidade.
- Defina quem classifica, coordena, aprova contenção, aceita risco, comunica e encerra.
- Identifique donos e substitutos dos serviços críticos.
- Documente critérios de evento, alerta, investigação, incidente e crise.
- Mantenha playbooks, escalonamento, comunicação, coleta, handoff e revisão pós-incidente.

## Tecnologia, acesso e evidência

Conheça cobertura, retenção, relógios e acesso às fontes de identidade, endpoint, rede, cloud, email e aplicações usadas pela organização. Mapeie SIEM, EDR/XDR, ticketing, backups e ferramentas forenses quando aplicável. Defina acesso de emergência com MFA e auditoria, canal alternativo e armazenamento seguro de evidências. Nunca coloque credenciais no repositório.

## Continuidade e exercícios

Mapeie dependências, donos, RTO/RPO aprovados e ordem de recuperação. Exercite restauração em ambiente controlado. Tabletop testa papéis e decisões; simulação técnica requer ambiente, escopo e autorização próprios. Revise após mudanças e converta lacunas em ações com dono e teste de eficácia.

## Durante o incidente é tarde para descobrir que...

Ninguém sabe quem autoriza bloquear conta; o dono do servidor não tem suplente; logs já expiraram; backup nunca foi restaurado; contato do provedor está desatualizado; acesso emergencial não funciona; canal corporativo é o único e pode estar comprometido; ou ninguém sabe quem avalia impacto em dados pessoais. Esses itens devem ser tratados como lacunas concretas, não como surpresa inevitável.

## Checklist

- [ ] Responsáveis, suplentes e autoridade documentados.
- [ ] Contatos e canal alternativo exercitados.
- [ ] Serviços críticos e dependências mapeados.
- [ ] Cobertura, retenção e relógios das fontes conhecidos.
- [ ] Acesso de emergência testado e auditado.
- [ ] Evidência protegida por processo e acesso mínimo.
- [ ] Backup restaurado em teste controlado.
- [ ] Playbooks e escalonamento exercitados.
- [ ] Ações de melhoria têm dono e verificação.

## Prática e entrega

Para o cenário fictício `LAB-EXEC`, localize aprovador, equipe IAM, dono de aplicação, fonte de sessões, canal alternativo e caminho para preservar registros. Identifique lacunas sem presumir que o alerta confirma comprometimento. Entrega: mapa de papéis e dependências, relacionado ao [modelo de incidente](TEMPLATE-INCIDENTE.md).

---

[← Índice do módulo](README.md) · [Página principal](../README.md) · [Papéis e responsabilidades →](roles-and-responsibilities.md)
