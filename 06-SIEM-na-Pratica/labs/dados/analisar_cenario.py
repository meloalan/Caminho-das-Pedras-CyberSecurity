"""Conferência offline de observações sintéticas; não executa consultas SIEM."""

import json
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path


def instante(evento):
    return datetime.fromisoformat(evento["timestamp"].replace("Z", "+00:00"))


def chave(evento):
    campos = ("target_domain", "target_user", "host", "source_ip", "logon_type")
    valores = tuple(evento.get(campo) for campo in campos)
    return valores if all(valor not in (None, "", "-") for valor in valores) else None


def sequencias(eventos, minutos=10, minimo=3):
    """Exige chave completa, anterioridade estrita e janela inclusiva no início."""
    security = "Microsoft-Windows-Security-Auditing"
    falhas = [e for e in eventos if e["provider"] == security and e["event_id"] == 4625]
    resultado = []
    for sucesso in eventos:
        if sucesso["provider"] != security or sucesso["event_id"] != 4624:
            continue
        identidade = chave(sucesso)
        if identidade is None:
            continue
        fim = instante(sucesso)
        anteriores = [e for e in falhas if chave(e) == identidade
                      and fim - timedelta(minutes=minutos) <= instante(e) < fim]
        if len(anteriores) >= minimo:
            resultado.append((sucesso, sorted(anteriores, key=instante)))
    return resultado


def main():
    caminho = Path(__file__).with_name("cenario-final.jsonl")
    eventos = [json.loads(linha) for linha in caminho.read_text(encoding="utf-8").splitlines() if linha.strip()]
    ids = [e["id"] for e in eventos]
    if len(ids) != len(set(ids)):
        raise ValueError("IDs duplicados: revise a origem antes de contar os eventos.")
    if not all(e.get("synthetic") is True for e in eventos):
        raise ValueError("Este exercício espera somente observações sintéticas.")
    print(f"Registros: {len(eventos)}")
    for (provider, event_id), quantidade in sorted(Counter((e["provider"], e["event_id"]) for e in eventos).items()):
        print(f"{provider} / {event_id}: {quantidade}")
    candidatos = sequencias(eventos)
    print(f"Sequências candidatas: {len(candidatos)}")
    for sucesso, falhas in candidatos:
        print(f"{sucesso['id']} precedido por {len(falhas)} falhas: {', '.join(e['id'] for e in falhas)}")
        print(f"Chave (domínio, usuário, host, origem, tipo): {chave(sucesso)}")
    print("Timeline UTC:")
    for evento in sorted(eventos, key=instante):
        print(f"{evento['timestamp']} {evento['id']} {evento['host']} {evento['provider']} / {evento['event_id']}")
    print("A sequência é candidata à investigação. Não demonstra ataque nem execução nos quatro SIEMs.")


if __name__ == "__main__":
    main()
