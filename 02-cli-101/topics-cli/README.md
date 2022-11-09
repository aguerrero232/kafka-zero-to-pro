# <img src="../../assets/img/kafka.png" width="30px"> **Kafka** - ***Topics*** `CLI` 🚿

***Refer back to the theories section for more information on topics.***

## **Description** 👀

Used for `Kafka` topic management. (i.e create, delete, list, describe, etc.)

<br />

## **Basic** `Commands` 📝

* **get** `topics` functionalities

  ```bash
  kafka-topics.sh
  ```

* **get** list of `topics`

  ```bash
  kafka-topics.sh --bootstrap-server <kafka-broker> --list
  ```

* **create** a `topic`

  ```bash
  kafka-topics.sh --bootstrap-server <kafka-broker> --topic <topic-name> --create
  ```

* **create** a `topic` with `partitions`

  ```bash
  kafka-topics.sh --bootstrap-server <kafka-broker> --topic <topic-name> --create --partitions <number-of-partitions>
  ```

* **create** a `topic` with `replication-factor`

  ```bash
  kafka-topics.sh --bootstrap-server <kafka-broker> --topic <topic-name> --create --replication-factor <replication-factor>
  ```

* **create** a `topic` with `partitions` and `replication-factor`

  ```bash
  kafka-topics.sh --bootstrap-server <kafka-broker> --topic <topic-name> --create --partitions <number-of-partitions> --replication-factor <replication-factor>
  ```

* **describe** a `topic`

  ```bash
  kafka-topics.sh --bootstrap-server <kafka-broker> --topic <topic-name> --describe
  ```

* **delete** a `topic`

  ```bash
  kafka-topics.sh --bootstrap-server <kafka-broker> --topic <topic-name> --delete
  ```

<br>

## **Examples** 🧩

* **get** help for `kafka-topics`

    ```bash
    kafka-topics --help
    ```

<br>

* **list** all `topics` in the cluster

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --list
    ```

  * `--bootstrap-server` is the `Kafka broker` to connect to

<br>

* **create** a `topic`

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --create --topic first_topic
    ```

<br>

* **create** a `topic` with a `partition` count of `3`

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --create --topic second_topic --partitions 3
    ```
<br>

* **create** a `topic` with a `partition` count of `3` and a `replication factor` of `2`

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --create --topic third_topic --partitions 3 --replication-factor 2
    ```

  * will **error** since the `replication factor` is ***greater than*** the number of `brokers` available

<br>

* **create** a `topic` with a `partition` count of `3` and a `replication factor` of `1`

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --create --topic third_topic --partitions 3 --replication-factor 1
    ```

  * now it works since the `replication factor` is ***less than or equal*** to the number of `brokers` available

<br>

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

<br>

* **delete** a `topic`

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic first_topic
    ```

<br />

[↩️](../README.md)
