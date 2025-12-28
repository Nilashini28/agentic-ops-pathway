# -*- coding: utf-8 -*-
import time
import random

def generate_log():
    return {
        "service": "auth-service",
        "latency_ms": random.randint(100, 800)
    }

if __name__ == "__main__":
    while True:
        log = generate_log()
        print(log)
        time.sleep(2)
