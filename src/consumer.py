import pika

params = pika.URLParameters('amqps://qxbckujb:TNhb9rDz6qr1H3ZyiPn952zP-FM5zjW8@jackal.rmq.cloudamqp.com/qxbckujb')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='main')


def callback(channel, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('started Consuming')

channel.start_consuming()

channel.close()
