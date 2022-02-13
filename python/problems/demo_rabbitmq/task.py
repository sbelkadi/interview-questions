#!/usr/bin/env python
import pika
import sys

# establish connection; by default, rabbitmq runs on port 5642
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# declare queue for data queue
channel.queue_declare(queue='task_queue', durable=True)

# publish message to queue
message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
print(" [x] Sent %r" % message)
connection.close()