from pulsar import Client
import time

service_url = 'pulsar://localhost:6650'
topic = 'test-topic'

client = Client(service_url)
producer = client.create_producer(topic, batching_enabled=True,batching_max_messages=10)
batch_size = 100
batch_interval = 5

# Generate and send messages
for i in range(batch_size):  # Change the number of messages as needed
    message = "Message {}".format(i)
    producer.send(message.encode('utf-8'))

    # Batch messages and send after reaching the specified batch size
    if (i + 1) % batch_size == 0:
        producer.flush()

    # Introduce a delay for batching based on time interval
    if (i + 1) % batch_interval == 0:
        time.sleep(1)  # Adjust the sleep duration as needed
