"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitPharmaAudit.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.electronic_signature_verifier import *
from tools.audit_trail_immutability_checker import *
from tools.sop_version_controller import *

class TestGitPharmaAuditPredictability(unittest.TestCase):
    def test_electronic_signature_verifier(self):
        res = verify_electronic_signature('{"signer_id": "dr_smith", "timestamp_iso": "2026-09-30T00:00:00Z", "signature_hash": "a1b2c3d4e5f678901234567890abcdef"}')
        self.assertTrue(res["signature_valid"])
        self.assertEqual(res["status"], "SIG_VERIFIED")

    def test_audit_trail_immutability_checker(self):
        res = check_audit_trail_immutability('[{"sequence_id": 1}, {"sequence_id": 2}, {"sequence_id": 3}]')
        self.assertTrue(res["intact"])
        self.assertEqual(res["status"], "TRAIL_INTACT")

    def test_sop_version_controller(self):
        res = verify_sop_version('{"executed_version": "3.1", "current_effective_version": "3.1"}')
        self.assertTrue(res["is_current"])
        self.assertEqual(res["status"], "SOP_CURRENT")


if __name__ == "__main__":
    unittest.main()
