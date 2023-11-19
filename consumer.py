from kafka import KafkaConsumer

consumer = KafkaConsumer('kafkaworkshop')

for message in consumer:
    print(message.value.decode('utf-8'))