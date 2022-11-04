# <img src="../../assets/img/kafka.png" width="30px"> **Kafka** - ***Consumer Groups*** 👥


## **Description** 👀

All the `consumers` in an application read data as `consumer groups`. Each `consumer` within a group reads from exlusive `partitions` of a topic. This allows for *parallel processing* of data. `Consumer groups` are *dynamically scalable* and can be *added or removed* at any time. To create distinct `consumer groups` you must use a *unique* `group.id` for each `consumer`. `Consumer Offsets` stores the offsets at which a `consumer group` has been reading stored in a `Kafka` topic named `__consumer_offsets`. When a `consumer` in a group has processed data received from `Kafka`, it should be **periodically** committing the offsets. If a `consumer` dies, it will be able to read back from where it left off thanks to the committed `consumer` offset. 

There are 3 delivery semantics for committing `consumer offsets`

1. **at least once** - `Consumer` offsets are committed *after* the message is processed. This means that if a `consumer` dies, it will read back from where it left off. This is the default delivery semantics for `consumer offsets`.
2. **at most once** - `Consumer` offsets are committed as soon as messages are received. If processing fails, some messages will be lost
3. **exactly once**



<!-- <br />

## **Basic** `Commands` 📝

<br />


## **Examples** 🧩 -->

<br />

[↩️](../README.md)
