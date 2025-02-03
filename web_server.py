import json
from bson import ObjectId
from aiohttp import web
from pymongo import MongoClient

mongo_uri = "mongodb://root:example@mongo:27017/"


def convert_objectid(document):
    if isinstance(document, list):
        return [convert_objectid(item) for item in document]
    elif isinstance(document, dict):
        return {key: convert_objectid(value) for key, value in document.items()}
    elif isinstance(document, ObjectId):
        return str(document)
    return document


async def retrieve_metrics(request):
    hw_type = request.match_info.get("hw_type")
    results = []
    try:
        client = MongoClient(mongo_uri)
        db = client["metrics_db"]
        collection = db["metrics_collection"]
        query = {"hw_type": hw_type}
        cursor = collection.find(query)
        results = list(cursor)
        results = convert_objectid(results)
    except Exception as e:
        print(f"Error: {e}")
        return web.json_response({"error": str(e)}, status=500)

    return web.json_response(results)


async def store_metrics(request):
    try:
        with open("metrics.json", "r") as f:
            json_result = json.load(f)

        client = MongoClient(mongo_uri)
        db = client["metrics_db"]
        collection = db["metrics_collection"]
        collection.insert_many(json_result)
        return web.json_response({"message": "Content stored successfully"}, status=200)
    except Exception as e:
        return web.json_response({"error": str(e)})


async def retrieve_hw_type_keys(request):
    hw_type_keys = []
    try:
        client = MongoClient(mongo_uri)
        db = client["metrics_db"]
        collection = db["metrics_collection"]
        cursor = collection.find()
        results = list(cursor)
        for result in results:
            if result["hw_type"] not in hw_type_keys:
                hw_type_keys.append(result["hw_type"])
        return web.json_response({"hw_type_keys": hw_type_keys}, status=200)
    except Exception as e:
        print(f"Error: {e}")
        return web.json_response({"error": str(e)}, status=500)


app = web.Application()
app.router.add_get("/metrics/{hw_type}", retrieve_metrics)
app.router.add_get("/metrics/hw_type", retrieve_hw_type_keys)
app.router.add_post("/metrics", store_metrics)

if __name__ == "__main__":
    web.run_app(app)
