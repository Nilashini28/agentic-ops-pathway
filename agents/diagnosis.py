# -*- coding: utf-8 -*-

def diagnose(observation_result):
    """
    Diagnosis agent that explains the root cause of anomalies.
    """
    if observation_result["status"] == "anomaly":
        return {
            "cause": "Service overload or network delay",
            "severity": "high",
            "recommended_action": "Scale service or reroute traffic"
        }

    return {
        "cause": "No issue detected",
        "severity": "low"
    }
