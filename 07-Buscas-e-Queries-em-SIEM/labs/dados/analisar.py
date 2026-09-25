"""Analisa apenas o fixture local. Não executa linguagens ou APIs de SIEM."""

import csv
import json
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

SECURITY = "Microsoft-Windows-Security-Auditing"
SYSMON = "Microsoft-Windows-Sysmon"


def instante(evento):
    return datetime.fromisoformat(evento["timestamp"].replace("Z", "+00:00"))


def chave(evento):
    valores = tuple(evento.get(c) for c in ("domain", "user", "host", "source_ip", "logon_type"))
    return valores if all(v not in (None, "", "-") for v in valores) else None


def resumir(eventos, inventario):
    ids = [e["id"] for e in eventos]
    if len(ids) != len(set(ids)):
        raise ValueError("ID duplicado no fixture: confira as ocorrências antes de contar.")
    if not all(e.get("synthetic") is True for e in eventos):
        raise ValueError("Este exercício aceita apenas dados fictícios declarados.")
    inicio = datetime(2026, 9, 24, tzinfo=timezone.utc)
    fim = inicio + timedelta(days=1)
    atuais = sorted((e for e in eventos if inicio <= instante(e) < fim), key=instante)
    falhas = [e for e in eventos if e["provider"] == SECURITY and e["event_id"] == 4625]
    falhas_atuais = [e for e in atuais if e["provider"] == SECURITY and e["event_id"] == 4625]
    sequencias = []
    for sucesso in atuais:
        if sucesso["provider"] != SECURITY or sucesso["event_id"] != 4624 or chave(sucesso) is None:
            continue
        tempo = instante(sucesso)
        anteriores = sorted((e for e in falhas if chave(e) == chave(sucesso)
                             and tempo - timedelta(minutes=10) <= instante(e) < tempo), key=instante)
        if len(anteriores) >= 3:
            sequencias.append({"sucesso": sucesso["id"], "falhas": [e["id"] for e in anteriores]})
    observados = {e["host"] for e in atuais}
    guid = "{11111111-2222-3333-4444-555555555555}"
    return {
        "total": len(eventos),
        "atuais": len(atuais),
        "falhas": len(falhas_atuais),
        "falhas_por_host": dict(sorted(Counter(e["host"] for e in falhas_atuais).items())),
        "falhas_por_identidade": dict(sorted(Counter(f"{e.get('domain')}/{e.get('user')}" for e in falhas_atuais).items())),
        "sequencias_candidatas": sequencias,
        "sysmon_processos_atuais": [e["id"] for e in atuais if e["provider"] == SYSMON and e["event_id"] == 1],
        "pivot_processo": [e["id"] for e in atuais if e["provider"] == SYSMON and e["host"] == "WIN-LAB01" and e.get("process_guid") == guid],
        "hosts_sem_registros": sorted({e["host"] for e in inventario} - observados),
        "timeline_atual": [e["id"] for e in atuais],
    }


def main():
    pasta = Path(__file__).resolve().parent
    eventos = [json.loads(linha) for linha in (pasta / "eventos.jsonl").read_text(encoding="utf-8").splitlines() if linha.strip()]
    with (pasta / "inventario.csv").open(encoding="utf-8", newline="") as arquivo:
        inventario = list(csv.DictReader(arquivo))
    print(json.dumps(resumir(eventos, inventario), ensure_ascii=False, indent=2))
    print("Resultado offline sobre dados fictícios. Sequência não comprova ataque; ausência não comprova falha de coleta.")


if __name__ == "__main__":
    main()
