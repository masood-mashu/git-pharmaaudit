"""
sop_version_controller.py - Confirms that manufacturing batch execution used current effective SOP revision
"""
import sys
import json


def verify_sop_version(sop_meta_json: str):
    import json
    data = json.loads(sop_meta_json) if isinstance(sop_meta_json, str) else sop_meta_json
    exec_v = data.get("executed_version", "2.0")
    curr_v = data.get("current_effective_version", "2.0")
    is_current = (exec_v == curr_v)
    return {"is_current": is_current, "status": "SOP_CURRENT" if is_current else "SOP_OUTDATED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "sop-version-controller"}))
