# -*- coding: utf-8 -*-
import time
from data_simulator import generate_log
from agents.observation import observe
from agents.diagnosis import diagnose
from agents.action import act

if __name__ == "__main__":
    while True:
        log_entry = generate_log()

        observation = observe(log_entry)
        diagnosis = diagnose(observation)
        action = act(diagnosis)

        print("Log:", log_entry)
        print("Observation:", observation)
        print("Diagnosis:", diagnosis)
        print("Action:", action)
        print("=" * 60)

        time.sleep(2)
