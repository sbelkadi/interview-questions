from controllers.espresso_machine_broken import EspressoMachineBroken 
import pika
import time

if __name__ == "__main__":
  # TODO: 3 - create a worker that is more load-balanced than round-robin allocation used by RabbitMQ as a default.
  list_of_drinks = ['ristretto', 'espresso', 'lungo', 'crema', 'cappuccino', 'latte', 'flat_white']
  
  # add all drinks to the menu for this machine
  machine_broken_1 = EspressoMachineBroken()
  for drink in list_of_drinks:
      machine_broken_1.add_drink_to_menu(drink)

  # establish connection; by default, rabbitmq runs on port 5642
  connection = pika.BlockingConnection(
      pika.ConnectionParameters(host='localhost'))
  channel = connection.channel()

  # declare queue for data queue
  channel.queue_declare(queue='coffee_queue', durable=True)
  print(' [*] Waiting for coffee orders. To exit press CTRL+C')

  # declare callback function to call when message received
  def callback(ch, method, properties, body):
      drink_order = body.decode()
      print(" [x] Received %r" % drink_order)

      # test to see if the espresso machine recognized the drink order
      # the machine fails 10% of the time, so catch the exception
      try:
        params = machine_broken_1.get_drink_params(drink_order)
        if any(param is None for param in params):
          raise Exception("Drink order not recognized by espresso machine. Retrying...")
      
        # simulate time required to create drink
        time_to_create_drink = machine_broken_1.time_to_create_drink(drink_order)
        time.sleep(time_to_create_drink)

        print(f" [x] Ahhh, that's a tasty {drink_order}!")
        ch.basic_ack(delivery_tag=method.delivery_tag)
      
      except Exception as e:
        print(f" [***] {e}")
        if 'Retrying' in str(e):
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
        else:
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

  # basic_qos prefetch_count: number of messages that can be fetched on 1 queue
  # basic_consume: associate queue with callback function
  channel.basic_qos(prefetch_count=1)
  channel.basic_consume(queue='coffee_queue', on_message_callback=callback)

  # start listener
  channel.start_consuming()