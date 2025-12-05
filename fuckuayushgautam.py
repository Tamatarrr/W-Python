import time
import random
import sys

def fake_progress(task, duration=3):
    print(f"{task}...")
    for i in range(1, 101):
        time.sleep(duration / 100)
        sys.stdout.write(f"\r[{i}%] {task}")
        sys.stdout.flush()
    print("\n")

def dramatic_pause():
    time.sleep(random.uniform(0.6, 1.2))

def main():
    print("Initializing Ultra-Mega-Quantum System…")
    dramatic_pause()
    
    fake_progress("Calibrating nonsense parameters", 2)
    fake_progress("Calculating useless metrics", 2)
    fake_progress("Overclocking sarcasm module", 1.5)

    print("\n⚠️  WARNING: Consuming too much oxygen in the room!")
    dramatic_pause()
    print("⚠️  WARNING: Your brain is 73% slower than recommended!")
    dramatic_pause()
    print("⚠️  ALERT: Dalla detected.")
    dramatic_pause()
    print()

    messages = [
        "Scanning for brain… (none found)",
        "Go learn some coding bitch",
        "Downloading some skill for coding…..",
        "Searching Database for optimised skillset",
        "Throws error at line 69, No optimal database found : Error message- Maa chuda le na bhosdkk",
    ]

    for msg in messages:
        print(msg)
        time.sleep(4)

if __name__ == "__main__":
    main()
