# <img src="../../assets/img/kafka.png" width="30px"> **Kafka** - ***Consumer Groups*** `CLI` 👥

***Refer back to the theories section for more information on consumer groups.***

## **Description** 👀

Used to ***divide*** `partitions` among `consumers`.

<br />

## **Basic** `Commands` 📝

* start a `consumer` in a `group`

    ```bash
    kafka-console-consumer.sh --bootstrap-server <kafka-broker> --topic <topic-name> --group <group-name>
    ```

<br />

## **Examples** 🧩

* **create** a `topic` with 3 `partitions` and 1 `replication factor`
  * its necessary to have **at least** 2 `partitions` to make use of a `consumer group`

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --create --topic third_topic --partitions 3 --replication-factor 1
    ```

* start a **consumer** in the `consumer group` **my-first-application**

    ```bash
    kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic --group my-first-application
    ```

  * start a `producer` and start **producing** `messages` to the `topic`

    ```bash
    kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first_topic
    ```

* start *another* `consumer` part of the **same** `group`
  * observe the messages being spread

    ```bash
    kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic --group my-first-application
    ```

* start *another* `consumer` part of a **different** `group` from beginning, i.e. **my-second-application**

    ```bash
    kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic --group my-second-application --from-beginning
    ```

<br />

[↩️](../README.md)
