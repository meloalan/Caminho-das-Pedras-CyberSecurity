# Análise de exemplo

**Tudo nesta página é fictício. Não é evidência de um incidente executado.**

## Observações

A fixture contém cinco eventos 4625 entre 09:00 e 09:04 UTC para `lab.user`, host `LAB-WS01` e endereço de documentação reservado `192.0.2.44`. Um 4624 correspondente aparece às 09:05. Mais tarde, há processo benigno PowerShell `Get-Date`, um evento 4720 para `lab.audit-local` e uma associação ao grupo local `Lab-Auditoria`.

## Interpretação limitada

O padrão 4625 seguido de 4624 satisfaz a lógica de correlação didática. Não prova que a senha foi adivinhada nem que a sessão comprometeu o ativo. Processo PowerShell executou ação benigna. A criação e associação de conta foram rotuladas como exercício autorizado na própria fixture. A proximidade temporal não prova que os eventos tenham a mesma causa.

## ATT&CK candidato

`T1059.001` pode descrever execução de PowerShell observada, mas intenção adversária não está sustentada. `T1136.001` pode descrever a criação local porque a fixture especifica host independente e conta local. Essa conclusão depende do contexto sintético declarado. As falhas de login só apoiariam `T1110.001` se contexto adicional sustentasse password guessing; o exemplo não exige essa inferência.

## Lacunas e melhorias

O dataset não inclui política de autorização, evento de sistema de identidade, conteúdo de PowerShell logging nem cobertura de outros hosts. Em ambiente real, verificar fonte, schema, timezone, atraso, população e mudança aprovada. Não tomar decisão de contenção com base nesta fixture.

## Resultado

O exercício mostra consultas possíveis e limites de mapping. Não declara SIEM instalado, regra testada ou cobertura medida.
