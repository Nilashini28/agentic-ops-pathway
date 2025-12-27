# -*- coding: utf-8 -*-

def observe(log_entry):
    """
    Observation agent that detects simple latency anomalies.
    """
    latency = log_entry.get("latency_ms", 0)

    if latency > 500:
        return {
            "status": "anomaly",
            "reason": "High latency detected",
            "latency_ms": latency
        }

    return {
        "status": "normal",
        "latency_ms": latency
    }
