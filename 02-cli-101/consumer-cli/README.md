# <img src="../../assets/img/kafka.png" width="30px"> **Kafka** - ***Consumers*** `CLI` 🍽️


## **Description** 👀

<br />

## **Basic** `Commands` 📝

<br />


## **Examples** 🧩

```bash
# basic
kafka-console-consumer.sh 
```

```bash
# consuming
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic
```

```bash
# other terminal
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first_topic
```

```bash
# consuming from beginning
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic --from-beginning
```

```bash
# display key, values and timestamp in consumer
kafka-console-consumer --bootstrap-server localhost:9092 --topic first_topic --formatter kafka.tools.DefaultMessageFormatter --property print.timestamp=true --property print.key=true --property print.value=true --from-beginning
```

<br />

[↩️](../README.md)
