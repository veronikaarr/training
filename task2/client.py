#!/usr/bin/env python3
# сообщения идут в ту очередь, binding key которой совпадает с routing key сообщения
'''#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange = 'logs',
                         exchange_type = 'fanout')

result = channel.queue_declare(exclusive = True)  #обеспечивает каждому клиенту новую очередь
queue_name = result.method.queue

channel.queue_bind(exchange = 'logs',
                   queue = queue_name)  #имя очереди уникально

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))  #получение сообщений - подписка

channel.basic_consume(callback,
                      queue=queue_name, #наша callback функция будет получать сообщения из очереди с именем hello
                      no_ack=True)

channel.start_consuming() #запускаем бесконечную очередь'''

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:  #здесь - если нет аргумента, записывать всё  написан образей того, что можно отправить
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities: #
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,  #имя очереди создаётся рандомно -?
                       routing_key=severity) # но её ключ будет тот, который мы написали в параметре

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,  #callback функция будет получать сообщения из этой очереди
                      no_ack=True)

channel.start_consuming()
