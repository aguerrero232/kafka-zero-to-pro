# <img src="../assets/img/kafka.png" width="30px"> **Kafka** - ***Section 2:*** `CLI 101` 👩‍💻

## ***Table*** *of* ***`Contents`*** 📜

* 🏠 [**home**](../README.md)
* 👩‍💻 **cli 101**
  * 🚿 [**topics**](topics-cli/README.md)
* 🔗 **links**

<br />

## **Description** 👀

These are concepts used to interact with `Kafka` using the `CLI`, and come bundled with the `Kafka` binaries. Follow the quick start guide to install `Kafka` and get started, [**located here**](../00-resources/README.md#kafka-setup-).

### Important Note

Use the bootstrap server option ***EVERYWHERE***.

* i.e `kafka-topics --bootstrap-server localhost:9092`
  
since zookeeper will be deprecated in the future

* i.e `kafka-topics --zookeeper localhost:2181` (don't do this, this is bad)
