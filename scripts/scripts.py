import json
import random


def generate_random_metrics():
    hw_types = ["hw_type_1", "hw_type_2", "hw_type_3", "hw_type_4"]

    json_results = []
    for hw_type in hw_types:
        for i in range(500):
            occurrence = {
                "scenario": f"scenario_{i}_{hw_type}",
                "cpu_consumption": round(random.uniform(0.1, 99.9), 2),
                "cpu_mean": round(random.uniform(0.1, 99.9), 2),
                "cpu_calculator": round(random.uniform(0.1, 99.9), 2),
                "memory_consumption": round(random.uniform(0.1, 99.9), 2),
                "hw_type": hw_type,
            }
            json_results.append(occurrence)

    json_results = json.dumps(json_results, indent=2)
    with open("metrics.json", "w") as file:
        file.write(json_results)


if __name__ == "__main__":
    generate_random_metrics()
