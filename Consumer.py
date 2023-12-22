from pulsar import Client, ConsumerType
import signal
import sys

service_url = 'pulsar://localhost:6650'
topic = 'test-topic'
subscription = 'test-subscription'

client = Client(service_url)
consumer = client.subscribe(topic, subscription_name=subscription, consumer_type=ConsumerType.Shared)
ack_timeout = 10000


def exit_handler(signal, frame):
    # to ensure an error-free exit
    consumer.close()
    client.close()
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

try:
    while True:
        msg = consumer.receive(timeout_millis=ack_timeout)  # Receive messages
        try:
            # Process the message
            print(f"Received message: {msg.data().decode('utf-8')}")
        except Exception as e:
            # Handle processing errors
            print(f"Error processing message: {e}")
            # Don't acknowledge the message, allowing for redelivery
        finally:
            consumer.acknowledge(msg)  # Acknowledge the message
except KeyboardInterrupt:
    exit_handler(signal.SIGINT, None)