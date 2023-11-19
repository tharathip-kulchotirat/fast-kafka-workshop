from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('kafkaworkshop', b'Testing Kafka Streaming!')
producer.flush()