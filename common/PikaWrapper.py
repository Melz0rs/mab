import pika


class PikaWrapper:

    def __init__(self, host):
        self.__initialize_connection(host)

    def declare_queue(self, queue_name=None):
        # if queueName is None:

        self.channel.queue_declare(queue=queue_name)

    def declare_exchange(self, exchange_name, exchange_type):
        # if exchangeName is None:

        self.channel.exchange_declare(exchange_type)

    def send_message(self, message, routing_key='', exchange_name=''):
        self.channel.basic_publish(exchange=exchange_name,
                                   routing_key=routing_key,
                                   body=message)

    def start_receiving_messages(self, queue_name, callback_fn, auto_ack=True):
        self.channel.basic_consume(queue=queue_name,
                                   auto_ack=auto_ack,
                                   on_message_callback=callback_fn)

    def __initialize_connection(self, host):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = connection.channel()
