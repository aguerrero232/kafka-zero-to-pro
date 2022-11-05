# <img src="../assets/img/kafka.png" width="30px"> **Kafka** - ***Section 0:*** `Resources` 🗃️

## ***Table*** *of* ***`Contents`*** 📜

* 🏠 [**home**](../README.md)
* 🗃️ **resources**
  * 🔗 **links**
    * 📄 <a href="https://kafka.apache.org/documentation/" target="_blank">**kafka documentation**</a>

<br />

## **Description** 👀

Resources for the `Kafka` ***Zero to Pro Guide***. Has images, pdfs, and links to other resources.

<br />

## **Helpful** `Content` 📌

This is a collection of helpful content for the `Kafka` ***Zero to Pro Guide***. It is not a part of `Kafka`, but it is helpful for learning `Kafka`.

### **Kafka** `Setup` <img src="../assets/img/kafka.png" width="19px">

Kafkas own quick start guide for setting up `Kafka`

* <a href="https://kafka.apache.org/quickstart" target="_blank">**kafka quick start**</a>

If your lazy, or don't want to leave these docs, you can use the quick start I made below.

1. get kafka
   * download kafka

      ```bash
      wget https://dlcdn.apache.org/kafka/3.1.0/kafka_2.13-3.1.0.tgz
      ```

   * extract the tar file
  
      ```bash
      tar -xzf kafka_2.13-3.3.1.tgz
      ```

   * move the extracted folder to your home directory

      ```bash
      mv kafka_2.13-3.3.1 ~/
      ```

2. set up your environment variables

   * go to you `.bashrc` or `.profile` file and add the following lines

      ```bash
        export KAFKA_BIN_ROOT="$HOME/kafka_2.13-3.3.1/bin"
        export KAFKA_CONFIG_ROOT="$HOME/kafka_2.13-3.3.1/config"
        PATH="$PATH:$KAFKA_BIN_ROOT:$KAFKA_CONFIG_ROOT"
      ```

   * test your `environment variables` in a **new** terminal

      ```bash
      echo $KAFKA_BIN_ROOT
      echo $KAFKA_CONFIG_ROOT
      echo $PATH
      ```

   * test to see if you can run `kafka` commands

      ```bash
      kafka-topics.sh
      ```

3. start up `Kafka` (using **KRaft**)

   * create Kafka data directory

      ```bash
      mkdir data/kafka-kraft
      ```

   * generate a cluster UUID

      ```bash
      KAFKA_CLUSTER_ID="$(kafka-storage.sh random-uuid)"
      ```

   * format the log directories

      ```bash
      kafka-storage.sh format -t "$KAFKA_CLUSTER_ID" -c "$KAFKA_CONFIG_ROOT/kraft/server.properties"
      ```

   * start the server

      ```bash
      kafka-server-start.sh  $KAFKA_CONFIG_ROOT/kraft/server.properties
      ```

   * Kafka is now running, keep this terminal open
    * the logs are located in `/tmp/kraft-combined-logs`, and can be configured in `$KAFKA_CONFIG_ROOT/kraft/server.properties`

<br>

### Kafka `Troubleshooting` <img src="../assets/img/kafka.png" width="19px">

* when running a command from the CLI and you get the following error

  ```bash
  Warn [AdminCLient clientId=adminclient-1] Connection to node -1
  ```

  * this is a WSL2 networking issue
    * stop the `Kafka` server and either KRaft or Zookeeper (depending on which you are using)
    * then run the following commands

      ```bash
      sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1
      ```

      ```bash
      sudo sysctl -w net.ipv6.conf.default.disable_ipv6=1
      ```

    * then go to the `Kafka` config file `server.properites` and change the `listeners` to `PLAINTEXT://localhost:9092`

      ```bash
      cd $KAFKA_CONFIG_ROOT
      ```

      ```bash
      nano server.properties
      ```

      ```bash
      listeners=PLAINTEXT://localhost:9092
      ```

    * then start the `Kafka` server and either KRaft or Zookeeper (depending on which you are using)
