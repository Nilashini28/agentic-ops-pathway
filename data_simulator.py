import time
import random

LATENCY_THRESHOLD = 700

def observation_agent():
    latency = random.randint(200, 900)
    event = {
        "service": "auth-service",
        "latency_ms": latency
    }
    print(f"[ObservationAgent] Observed metrics: {event}")
    return event

def diagnosis_agent(event):
    if event["latency_ms"] > LATENCY_THRESHOLD:
        diagnosis = {
            "issue": "High latency detected",
            "root_cause": "Possible resource saturation",
            "confidence": round(random.uniform(0.7, 0.9), 2)
        }
        print(f"[DiagnosisAgent] Diagnosis: {diagnosis}")
        return diagnosis
    return None

def planning_agent(diagnosis):
    if diagnosis:
        plan = {
            "action": "Scale auth-service",
            "risk": "Low"
        }
        print(f"[PlanningAgent] Planned action: {plan}")
        return plan
    return None

def action_agent(plan):
    if plan:
        print(f"[ActionAgent] Executing action: {plan['action']}")
        time.sleep(1)
        print("[ActionAgent] Action executed successfully")

if __name__ == "__main__":
    print("Starting real-time agentic incident response simulation...\n")

    while True:
        event = observation_agent()
        diagnosis = diagnosis_agent(event)
        plan = planning_agent(diagnosis)
        action_agent(plan)
        print("-" * 60)
        time.sleep(2)
