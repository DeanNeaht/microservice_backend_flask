import pika


params = pika.URLParameters('amqps://wvmozvxz:CJH8LLByzoJ41YKKgmS5fbXaslTRrRLW@woodpecker.rmq.cloudamqp.com/wvmozvxz')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='flask_backend')


def callback(ch, method, properties, body):
    print('Received in flask_backend')
    print(body)


channel.basic_consume(queue='flask_backend', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()
