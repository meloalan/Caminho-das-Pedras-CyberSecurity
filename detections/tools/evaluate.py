"""Reference logic for fictitious fixtures only. No SIEM deployment or Sigma execution."""
import json
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SECURITY = "Microsoft-Windows-Security-Auditing"


def instant(value):
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("Timezone is required")
    return result


def account_created(event):
    if event.get("synthetic") is not True:
        raise ValueError("Only declared synthetic input is accepted")
    match = event.get("provider") == SECURITY and event.get("channel") == "Security" and event.get("event_id") == 4720
    required = ("host", "timestamp", "actor", "actor_domain", "user", "domain")
    missing = [field for field in required if event.get(field) in (None, "", "-")]
    return {"match": match, "missing_context": missing if match else []}


def unique(events):
    found = {}
    for event in events:
        if event.get("synthetic") is not True:
            raise ValueError("Only declared synthetic input is accepted")
        identity = event["id"]
        if identity in found and found[identity] != event:
            raise ValueError("Conflicting records sharing the same ID")
        found[identity] = event
    return list(found.values())


def correlate(events, threshold=3, as_of=None):
    if not isinstance(threshold, int) or isinstance(threshold, bool) or threshold < 1:
        raise ValueError("Threshold must be a positive integer")
    cutoff = instant(as_of) if as_of else None
    ready = [e for e in unique(events) if cutoff is None or instant(e.get("ingested_at", e["timestamp"])) <= cutoff]
    def key(e):
        values = tuple(e.get(f) for f in ("domain", "user", "host", "source_ip", "logon_type"))
        return values if all(v not in (None, "", "-") for v in values) else None
    failures = [e for e in ready if e["provider"] == SECURITY and e["event_id"] == 4625]
    results = []
    for success in sorted(ready, key=lambda e: (instant(e["timestamp"]), e["id"])):
        if success["provider"] != SECURITY or success["event_id"] != 4624 or key(success) is None:
            continue
        end = instant(success["timestamp"])
        previous = sorted((e for e in failures if key(e) == key(success)
                           and end-timedelta(minutes=10) <= instant(e["timestamp"]) < end),
                          key=lambda e: (instant(e["timestamp"]), e["id"]))
        if len(previous) >= threshold:
            results.append({"success": success["id"], "failures": [e["id"] for e in previous]})
    return results


def scoped_exception(e):
    # Context is from a fictitious independently approved change register, not an event's assertion.
    return (e["actor"] == "svc_provision.lab" and e["host"] == "WIN-LAB01"
            and e["approved_change"] == "CHG-LAB-1234"
            and instant("2026-09-28T10:00:00Z") <= instant(e["timestamp"]) < instant("2026-09-28T11:00:00Z"))


def tuning_report():
    path = ROOT / "detections/tests/tuning.jsonl"
    events = unique([json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()])
    decisions = {"baseline": lambda e: True,
                 "broad_exception": lambda e: not e["actor"].startswith("svc_"),
                 "scoped_exception": lambda e: not scoped_exception(e)}
    report = {}
    for name, decision in decisions.items():
        counts = dict.fromkeys(("alerts", "tp", "fp", "fn", "tn"), 0)
        for event in events:
            if not account_created(event)["match"]:
                raise ValueError("Tuning fixture must contain account creation candidates")
            predicted, expected = decision(event), event["requires_investigation"]
            counts["alerts"] += int(predicted)
            counts["tp" if predicted and expected else "fp" if predicted else "fn" if expected else "tn"] += 1
        report[name] = counts
    return report


if __name__ == "__main__":
    print(json.dumps(tuning_report(), indent=2))
    print("Synthetic ground truth only. This does not execute a SIEM rule.")
