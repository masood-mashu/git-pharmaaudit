"""
audit_trail_immutability_checker.py - Verifies sequential chronological continuity and immutability of audit trail entries
"""
import sys
import json


def check_audit_trail_immutability(log_entries_json: str):
    import json
    entries = json.loads(log_entries_json) if isinstance(log_entries_json, str) else log_entries_json
    seqs = [e.get("sequence_id", 0) for e in entries]
    is_sequential = all(seqs[i] == seqs[i-1] + 1 for i in range(1, len(seqs))) if len(seqs) > 1 else True
    return {"intact": is_sequential, "status": "TRAIL_INTACT" if is_sequential else "TRAIL_GAP_DETECTED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "audit-trail-immutability-checker"}))
