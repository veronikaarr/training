#!/usr/bin/env python3
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))  #подключились к брокеру сообщений, находящемся на локальном хосте
channel = connection.channel()

channel.queue_declare(queue='hello')  #создали очередь с именем хеллоу

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')  #отправили сообщение в очередь через точку обмена exchange в очередь hello
#c телом Hello Worls - ?

print(" [x] Sent 'Hello World!'") #
connection.close()
