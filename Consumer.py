from pulsar import Client, ConsumerType
import signal
import sys

service_url = 'pulsar://localhost:6650'
topic = 'test-topic'
subscription = 'test-subscription'

client = Client(service_url)
consumer = client.subscribe(topic, subscription_name=subscription, consumer_type=ConsumerType.Shared)

def exit_handler(signal, frame):
    # to ensure an error-free exit
    consumer.close()
    client.close()
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

try:
    while True:
        msg = consumer.receive()  # Receive messages
        print("Received message: %s" % msg.data())
        consumer.acknowledge(msg)  # Acknowledge the message
except KeyboardInterrupt:
    exit_handler(signal.SIGINT, None)