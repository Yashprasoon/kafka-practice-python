from kafka import KafkaConsumer

def consume_messages(topic):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers='localhost:9092',
        group_id='message_processing_group',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        value_deserializer=lambda x: x.decode('utf-8')
    )
        
    for msg in consumer:
        if msg is None:
            continue

        print(f"Received message: {msg.value} from topic: {msg.topic}")
