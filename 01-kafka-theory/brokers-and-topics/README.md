# <img src="../../assets/img/kafka.png" width="30px"> **Kafka** - ***Brokers*** *and* ***Topics*** 🛃

## **Description** 👀

A `Kafka` cluster is composed of multiple `brokers` (servers). Each `broker` is identified with its ID (integer). Each `broker` contains certain `topic partitions`. Partitions are distributed across all the `brokers` in the `Kafka` cluster. This is what makes `Kafka` scale, and is called ***horizontal scaling***. You only need to connect to one `broker` and the `Kafka` clients will know how to be connected to the entire cluster. Each `broker` knows about all brokers, topics, and partitions (metadata). This is called ***cluster bootstrapping***.

<br />

<!-- 
## **Basic** `Commands` 📝

<br />

## **Examples** 🧩

<br /> -->

[↩️](../README.md)
