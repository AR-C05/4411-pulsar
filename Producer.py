from pulsar import Client, Message

service_url = 'pulsar://localhost:6650'
topic = 'test-topic'

client = Client(service_url)
producer = client.create_producer(topic)

# Generate and send messages
for i in range(1000):  # Change the number of messages as needed
    message = "Message {}".format(i)
    producer.send(message.encode('utf-8'))
