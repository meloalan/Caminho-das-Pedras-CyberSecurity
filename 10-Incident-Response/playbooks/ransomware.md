# Playbook: suspeita de ransomware

[← Playbooks](README.md) · [↑ Módulo 10](../README.md) · [Página principal](../../README.md)

Este guia coordena defesa e continuidade; não contém código ou instrução para criar ou executar ransomware. Sinais de criptografia ou indisponibilidade em massa podem exigir escalonamento imediato. Valide o sinal sem atrasar proteção quando dano ativo for plausível.

## Primeiras prioridades

- Acione autoridade e coordenação conforme política de incidente grave.
- Mobilize segurança, infraestrutura, rede, identidade, continuidade, donos dos serviços e jurídico/privacidade conforme aplicável.
- Determine o que está indisponível, o que está sendo alterado, sistemas críticos e dependências.
- Considere limitar comunicação entre segmentos ou isolar sistemas com aprovador. Evite desligar indiscriminadamente, pois pode interromper serviços ou eliminar evidência.
- Preserve registros, notas de resgate e amostras conforme procedimento. Não envie amostras ou dados a serviços públicos sem autorização.
- Proteja credenciais e canais administrativos potencialmente afetados usando equipe autorizada.

## Escopo e recuperação

Mapeie hosts, identidades, compartilhamentos, serviços, backups e janela. Distinga dano confirmado de capacidade potencial. Valide backup em ambiente controlado, integridade, data, escopo e se a causa foi removida antes de restaurar. Priorize serviços com donos e continuidade. A decisão sobre extorsão, comunicação, obrigação legal ou pagamento pertence às autoridades organizacionais competentes, com assessoria apropriada.

## Encerramento

Documente impactos, dependências, evidências, decisões, serviços restaurados, critérios de validação, monitoramento e risco residual. O [lab 11](../labs/lab-11-incidente-completo.md) traz uma variação sintética de indisponibilidade e recuperação.

---

[← Playbooks](README.md) · [↑ Módulo 10](../README.md) · [Página principal](../../README.md)
