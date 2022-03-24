import pika
import sys

if __name__ == "__main__":
  # TODO: 2a - specify different coffee drinks and send to p2_worker to create

  # establish connection; by default, rabbitmq runs on port 5642
  connection = pika.BlockingConnection(
      pika.ConnectionParameters(host='localhost'))
  channel = connection.channel()

  # declare queue for data queue
  channel.queue_declare(queue='coffee_queue', durable=True)
  
  # publish order to queue
  message = ' '.join(sys.argv[1:]) or 'latte'

  channel.basic_publish(
      exchange='',
      routing_key='coffee_queue',
      body=message,
      properties=pika.BasicProperties(
          delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
      ))
  print(" [x] Ordered %r" % message)
  connection.close()
  