# <img src="../../assets/img/kafka.png" width="30px"> **Kafka** - ***Topics*** `CLI` 🚿

***Refer back to the theories section for more information on topics.***

## **Description** 👀

Used for `Kafka` topic management. (i.e create, delete, list, describe, etc.)

<br />

## **Basic** `Commands` 📝

* get help for `kafka-topics`

    ```bash
    kafka-topics --help
    ```

* **list** all `topics` in the cluster

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --list
    ```

  * `--bootstrap-server` is the `Kafka broker` to connect to

* **create** a `topic`

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --create --topic first_topic
    ```

* **create** a `topic` with a `partition` count of `3`

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --create --topic second_topic --partitions 3
    ```

* **create** a `topic` with a `partition` count of `3` and a `replication factor` of `2`

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --create --topic third_topic --partitions 3 --replication-factor 2
    ```

  * will error since the `replication factor` is greater than the number of `brokers` available

* **create** a `topic` with a `partition` count of `3` and a `replication factor` of `1`

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --create --topic third_topic --partitions 3 --replication-factor 1
    ```

  * now it works since we only have 1 `broker` running and the `replication factor` is less than or equal to the number of `brokers` available

* **describe** a `topic`

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic third_topic
    ```

  * output

    ```shell
    🚀  kafka-zero-to-pro ➜ kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic third_topic
    Topic: third_topic      TopicId: ePbXIDTPToa3OP2q_UAqYw PartitionCount: 3       ReplicationFactor: 1    Configs: segment.bytes=1073741824
    Topic: third_topic      Partition: 0    Leader: 1       Replicas: 1     Isr: 1
    Topic: third_topic      Partition: 1    Leader: 1       Replicas: 1     Isr: 1
    Topic: third_topic      Partition: 2    Leader: 1       Replicas: 1     Isr: 1
    ```

* **delete** a `topic`

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic first_topic
    ```

<br />

[↩️](../README.md)
