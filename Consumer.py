from pulsar import Client, ConsumerType, Message
import signal
import sys

service_url = 'pulsar://localhost:6650'
topic = 'test-topic'
subscription = 'test-subscription'

client = Client(service_url)
consumer = client.subscribe(topic, subscription_name=subscription, consumer_type=ConsumerType.Shared,  negative_ack_redelivery_delay=5000)

def exit_handler(signal, frame):
    # to ensure an error-free exit
    consumer.close()
    client.close()
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

def process_message(msg: Message):
    consumer.negative_acknowledge(msg);
    msg = consumer.receive();
    consumer.acknowledge(msg);

try:
    while True:
        msg = consumer.receive()  # Receive messages
        if msg:
            process_message(msg)

except KeyboardInterrupt:
    exit_handler(signal.SIGINT, None)