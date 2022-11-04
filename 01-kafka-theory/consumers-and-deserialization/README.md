# <img src="../../assets/img/kafka.png" width="30px"> **Kafka** - ***Consumers*** *and* ***Deserialization*** 🍽️


## **Description** 👀

`Consumers` read data from a topic, identified by name, using a pull model. `Consumers` automatically know which broker (kafka server) to read from, and which `partition` to read from. In case of a broker failure. `consumers` know how to recover. Data is read in order from low to high **offset** *within each partition*. The serialization/deserialization type must not change during a topics lifecycle (i.e. you can't change from `JSON` to `Avro`), and instead you should create a new topic instead.

<!-- 
<br />

## **Basic** `Commands` 📝

<br />


## **Examples** 🧩 -->

<br />

[↩️](../README.md)
