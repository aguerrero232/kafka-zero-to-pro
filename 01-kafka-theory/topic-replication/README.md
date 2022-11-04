# <img src="../../assets/img/kafka.png" width="30px"> **Kafka** - ***Topic Replication*** 👯

## **Description** 👀

`Topics` should have a replication factor of **> 1**, ***usually between 2 and 3 in production***, to ensure that data is not lost in the event of a `broker` failure. Leader `partitions` are replicated to `followers` on other `brokers`. If the `leader` fails, one of the `followers` will be elected as the new `leader` for the `partition`. `Producers` can only send data to brokers that are leaders of a partition. Each `partition` has a single `leader` and zero or more `ISR` (**in-sync replicas**). 

<!-- <br />

## **Basic** `Commands` 📝

<br />

## **Examples** 🧩 -->

<br />

[↩️](../README.md)