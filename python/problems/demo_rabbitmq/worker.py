#!/usr/bin/env python
import pika
import time

# establish connection; by default, rabbitmq runs on port 5642
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# declare queue for data queue
channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

# declare callback function to call when message received
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())

    # simulate time required to perform function
    time.sleep(body.count(b'.'))

    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


# basic_qos prefetch_count: number of messages that can be fetched on 1 queue
# basic_consume: associate queue with callback function
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

# start listener
channel.start_consuming()