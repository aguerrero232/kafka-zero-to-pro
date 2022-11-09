# <img src="../../assets/img/kafka.png" width="30px"> **Kafka** - ***Consumer Groups*** `CLI` 👥

***Refer back to the theories section for more information on consumer groups.***

## **Description** 👀

Used to ***divide*** `partitions` among `consumers`.

<br />

## **Basic** `Commands` 📝

* **start** a `consumer` in a `consumer group`

    ```bash
    kafka-console-consumer.sh --bootstrap-server <kafka-broker> --topic <topic-name> --group <group-name>
    ```

* **describe** a `consumer group`

    ```bash
    kafka-consumer-groups.sh --bootstrap-server <kafka-broker> --group <group-name> --describe
    ```

* **reset** a `consumer group` to `earliest` offset to the earliest offset

    ```bash
    kafka-consumer-groups.sh --bootstrap-server <kafka-broker> --group <group-name> --reset-offsets --to-earliest --execute --topic <topic-name>
    ```

  * the `--topic` flag is needed if the `consumer group` is consuming from multiple `topics`  
    * you can use `--all-topics` instead of `--topic` to reset all `topics` in the `consumer group`

  * the `--execute` flag is ***required*** to actually reset the offsets


* **shift** the `consumer group` offset by `n` messages

    ```bash
    kafka-consumer-groups.sh --bootstrap-server <kafka-broker> --group <group-name> --reset-offsets --shift-by <number-of-messages> --execute --topic <topic-name>
    ```

    * `shift-by` can be a ***negative*** number to shift the offset ***backwards*** by `n` messages

<br />

## **Examples** 🧩

* **create** a `topic` with 3 `partitions` and 1 `replication factor`
  * its necessary to have **at least** 2 `partitions` to make use of a `consumer group`

    ```bash
    kafka-topics.sh --bootstrap-server localhost:9092 --create --topic first_topic --partitions 3 --replication-factor 1
    ```

* start a `consumer` in the `consumer group` **my-first-application**

    ```bash
    kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic --group my-first-application
    ```

  * start a `producer` and start **producing** `messages` to the `topic`

    ```bash
    kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first_topic
    ```

* start *another* `consumer` part of the **same** `group`

    ```bash
    kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic --group my-first-application
    ```

* start *another* `consumer` part of a **different** `group` from beginning, i.e. **my-second-application**

    ```bash
    kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic --group my-second-application --from-beginning
    ```

* observe the messages being spread

* describe the `consumer group`

    ```bash
    kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group my-first-application --describe
    ```

  * output

  ```bash
   🚀  kafka-zero-to-pro ❯ kafka-consumer-groups.sh --bootstrap-server localhost:9092  --describe --group my-first-group

  GROUP           TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID                                           HOST            CLIENT-ID
  my-first-group  first_topic     0          5               5               0               console-consumer-5d028f33-0549-4826-a719-70b6188d5f52 /127.0.0.1      console-consumer
  my-first-group  first_topic     1          2               2               0               console-consumer-5d028f33-0549-4826-a719-70b6188d5f52 /127.0.0.1      console-consumer
  my-first-group  first_topic     2          1               1               0               console-consumer-c5ff906d-9abc-40d2-83d1-134ead27a552 /127.0.0.1      console-consumer
  ```

<br />

[↩️](../README.md)
