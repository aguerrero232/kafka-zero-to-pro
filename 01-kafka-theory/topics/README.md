# <img src="../../assets/img/kafka.png" width="30px"> **Kafka** - ***Topics*** 🚿

## **Description** 👀

`Topics` are a *particular* stream of **data**, like a table in a database (without the constraints). You can have as many topics as you want, and is identified by its **name**. `Topics` also support **any** message format. The sequence of messages in a `topic` is called a `data stream`. You can not query a `topic` directly, but you can use a `consumer` to read the `data stream` from the `topic`. Similarly `Kafka` uses a `producer` to write the `data stream` to the `topic`.

<br>

## **Kafka Topic** `Durability` 💪

As a rule, for a replication factor of **N**, you can permanently lose up to `N-1` brokers and still recover your data. For example, if you have a replication factor of 3, you can lose 2 brokers and still recover your data. This is because the data is replicated on the remaining brokers. If you lose all the brokers, you will lose all the data. This is why it is important to have a replication factor of **> 1**.


<br />

<!-- ## **Basic** `Commands` 📝

<br />

## **Examples** 🧩

<br /> -->

[↩️](../README.md)
