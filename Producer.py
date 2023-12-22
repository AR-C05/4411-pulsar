from pulsar import Client, CompressionType

service_url = 'pulsar://localhost:6650'
topic = 'test-topic'

client = Client(service_url)
producer = client.create_producer(topic, compression_type=CompressionType.LZ4)

# Generate and send messages
for i in range(10000):  # Change the number of messages as needed
    message = "Message {}".format(i)
    producer.send(message.encode('utf-8'))