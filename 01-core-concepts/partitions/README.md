# <img src="../../assets/img/kafka.png" width="30px"> **Kafka** - ***Partitions*** 🗄️

## **Description** 👀

`Topics` are split into `partitions`. `Messages` in each `partition` are ordered, and **immutable**. Each `message` within a `partition` is assigned a sequential `id` called the `offset`. `Offsets` are used to identify the position of a `message` within a `partition`. Data is only kept for a limited time (default is 1 week) and is **automatically deleted** to prevent data from growing indefinitely. `Offsets` are **never** reused, *even if data is deleted*. Order is guaranteed within a `partition`, but not across `partitions`. Data is assigned randomly to a `partition` unless a `key` is provided. If a `key` is provided, the same `key` will always be assigned to the same `partition`. This allows for ordering of related messages. You can have as many `partitions` per `topic` as you want.

<!-- <br />

## **Basic** `Commands` 📝

<br />

## **Examples** 🧩 -->

<br />

[↩️](../README.md)
