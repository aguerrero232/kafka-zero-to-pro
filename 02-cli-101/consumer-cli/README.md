# <img src="../../assets/img/kafka.png" width="30px"> **Kafka** - ***Consumers*** `CLI` 🍽️

***Refer back to the theories section for more information on consumers.***

## **Description** 👀

The `Kafka cli` uses consumers for consuming messages from  `Kafka` topics.

<br />

## **Basic** `Commands` 📝

* **get** *consumers*-`cli` functionalities

    ```bash
    kafka-console-consumer.sh 
    ```

* **consume** `messages` from a `topic`

    ```bash
    kafka-console-consumer.sh --bootstrap-server <kafka-broker> --topic <topic-name>
    ```

  * the consumer will start consuming from the `end` of the `topic` by default
  * to test this, you can use the `producer` to send `messages` to the `topic` and then use the `consumer` to consume the `messages` from the `topic`

    * create a `topic`

    * create a `consumer` to consume `messages` from the `topic`

    * create a `producer` to send `messages` to the `topic`

    * view the `messages` consumed by the `consumer` in the `terminal`

  * **view** the next `message` in the `topic`

    ```bash
    kafka-console-producer.sh --bootstrap-server <kafka-broker> --topic <topic-name>
    ```

* **consume** `messages` from a `topic` at the `beginning`

    ```bash
    kafka-console-consumer.sh --bootstrap-server <kafka-broker> --topic <topic-name> --from-beginning
    ```

* **display** *key*, *values* and *timestamps* of `messages` consumed

    ```bash
    kafka-console-consumer.sh --bootstrap-server <kafka-broker> --topic <topic-name> --formatter kafka.tools.DefaultMessageFormatter --property print.key=true --property print.value=true --property print.timestamp=true --from-beginning 
    ```

<br />

## **Examples** 🧩

* **consume** `messages` from a `topic`

    ```bash
    kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic
    ```

* **consume** `messages` from a `topic`

    ```bash
    kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic --from-beginning
    ```

* **display** *key*, *values* and *timestamps* of `messages` consumed

    ```bash
    kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic --formatter kafka.tools.DefaultMessageFormatter --property print.key=true --property print.value=true --property print.timestamp=true
    ```

* *sample output* from final example using `producer` and `consumer`

  * `prodcuer` produces `messages` to the `topic`

    ```bash
    🚀  kafka-zero-to-pro ❯ kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first_topic --property parse.key=true --property key.separator=:                                                                                                                                     
    >hello:world
    >im:guerrero
    >i:love learning
    ```

  * `consumer` consumes `messages` from the `topic`

    ```bash
    🚀  kafka-zero-to-pro ❯ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic --formatter kafka.tools.DefaultMessageFormatter --property print.key=true --property print.value=true --property print.timestamp=true
    CreateTime:1667959647470        hello   world
    CreateTime:1667959656726        im      guerrero
    CreateTime:1667959665180        i       love learning
    ```

<br />

[↩️](../README.md)
