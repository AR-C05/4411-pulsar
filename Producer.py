from pulsar import Client, Message
import time

service_url = 'pulsar://localhost:6650'
topic = 'test-topic'

client = Client(service_url)
producer = client.create_producer(topic, batching_enabled=True)

# Generate and send messages
for i in range(1000):  # Change the number of messages as needed
    message = "Message {}".format(i)
    producer.send_async(message.encode('utf-8'), callback=None)


producer.flush()

producer.close()
client.close()