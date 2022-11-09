from kafka import KafkaConsumer
from json import loads
from pymongo import MongoClient


consumer = KafkaConsumer(
    "third_topic",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="my-first-group",
    value_deserializer=lambda x: loads(x.decode("utf-8")),
)


my_client = MongoClient("mongodb://localhost:27017")

try:
    my_db = my_client["third_topic"]
    my_collection = my_db["third_topic"]
except Exception as e:
    print(e)

for message in consumer:
    print(f"{message.value}")
    j_msg = {
        "message": message.value,
        "topic": message.topic,
        "partition": message.partition,
        "offset": message.offset,
        "timestamp": message.timestamp,
    }
    try:
        my_collection.insert_one(j_msg)
    except Exception as e:
        print(e)
