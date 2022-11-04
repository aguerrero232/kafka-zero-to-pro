# Kafka Zero To Pro <img src="assets/img/kafka.png" width="30px">

<img src="assets/img/header.png" width="100%" height="330px">

<br/>

### ⛏️ ***"A stone is broken by the last stroke of the hammer. This does not mean that the first stroke was useless. Success is the result of continuous effort."*** ⛏️

<br>

## ***Table*** *of* ***`Contents`*** 📜

* 🗃️ [***resources***](00-resources/README.md)
* 🧠 [***core concepts***](01-core-concepts/README.md)

<br />

`Kafka` is used for building *real-time data pipelines* and *streaming apps*. It is **horizontally scalable**, **fault-tolerant**, **wicked fast**, and runs in production in **thousands of companies**.

***Use cases include***

* **`real-time analytics`** (e.g. clickstreams, ad impressions, IoT telemetry)
* **`messaging systems`** (e.g. activity feeds, alert notifications, **`stream processing`**)
* **`activity tracking`** (e.g. GPS location, user behavior)
* **`stream processing`** (e.g. fraud detection, anomaly detection, real-time alerting)
* **`decoupling`** **microservice`** (e.g. service oriented architecture)
* **`microservices pub/sub`** (e.g. event-driven architecture)


## **Kafka** `Architecture` 🏗️

`Kafka` only accepts bytes as an input from producers and sends bytes out as an output to consumers. Messages are serialized and deserialized by the producer and consumer respectively. This allows `Kafka` to be used with any programming language. Serialization and deserialization is used only on keys and values.

* topics
* partitions
* messages  
