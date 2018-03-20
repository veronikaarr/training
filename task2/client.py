#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))  #получение сообщений - подписка

channel.basic_consume(callback,
                      queue='hello', #наша callback функция будет получать сообщения из очереди с именем hello
                      no_ack=True)

channel.start_consuming() #запускаем бесконечную очередь