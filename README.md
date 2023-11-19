# Apache Kafka Simple Workshop by Tharathip Kulchotirat

Apache Kafka is a distributed streaming platform that is designed to handle high volumes of data in real-time. It provides a publish-subscribe model for sending and receiving streams of records, similar to a message queue or enterprise messaging system. Kafka is known for its high throughput, fault-tolerance, and scalability, making it a popular choice for building real-time data pipelines and streaming applications.

Here's my short workshop for Apache Kafka. I will show you how to install and run Kafka on your local Mac OS machine. Then, we will create a simple producer and consumer to send and receive messages.

## Prerequisites
- Install Kafka using Homebrew
```bash
brew install kafka
```
- Prepare your python environment (in my case, I used `pyenv`)
```bash
pyenv virtualenv kafkaworkshop
```
- Activate your python environment
```bash
pyenv activate kafkaworkshop
```
- Install `kafka-python` library
```bash
pip install kafka-python
```
Now, you are ready to go!

## Start Kafka Server
- Start Zookeeper server
```bash
zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties
```
- Start Kafka server
```bash
kafka-server-start /opt/homebrew/etc/kafka/server.properties
```
Now, you have a Kafka server running on your local machine. Let's create a topic and test it out!

## Prepare a Consumer and a Producer in Python
- Consumer
```python
# import KafkaConsumer
from kafka import KafkaConsumer

# Create a consumer object with the topic name `kafkaworkshop`
consumer = KafkaConsumer('kafkaworkshop')

# Print out the message value from the consumer
for message in consumer:
    print(message.value.decode('utf-8'))
```
- Producer
```python
# import KafkaProducer
from kafka import KafkaProducer

# Create a producer object with defined bootstrap server
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send a message to the topic `kafkaworkshop` with the message `Testing Kafka Streaming!` (remember to encode the message to bytes with `b` prefix)
producer.send('kafkaworkshop', b'Testing Kafka Streaming!')

# Flush the producer
producer.flush()
```
Now, you have a consumer and a producer ready to go. Let's run them!

## Run the Consumer and the Producer
- Run the consumer
```bash
python consumer.py
```
- Run the producer
```bash
python producer.py
```
You should see the message `Testing Kafka Streaming!` on the consumer side.

## Conclusion
That's it! You have successfully installed and run Kafka on your local machine. You also have a simple consumer and producer to send and receive messages. Now, you can try to create a more complex consumer and producer to send and receive messages in real-time. Have fun!