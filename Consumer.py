from pulsar import Client, ConsumerType

service_url = 'pulsar://localhost:6650'
topic = 'test-topic2'

client = Client(service_url)

# Create consumers for specific partitions
consumers = []
for i in range(4):
    consumer = client.subscribe(
        topic,
        subscription_name=f'sub-{i}',
        consumer_type=ConsumerType.Shared,
        subscription_topics=[f'persistent://public/default/partitioned-topic-partition-{i}']
    )
    consumers.append(consumer)

# Consume messages from specific partitions
try:
    while True:
        for i, consumer in enumerate(consumers):
            msg = consumer.receive()
            if msg:
                print(f"Consumer {i} received: {msg.data().decode('utf-8')}")
                consumer.acknowledge(msg)

except KeyboardInterrupt:
    pass
finally:
    # Close the consumers and client
    for consumer in consumers:
        consumer.close()
    client.close()
