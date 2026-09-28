"""Read-only structural checks. Does not convert rules or execute SIEM engines."""
from pathlib import Path
import json
import uuid
import xml.etree.ElementTree as ET

import yaml
from sigma.collection import SigmaCollection

ROOT = Path(__file__).resolve().parents[2]


def validate():
    specification = ROOT / "detections/windows/account-management/DET-WIN-ACCOUNT-001.yml"
    data = yaml.safe_load(specification.read_text(encoding="utf-8"))
    required = {"id", "name", "version", "status", "owner", "hypothesis", "risk", "scope",
                "data_sources", "required_fields", "logic", "severity", "confidence", "mitre",
                "false_positives", "false_negatives", "exceptions", "tests", "runbook", "health",
                "review", "retirement", "changelog"}
    if not isinstance(data, dict) or not required <= data.keys():
        raise ValueError("Educational specification is missing required sections")
    for path in [data["tests"]["fixture"], data["runbook"]]:
        if not (ROOT / path).is_file():
            raise ValueError(f"Missing referenced file: {path}")
    paths = list((ROOT / "detections/windows").rglob("*.sigma.yml"))
    paths.append(ROOT / "queries/sigma/windows-account-created.yml")
    identifiers = set()
    for path in paths:
        text = path.read_text(encoding="utf-8")
        document = yaml.safe_load(text)
        identifier = str(uuid.UUID(document["id"]))
        if identifier in identifiers:
            raise ValueError("Repeated Sigma UUID")
        identifiers.add(identifier)
        collection = SigmaCollection.from_yaml(text)
        if len(collection.rules) != 1:
            raise ValueError("Expected one Sigma rule per file")
    tree = ET.parse(ROOT / "detections/windows/account-management/wazuh-account-created.xml")
    rule = tree.getroot().find("rule")
    if not 100000 <= int(rule.attrib["id"]) <= 120000:
        raise ValueError("Custom Wazuh ID outside documented range")
    for path in (ROOT / "detections/tests").glob("*.json"):
        cases = json.loads(path.read_text(encoding="utf-8"))
        for case in cases:
            record = case.get("input", case)
            if record.get("synthetic") is not True:
                raise ValueError(f"Undeclared synthetic record in {path}")
    print(f"{len(paths)} Sigma rules parsed; specification, references, XML and JSON checked.")
    print("No backend conversion, SIEM execution, Wazuh logtest or deployment performed.")


if __name__ == "__main__":
    validate()
