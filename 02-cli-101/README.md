# <img src="../assets/img/kafka.png" width="30px"> **Kafka** - ***Section 2:*** `CLI 101` 👩‍💻

## ***Table*** *of* ***`Contents`*** 📜

* 🏠 [**home**](../README.md)
* 👩‍💻 **cli 101**
  * 🚿 [**topics**](topics-cli/README.md)
* 🔗 **links**

<br />

## **Description** 👀

These are concepts used to interact with `Kafka` using the `CLI`, and come bundled with the `Kafka` binaries. Follow the quick start guide to install `Kafka` and get started, [**located here**](../00-resources/README.md#kafka-setup-).

<br>

## Important Notes 📝

* use the bootstrap server option ***EVERYWHERE***.
  * i.e `kafka-topics --bootstrap-server localhost:9092`

  since zookeeper will be deprecated in the future
  * i.e `kafka-topics --zookeeper localhost:2181` (don't do this, this is bad)

<br>

* when running a command from the `CLI` and you get the ***following error***

  ```bash
  Warn [AdminCLient clientId=adminclient-1] Connection to node -1
  ```

  * refer to this [**link**](../00-resources/README.md#kafka-troubleshooting-) for a solution
