#!/usr/bin/env python3
# сообщения идут в ту очередь, binding key которой совпадает с routing key сообщения

import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

result = channel.queue_declare(exclusive=True)  #обеспечивает каждому клиенту новую очередь
queue_name = result.method.queue

severities = sys.argv[1]
if not severities:  #здесь - если нет аргумента
    sys.stderr.write("Please, enter correct params")
    sys.exit(1)

channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,  #имя очереди уникально
                       routing_key=severities) # но её ключ будет тот, который мы написали в параметре

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,  #callback функция будет получать сообщения из этой очереди
                      no_ack=True)

channel.start_consuming()  #запускаем бесконечную очередь
