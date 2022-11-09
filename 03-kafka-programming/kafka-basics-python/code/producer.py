from json import dumps
from kafka import KafkaProducer


def send_message(producer, topic, message=None):
    if message is not None:
        future = producer.send(topic, message)
        future.get(timeout=60)


def run(brokers):
    producer = KafkaProducer(
        # default is localhost:9092, but we can specify multiple brokers
        bootstrap_servers=brokers,
        # how the data should be serialized before sending to the broker
        value_serializer=lambda x: dumps(x).encode("utf-8"),
    )
    return producer


if __name__ == "__main__":
    producer = run(["localhost:9092"])
    while True:
        try:
            line = input()
            send_message(producer, "third_topic", line)
        except KeyboardInterrupt:
            break
    producer.flush()
    producer.close()
