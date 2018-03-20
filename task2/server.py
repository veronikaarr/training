#!/usr/bin/env python

'''#!/usr/bin/env python3
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))  #подключились к брокеру сообщений, находящемся на локальном хосте
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')  #создали точку обмена с именем logs и типом fanout - просто передаёт
#сообщения подписавшимся клиентам

message = 'Hello, boy {}, I am just a message'.format(' '.join(sys.argv[1:]))

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)  #отправили сообщение в очередь через точку обмена exchange в очередь hello
#c телом Hello Worls - ?

print(" [x] Sent %r" % message) #
connection.close()'''

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 2 else 'info' #если есть что-то в аргументе записывать в переменную, иначе -
#она равна info
message = ' '.join(sys.argv[2:]) or 'Hello World!' #сообщение - срез после второго аргумента - ?

channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
