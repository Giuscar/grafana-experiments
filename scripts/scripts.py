import argparse
import json
import random
import asyncio
from pymongo import MongoClient


def generate_random_metrics(create_file=True):
    hw_types = ["hw_type_1", "hw_type_2", "hw_type_3", "hw_type_4"]

    json_results = []
    for hw_type in hw_types:
        for i in range(500):
            occurrence = {
                "scenario": f"scenario_{i}_{hw_type}",
                "cpu_consumption": round(random.uniform(0.1, 99.9), 2),
                "cpu_avg_consumption": round(random.uniform(0.1, 99.9), 2),
                "memory_consumption": round(random.uniform(0.1, 99.9), 2),
                "hw_type": hw_type,
            }
            json_results.append(occurrence)

    if create_file:
        with open("metrics.json", "w") as file:
            file.write(json.dumps(json_results, indent=2))
    print("Done")
    return json_results


def store_metrics_in_mongo(metrics):
    db_uri = "mongodb://root:example@mongo:27017"
    client = MongoClient(db_uri)
    db = client["metrics_db"]
    collection = db["metrics_collection"]
    try:
        collection.insert_many(metrics)
        print("Metrics stored successfully")
    except Exception as e:
        print(f"Error storing metrics in MongoDB: {e}")


def main():
    parser = argparse.ArgumentParser(description="Script for grafana-experiments")
    parser.add_argument(
        "-g", "--generate_random_metrics", action="store_true", help="Generate a json file containing random metrics"
    )
    parser.add_argument(
        "-j", "--store_metrics_in_json_file", action="store_true", help="Store metrics in a json file"
    )
    parser.add_argument("-s", "--store_metrics_in_mongo", action="store_true", help="Store metrics in mongo db")

    args = parser.parse_args()
    metrics = {}
    if args.generate_random_metrics:
        create_file = True if args.store_metrics_in_json_file else False
        metrics = generate_random_metrics(create_file)
    if args.store_metrics_in_mongo and metrics:
        store_metrics_in_mongo(metrics)


if __name__ == "__main__":
    main()
