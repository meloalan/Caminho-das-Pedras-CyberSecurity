"""Synthetic specification tests, not executions of Sigma or a SIEM engine."""
import copy
import json
import sys
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "detections/tools"))
from evaluate import account_created, correlate, tuning_report, scoped_exception


class DetectionTests(unittest.TestCase):
    def test_account_cases(self):
        cases = json.loads((ROOT / "detections/tests/account-cases.json").read_text(encoding="utf-8"))
        for case in cases:
            with self.subTest(case=case["name"]):
                self.assertEqual(account_created(case["input"]), case["expected"])

    def events(self):
        path = ROOT / "07-Buscas-e-Queries-em-SIEM/labs/dados/eventos.jsonl"
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]

    def test_thresholds(self):
        self.assertEqual([len(correlate(self.events(), n)) for n in (3, 5, 10)], [1, 0, 0])

    def test_each_threshold_boundary(self):
        baseline = self.events()
        first = next(e for e in baseline if e['id'] == 'E01')
        success = next(e for e in baseline if e['id'] == 'E04')
        for threshold in (3, 5, 10):
            for count in (threshold-1, threshold, threshold+1):
                events = [{**first, 'id': f'BOUNDARY-{i}'} for i in range(count)] + [success]
                with self.subTest(threshold=threshold, count=count):
                    self.assertEqual(len(correlate(events, threshold)), int(count >= threshold))

    def test_exception_scope_and_expiry(self):
        path = ROOT / 'detections/tests/tuning.jsonl'
        event = json.loads(path.read_text(encoding='utf-8').splitlines()[0])
        self.assertTrue(scoped_exception(event))
        for change in ({'host': 'WIN-LAB02'}, {'actor': 'svc_backup.lab'},
                       {'approved_change': None}, {'timestamp': '2026-09-28T11:00:00Z'},
                       {'timestamp': '2026-09-28T09:59:59Z'}):
            with self.subTest(change=change):
                self.assertFalse(scoped_exception({**event, **change}))

    def test_expected_identity(self):
        self.assertEqual(correlate(self.events(), 3), [{"success": "E04", "failures": ["E01", "E02", "E03"]}])

    def test_out_of_order(self):
        self.assertEqual(correlate(list(reversed(self.events())), 3), correlate(self.events(), 3))

    def test_identical_duplicate_not_counted(self):
        es = self.events(); es.append(copy.deepcopy(es[0]))
        self.assertEqual(correlate(es, 3), correlate(self.events(), 3))

    def test_conflicting_duplicate_rejected(self):
        es = self.events(); duplicate = copy.deepcopy(es[0]); duplicate["host"] = "OTHER-LAB"; es.append(duplicate)
        with self.assertRaises(ValueError):
            correlate(es, 3)

    def change(self, **fields):
        es = self.events()
        next(e for e in es if e["id"] == "E01").update(fields)
        return es

    def test_null_key(self):
        self.assertEqual(correlate(self.change(source_ip=None), 3), [])

    def test_lower_boundary_included(self):
        self.assertEqual(len(correlate(self.change(timestamp="2026-09-24T07:55:00Z"), 3)), 1)

    def test_outside_boundary_excluded(self):
        self.assertEqual(correlate(self.change(timestamp="2026-09-24T07:54:59Z"), 3), [])

    def test_equal_time_excluded(self):
        self.assertEqual(correlate(self.change(timestamp="2026-09-24T08:05:00Z"), 3), [])

    def test_late_ingestion(self):
        es = self.change(ingested_at="2026-09-24T08:15:00Z")
        self.assertEqual(correlate(es, 3, as_of="2026-09-24T08:10:00Z"), [])
        self.assertEqual(len(correlate(es, 3, as_of="2026-09-24T08:20:00Z")), 1)

    def test_tuning_tradeoff(self):
        report = tuning_report()
        self.assertEqual(report["baseline"], {"alerts": 100, "tp": 30, "fp": 70, "fn": 0, "tn": 0})
        self.assertEqual(report["broad_exception"], {"alerts": 30, "tp": 20, "fp": 10, "fn": 10, "tn": 60})
        self.assertEqual(report["scoped_exception"], {"alerts": 40, "tp": 30, "fp": 10, "fn": 0, "tn": 60})

    def test_only_synthetic(self):
        es = self.events(); es[0]["synthetic"] = False
        with self.assertRaises(ValueError):
            correlate(es, 3)

    def test_invalid_threshold(self):
        for threshold in (0, -1, True, '3'):
            with self.subTest(threshold=threshold), self.assertRaises(ValueError):
                correlate(self.events(), threshold)


if __name__ == "__main__":
    unittest.main()
