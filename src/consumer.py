import json

import pika

from main import Book, db

params = pika.URLParameters('amqps://qxbckujb:TNhb9rDz6qr1H3ZyiPn952zP-FM5zjW8@jackal.rmq.cloudamqp.com/qxbckujb')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='main')


def callback(channel, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'book_created':
        book = Book(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(book)
        db.session.commit()
        print('book_created')

    elif properties.content_type == 'book_updated':
        book = Book.query.get(data['id'])
        book.title = data['title']
        book.image = data['image']
        db.session.commit()
        print('book_updated')

    elif properties.content_type == 'book_deleted':
        book = Book.query.get(data)
        db.session.delete(book)
        db.session.commit()
        print('book_deleted')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('started Consuming')

channel.start_consuming()

channel.close()
