#!/usr/bin/env python

import pika
import random

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()  #подключились к брокеру сообщений, находящемся на локальном хосте

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct') #создали точку обмена сообщениями

message1 = ['black', 'white']
message2 = ['good color', 'bad color']

i = random.randint(0, 1)
severity = message1[i]
message = message2[i]

channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)    #отправили сообщение в очередь через точку обмена exchange
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
