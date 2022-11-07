# <img src="../../assets/img/kafka.png" width="30px"> **Kafka** - ***Producers*** `CLI` 🏭

***Refer back to the theories section for more information on producers.***

## **Description** 👀

`Produce` data for a `topic`. This is the most common way to write data to `Kafka`. It reads data from standard input and sends it to the `Kafka cluster`.

<br />

## **Basic** `Commands` 📝

* **produce** data to a `topic`

  ```bash
    kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first_topic 
    >Hello World
    >My name is Guerrero
    >I love learning new things 
    ```

  * `Ctrl + C` is  used to exit the producer

<br>

* **produce** data to a `topic` with properties

    ```bash
    kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first_topic --producer-property acks=all
    > some message that is acked
    > just for fun
    > fun learning!
    ```

<br>

* **produce** to a `topic` that **does not exist**

    ```bash
    kafka-console-producer.sh --bootstrap-server localhost:9092 --topic new_topic
    > hello world!
    ```

  * by default, `Kafka` will create a `topic` if it does not exist

  * the new topic only has one partition

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --list
    ```

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --topic new_topic --describe
    ```

    * output

        ```bash
         🚀  kafka-zero-to-pro ➜ kafka-topics.sh --bootstrap-server localhost:9092 --topic new_topic --describe
        Topic: new_topic        TopicId: gKHMWVz-Q9a51Zs0wezdNg PartitionCount: 1       ReplicationFactor: 1    Configs: segment.bytes=1073741824
        Topic: new_topic        Partition: 0    Leader: 1       Replicas: 1     Isr: 1
        ```

      * by default, `Kafka` will create a `topic` with a **single** `partition` and a `replication factor` of **one**
        * to edit the default settings, edit `config/server.properties` or `config/kraft/server.properties`

            ```bash
            num.partitions=3
            ```

        * produce to another non existing topic

            ```bash
            kafka-console-producer.sh --bootstrap-server localhost:9092 --topic new_topic_2
            > hello world again!
            ```

        * this time the topic has 3 partitions

            ```bash
            kafka-topics.sh --bootstrap-server localhost:9092 --topic new_topic_2 --describe
            ```

            ```bash
            Topic: new_topic_2      TopicId: 5Q3Z2ZzvQXq2Z2Z2Z2Z2Zg PartitionCount: 3       ReplicationFactor: 1    Configs: segment.bytes=1073741824
            Topic: new_topic_2      Partition: 0    Leader: 1       Replicas: 1     Isr: 1
            Topic: new_topic_2      Partition: 1    Leader: 1       Replicas: 1     Isr: 1
            Topic: new_topic_2      Partition: 2    Leader: 1       Replicas: 1     Isr: 1
            ```

            * even though `Kafka` provides this functionality, its best to **create** `topics` before producing to them!

<br>


* **produce** to a `topic` with a **key**

    ```bash
    kafka-console-producer --bootstrap-server localhost:9092 --topic first_topic --property parse.key=true --property key.separator=:
    >example key:example value
    >name:Guerrero
    ```

<br />

<!-- 
## **Examples** 🧩

<br />
-->

[↩️](../README.md)
