import random
import time
import numpy as N

'''как я поняла, фишка цепей тек и буд событий в том, что мы записываем в цепь буд
событий перед тем, как транзакт выполняет какое-то длительное действие'''

packages = {}
list_of_current = []
list_of_future = []
queue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

device_number = 1
current_time = 0
node_count = 10
node_period = 100
flag = 0
channel = 0

net_period = node_period/node_count
node_select = random.randint(0, net_period)

def collides(xmit_begin):
    x = time.time() # я хз, как определять время,
    # Функция time.time отображает время в секундах, начиная с эпохи, как число с плавающей запятой
    collide = (x - xmit_begin)
    return collide
# формируем по экспоненте время обработки
radius_array = N.random.exponential(10, (1, 9))
print('radius_array = ', radius_array)
# выбираем устр-во
device = {node_select: {'time': current_time + random.choice(radius_array[0])}}
# добавляем в список будущих событий
list_of_future.append(node_select)
list_of_future.sort(key=lambda n: device[n]['time'])
print("Цепь будущих событий после фазы ввода:", list_of_future)
print('device = ', device)
# увеличиваем очередь для этого устр-ва
queue[node_select] += 1

while(current_time<10000):
    print("\n")
    # делаем предыд пакет текущим
    cur_packages = node_select

    # generate
    radius_array = N.random.exponential(10, (1, 9))
    node_select = random.randint(0, net_period)
    device[node_select] = {'time': current_time + random.choice(radius_array[0])}
    list_of_future.append(node_select)   # 2 пакет в ЦБС
    # увеличиваем очередь для этого устр-ва
    queue[node_select] += 1

    if(device[node_select]['time'] >= device[cur_packages]['time']):
        list_of_future.remove(cur_packages)
        list_of_current.append(cur_packages)  # 1 пакет в ЦТС
        current_time = device[cur_packages]['time']  # пакет обработался
        queue[cur_packages] -= 1
        print("Пакет обработался")

    # проверяем, не возникла ли коллизия
    if(flag == 1):
      #  print('\nКоллизия по флагу\n')
        device[cur_packages]['time'] = current_time + random.uniform(5, 15)
        list_of_future.append(cur_packages)  # удаляем пакет из ЦТС
        list_of_current.remove(cur_packages)

# если разница между пакетами в цепи тек и в цепи буд событий меньше 1, то коллизия
    if(channel == 1):
        print('\nКанал занят\n')
        if((device[node_select]['time'] - device[cur_packages]['time']) <= 1):
           # print('\nКоллизия замечена\n')
            flag = 1
            device[cur_packages]['time'] = current_time + random.uniform(5, 15)
            list_of_future.append(cur_packages)    # удаляем пакет из ЦТС
            list_of_current.remove(cur_packages)
            device[node_select] = {'time': current_time + random.uniform(5, 15)} # а новый пакет остаётся в ЦБС,
            # просто прибавляем к него времени время коллизии

    list_of_future.sort(key=lambda n: device[n]['time'])
    print('list_of_current = ', list_of_current)
    print('cur_packages = ', cur_packages)
    if(flag==0):
        # обработка в канале
        channel = 1
        device[cur_packages] = {'time': current_time + 4}
        # переносим пакет из ЦТК в ЦБС
        list_of_current.remove(cur_packages)
        list_of_future.append(cur_packages)
        print('Пакет ушёл в обработку из ЦТС')
    else:
        #if(current_time >= device[node_select]['time']): # пакет обработался в коллизии
        print('Была коллизия, сначала пакет вытащился из ЦБС')
    flag = 0
    print('device = ', device)
    list_of_future.sort(key=lambda n: device[n]['time'])
    print("Цепь будущих событий после:", list_of_future)
    print('device = ', device)