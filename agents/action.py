# -*- coding: utf-8 -*-

def act(diagnosis_result):
    """
    Action agent that simulates remediation based on diagnosis.
    """
    if diagnosis_result.get("severity") == "high":
        return {
            "action": "Auto-scale service",
            "status": "Action triggered"
        }

    return {
        "action": "No action required",
        "status": "System stable"
    }
