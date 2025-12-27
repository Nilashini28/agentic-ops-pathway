# -*- coding: utf-8 -*-
import time
from agents.observation import observe
from agents.diagnosis import diagnose
from data_simulator import generate_log

if __name__ == "__main__":
    while True:
        log_entry = generate_log()
        observation = observe(log_entry)
        diagnosis = diagnose(observation)

        print("Log:", log_entry)
        print("Observation:", observation)
        print("Diagnosis:", diagnosis)
        print("-" * 50)

        time.sleep(2)
