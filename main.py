import time
import random
from simple_analyzer.analyzer import Analyzer

def read_config(path="simple_analyzer/config/config.txt"):
    config = {}
    with open(path, "r") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=")
                config[key] = int(value)
    return config

if __name__ == "__main__":
    cfg = read_config()
    interval = cfg["interval"]
    seq_len = cfg["sequence_length"]

    analyzer = Analyzer()

    print("Starting Simple Analyzer...")
    while True:
        num = random.randint(1, 100)
        analyzer.add_number(num)

        if len(analyzer.numbers) > seq_len:
            analyzer.numbers.pop(0)

        print(f"\nNew number: {num}")
        print(f"Even count: {analyzer.even_count()}")
        print(f"Odd count: {analyzer.odd_count()}")
        print(f"Highest number: {analyzer.highest_number()}")
        print(f"Increasing pairs: {analyzer.increasing_pairs()}")                       
        current_time = time.localtime()
        if len(analyzer.numbers) >= seq_len and current_time.tm_sec == 0:
            print("Sequence full and minute reached — stopping.")
            break

        time.sleep(interval)

