from pulsar import Client

service_url = 'pulsar://localhost:6650'
topic = 'test-topic2'

client = Client(service_url)
our_client = client.create_topic(topic, num_partitions=4)
producer = our_client.create_producer(topic)

# Generate and send messages
for i in range(1000):  # Change the number of messages as needed
    message = "Message {}".format(i)
    producer.send(message.encode('utf-8'))

# Close the producer and client
producer.close()
client.close()
