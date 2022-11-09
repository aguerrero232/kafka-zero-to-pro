# <img src="../../assets/img/kafka.png" width="30px"> **Kafka** - ***Kafka Basics***: `Python` 🛠️

## **Description** 👀

This is a simple producer and consumer program that uses the `kafka-python` library to produce and consume messages from a Kafka topic. Data is also stored in a MongoDB database.

## **Prerequisites** 📋

* python 3.7 or higher
* mongodb docker image
  * <https://hub.docker.com/_/mongo>
* kafka python library
  * <https://pypi.org/project/kafka-python/>

## **Examples** 🧩

* start up a mongodb docker container

    ```bash
    docker run -d -p 27017:27017 --name mongo mongo:latest
    ```

* start up the consumer program

    ```bash
    python consumer.py
    ```

    ```python
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
    ```

* start up the producer program

    ```bash
    python producer.py
    > test
    > hello there
    > hi there
    > ok ill try again
    ```

    * this will produce a message to the `topic`

    ```python
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
    ```

<br>

* check the mongodb database

    ```bash
    docker exec -it mongo bash
    ```

    ```bash
    mongosh
    ```

    ```bash
    use third_topic
    ```

    ```bash
    db.third_topic.find().pretty()
    ```

  * output

    ```yaml
        [
            {
                _id: ObjectId("636beacf8d55a7507a4799a1"),
                message: 'test',
                topic: 'third_topic',
                partition: 0,
                offset: 139,
                timestamp: Long("1668016844924")
            },
            {
                _id: ObjectId("636bead38d55a7507a4799a2"),
                message: 'hello there',
                topic: 'third_topic',
                partition: 1,
                offset: 133,
                timestamp: Long("1668016851536")
            },
            {
                _id: ObjectId("636bec478d55a7507a4799a3"),
                message: 'hi there',
                topic: 'third_topic',
                partition: 2,
                offset: 134,
                timestamp: Long("1668017223008")
            },
            {
                _id: ObjectId("636bed458d55a7507a4799a4"),
                message: 'ok ill try again',
                topic: 'third_topic',
                partition: 2,
                offset: 135,
                timestamp: Long("1668017477562")
            }
        ]
    ```

<br />

[↩️](../README.md)
