# <img src="../../assets/img/kafka.png" width="30px"> **Kafka** - ***Producers*** *and* ***Message Keys*** 🏭

## **Description** 👀

`Producers` write data to topics (which are made of partitions). `Producers` know in advance which `partition` to write to and which `Kafka` **broker** (server) has it. In case a `Kafka` **broker** fails, `producers` will *automatically recover*. `Producers` can also choose to write to a `partition` based on a `key` in the `message`. If a `key` is provided, the same `key` will always be assigned to the same `partition`. This allows for ordering of related messages. `Keys` are optional. If no `key` is provided, the `message` will be assigned to a `partition` randomly. 

<!-- <br />

## **Basic** `Commands` 📝

<br />


## **Examples** 🧩
 -->

<br />


[↩️](../README.md)
