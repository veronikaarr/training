# !user/bin/ev/python3
# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce

Tc = 27
Ts = 221
Tw = 523

def grafik():
    fig = plt.figure()
    xax = fig.add_subplot(111)
    xax.grid(True)

    #xax.grid(True, which='major')
    #xax.grid(True, which='minor')

    xax.yaxis.set_label_position('left')
    xax.set_ylabel(u' ')
    xax.xaxis.set_label_position('top')
    xax.set_xlabel(u'Число каналов')

    # Ось абсцисс
    for label in xax.xaxis.get_ticklabels():
        # label - это экземпляр текста Text
        label.set_color('red')
        label.set_rotation(-45)
        label.set_fontsize(15)

'''Первый пункт'''

lamda = 1/Tc
nu = 1/Ts
a = lamda/nu
n = 13
Potk = list()
Pobsl = list()
nsr = list()

Pn = [(math.pow(a, x) / math.factorial(x)) for x in range(0, n)]

Po = list(map(lambda y: (1 / sum(Pn[0:y])), range(1, n+1)))

for x in range(0, n):
    Potk.append(Pn[x] * Po[x])
    Pobsl.append(1 - Potk[x])
    if x != 0:
        nsr.append(a*Pobsl[x]/x)

Potk = list(map(lambda x:round(x,3), Potk))
nsr = list(map(lambda x:round(x,3), nsr))

'''Построение графика'''

grafik()

x = np.linspace(1, n, 0.1)
z = [x for x in range(1,n)]
plt.plot(z, Potk[1:n], z, nsr[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,Potk):
    plt.text(i, j, str(j))
for w,e in zip(z,nsr):
    plt.text(w, e, str(e))
plt.savefig('1_Вер_отк+коэф_загр.png')
#plt.show()


'''Второй пункт ок'''

def task_1_2(tc1, ts1, countOperator,channel):
    a = ts1 / tc1
    A = 1 / tc1

    channel = channel+1
    queue = countOperator - channel
    znam = 1.0

    i = 1
    while(i <= channel):
        promp = math.pow(a, i) / math.factorial(i)
        promp = float('{:.3f}'.format(promp))
        p[i] = promp
        znam += p[i]
        i = i + 1

    i = (channel + 1)
    while(i <= (channel + queue)):
        promp1 = math.pow((a / channel), (i - channel)) * (math.pow(a, channel) / math.factorial(channel))
        promp1 = float('{:.3f}'.format(promp1))
        p[i] = promp1
        znam += p[i]
        i=i+1

    # вычисление P0
    p[0] = 1.0 / znam

    i = 1
    while(i <= (channel + queue)):
        promp2 = p[i]*p[0]
        promp2 = float('{:.3f}'.format(promp2))
        p[i] = promp2
        i=i+1

    p2_list.append(p[countOperator])

    busyOperator = 0.0
    busyOperator = (a * (1 - p[countOperator])) / channel
    busyOperator = float('{:.3f}'.format(busyOperator))
    busyOperator_list.append(busyOperator)

    queueLengh = 0.0
    i = (channel + 1)
    while(i <= (channel + queue)):
        queueLengh=queueLengh+math.pow((a / channel), (i - channel)) * (math.pow(a, channel) / math.factorial(channel)) \
                   * p[0] * (i - channel)
        i=i+1

    busyQueue = 0.0
    if (queue == 0):
        busyQueue = 0
    else:
        busyQueue = queueLengh / queue

    queueWait = queueLengh / A
    queueLengh = float('{:.3f}'.format(queueLengh))
    queueWait = float('{:.3f}'.format(queueWait))
    queueLengh_list.append(queueLengh)
    queueWait_list.append(queueWait)
    return (channel, countOperator)

channel = 0
countOperator = 13

p = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
busyOperator_list = []
queueLengh_list = []
queueWait_list = []
p2_list = []

channel, countOperator = task_1_2(Tc, Ts, countOperator, channel)

while (channel < countOperator):
    channel, countOperator = task_1_2(Tc, Ts, countOperator,channel)
    #print('channel = {0}, countOperator = {1}'.format(channel,countOperator))

print('p2_list = ', p2_list)
print('len_p = ', len(p2_list))
print('len_b = ', len(busyOperator_list))
print('len_q_L = ', len(queueLengh_list))
print('len_q_W = ', len(queueWait_list))

'''Построение графиков'''

'вероятность отказа в зависимости от длины очереди'

grafik()

z = [x for x in range(1,14)]

plt.plot(z, p2_list[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,p2_list):
    plt.text(i, j, str(j))
plt.savefig('2_1_вероятность отказа.png')

'''коэффициент загрузки операторов в зависимости от длины очереди'''

grafik()

z = [x for x in range(1,14)]

plt.plot(z, busyOperator_list[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,busyOperator_list):
    plt.text(i, j, str(j))
plt.savefig('2_2_коэффициент загрузки операторов.png')

'''математического ожидания длины очереди в зависимости от длины очереди'''

grafik()

plt.plot(z, queueLengh_list[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,queueLengh_list):
    plt.text(i, j, str(j))
plt.savefig('2_3_математического ожидания длины очереди.png')

'Математического ожидания времени пребывания клиентов в очереди в зависимости от длины очереди'

grafik()

plt.plot(z, queueWait_list[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,queueWait_list):
    plt.text(i, j, str(j))
plt.savefig('2_4_математического ожидания времени пребывания клиентов.png')


Po_promej = [(math.pow(a, x) / math.factorial(x)) for x in range(0, n)]
Po_2_list = []

for n in range(1,16):
    m = 16 - n
    print('n = {}, m = {}'.format(n, m))
    Po_2 = 1 / (sum(Po_promej[0:(n)]) + (math.pow(a, n + 1) / math.factorial(n) * (n - a)) *
                                    (1 - (math.pow((a / n), m))))

    Potk_2 = (math.pow(a, (n + m)) * Po_2) / (math.factorial(n) * math.pow(n, m))
    q = a * (1 - (math.pow(a, (n + m)) * Po_2) / (math.factorial(n) * math.pow(n, m))) / n
    Loh = sum([x * (math.pow(a, (n + x)) / (math.pow(n, x) * math.factorial(n))) * Po_2 for x in range(1, m + 1)])
    S = Loh / m
    Tsr = Loh / lamda
    wtf = [(math.pow(n, x) * math.factorial(n)) for x in range(1, m + 1)]
    #print('То самое кривое выражение = ', wtf)
    print('Po_2 = {0}, Potk_2 = {1}, q = {2}, Loh = {3}, S = {4}, Tsr = {5}'.format(Po_2, Potk_2, q, Loh, S, Tsr))

'''Третий пункт'''

def task_1_3(tc1, ts1, countOperator, channel, foundResult):
    channel = channel+1
    if (a / channel < 1):
        queue = 1
        while(queue < maxQueue):
            for i in range(0, channel + queue + 1):
                p.append(0)
            znam = 1.0

            i = 1
            while (i <= channel):
                p[i] = pow(a, i) / math.factorial(i)
                znam += p[i]
                i=i+1

            i = (channel + 1)
            while (i <= (channel + queue)):
                p[i] = pow((a / channel), (i - channel)) * (pow(a, channel) / math.factorial(channel))
                znam += p[i]
                i=i+1

            # вычисление P0
            p[0] = 1.0 / znam

            i = 1
            while(i <= (channel + queue)):
                p[i] *= p[0]
                i=i+1

            busyOperator = 0.0    # коэффициент загрузки операторов в зависимости от длины очереди
            busyOperator = (a * (1 - p[channel + queue])) / channel

            queueLengh = 0.0
            i = (channel + 1)
            while(i <= (channel + queue)):
                queueLengh += pow((a / channel), (i - channel)) * (pow(a, channel) / math.factorial(channel)) * p[0] * (i - channel)
                i=i+1

            busyQueue = 0.0   # коэффициент занятости мест в очереди в зависимости от длины очереди
            if (queue == 0):
                busyQueue = 0
            else:
                busyQueue = queueLengh / queue

            results[queue] = abs(busyOperator - busyQueue)
            results_list.append(results[queue])

            #fout << results[queue] << '\t' << channel << '\t' << queue << endl;

            if (results[queue - 1] < results[queue] and results[queue - 1] < results[queue - 2]):
                finalParams[0] = channel
                finalParams[1] = queue
                finalResult = results[queue - 1]
                foundResult = True
            queue=queue+1
    return (channel,countOperator, foundResult,finalParams)

channel = 0
a = Ts / Tc
p = []
maxQueue = 100
results = []
finalParams = [0,0]
results_list = []
for i in range(0,maxQueue + 1):
    results.append(0)
foundResult = False
channel, countOperator, foundResult, finalParams = task_1_3(Tc, Ts, countOperator, channel, foundResult)
while (channel < countOperator and foundResult != True):
    channel, countOperator, foundResult, finalParams = task_1_3(Tc, Ts, countOperator,channel, foundResult)

print('\n\n\nResult 3 item: {0}, {1}\n\n\n'.format(finalParams[0], finalParams[1]))
print('results_list = ',len(results_list))

'''Построение графиков'''

grafik()

z = [x for x in range(1,160) if x%10==0]
plt.plot(z, results_list[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,results_list):
    plt.text(i, j, str(j))
plt.savefig('3_Длина_оч.png')

'''Четвёртый пункт Здесь вроде всё ок'''

Po_promej_3 = [(math.pow(a, x) / math.factorial(x)) for x in range(0, n)]


Loh_list = []
Tsr_list = []
q_list = []

for n in range(9,17):
    print('n = {}, m = {}'.format(n, m))
    Po_2 = 1 / (sum(Po_promej[0:(n)]) + (math.pow(a, n + 1) / math.factorial(n) * (n - a)))

    Loh = math.pow(a, (n + 1)) / (math.pow((n - a), 2) * math.factorial(n - 1)) * Po_2
    Loh_list.append(Loh)
    q = a / n
    q_list.append(q)
    Tsr = Loh / lamda
    Tsr_list.append(Tsr)
    print('Po_2 = {0}, Loh = {1}, q = {2}, Tsr = {3}, S = {4} '.format(Po_2, Loh, q, Tsr, S))

n = 9

z = [x for x in range(9,17)]

'''Построение графиков'''

grafik()

plt.plot(z, Loh_list[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,Loh_list):
    plt.text(i, j, str(j))
plt.savefig('4_Длина_оч.png')

grafik()

plt.plot(z, q_list[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,q_list):
    plt.text(i, j, str(j))
plt.savefig('4_Коэф_загр.png')

grafik()

plt.plot(z, Tsr_list[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,Tsr_list):
    plt.text(i, j, str(j))
plt.savefig('4_Время_ожид.png')


'''Пятый пункт Здесь почему-то при изменении числа каналов m почти не меняется (только при n = 16) меняется
увеличение точности не помогает
также: нужно сделать так, чтобы m пересчитывалось для разного числа каналов и:
дописать остальные формулы, следующие после расчёта длины очереди'''

eps = pow(10, -8)
Po_5 = 100
Po_5_next = 0
denomin_list = []
b_list = []
Po_5_list = []
m = 2
n = 5

def Po(n_ = 16, m_ = 2):
    Po_promej1_5 = [math.pow(a, x) / math.factorial(x) for x in range(1, n_)]
    term1 = sum(Po_promej1_5)
    for i in range(1, m_):
        for q in range(1, i):
            denomin = n_*nu + i * (1/Tw)
            denomin_list.append(denomin)
        op = reduce(lambda res, x: res * x, denomin_list, 1)
        denomin_list.clear()
        print(op, 'op_________________')
        b = math.pow(lamda, i) / op
        b_list.append(b)
    term2 = math.pow(a, n_) * sum(b_list) /math.factorial(n_)
    print('b = ', b_list)
    b_list.clear()
    print('Делимое = ', math.pow(a, n_) * sum(b_list))
    print('Делитель = ', math.factorial(n_))
    print('Первое слагаемое:', term1)
    print('Второе слагаемое:', term2)
    Po_5_next = 1 / (term1 + term2)
    print('m = ', m_)
    print('n = ', n_)
    print('Po_5_next = ', Po_5_next)
    return (m_, Po_5_next)

m, Po_5_next = Po()
m = m + 1
while(Po_5 - Po_5_next > eps):
    Po_promej1_5 = [math.pow(a, x) / math.factorial(x) for x in range(1, n)]
    term1 = sum(Po_promej1_5)
    print(m, 'm before')
    b = 0
    for i in range(1, m):
        for q in range(1, i):
            denomin = n*nu + i * (1/Tw)
            denomin_list.append(denomin)
        op = reduce(lambda res, x: res * x, denomin_list, 1)
        print(op, 'op')
        b = math.pow(lamda, i) / op
        b_list.append(b)
    term2 = math.pow(a, n) * sum(b_list) /math.factorial(n)
    Po_5 = Po_5_next
    Po_5_next = 1 / (term1 + term2)
    m = m + 1
    print(m, 'm after')
    print(Po_5_next, 'Po_5_next')
    # print(Po_5, 'Po_5')

   # print('\netooooo POOOOOOO', Po_5)
m = m + 2
print('Результат: m = ', m)
n = 16
for i_ in range(1, n + 1):
    print('\n Это новая итерация для Po при i = {} \n'.format(i_))
    m, Po_5_ =  Po(i_, m)
    Po_5_list.append(Po_5_)

print(Po_5_list, 'Po5___')

Loh_5_sum = 0
Loh_5_list = []

n = 16

for k_ in range(1, n+1):
    for z in range(1, k_):
            Pn_5 = math.pow(a, k_+z) * Po_5_list[k_-1] / (math.pow(z, k_) * math.factorial(z))
            Loh_5 = Pn_5*z
            Loh_5_sum = Loh_5 + Loh_5_sum
    Loh_5_list.append(Loh_5_sum)

print(Loh_5_list)

'''Построение графиков'''

grafik()

z = [x for x in range(1,17)]

plt.plot(z, Loh_5_list[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,Loh_5_list):
    plt.text(i, j, str(j))
plt.savefig('5_Длина_оч.png')

a = Ts / Tc
A = 1 / Tc
M = 1 / Ts
N = 1 / Tw
eps = 1e-8
p = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
queueLengh5_list = []
queueWait5_list = []
busyOperator5_list = []

countOperator = 12

def task_1_5(Tc, Ts, Tw, countOperator, channel):
    channel=channel+1
    znam = 1.0

    print('channel = ', channel)
    i = 1
    while(i <= channel):
        p[i] = math.pow(a, i) / math.factorial(i)
        znam += p[i]
        i=i+1

    p[channel + 1] = p[channel] * (A / (channel * M + N))
    znam += p[channel + 1]

    i = 2
    while(True):
        smalZnam = 1.0
        q = 1
        while(q <= i):
            smalZnam *= (channel * M + q * N)
            #print('q = {0}, i = {1}'.format(q,i))
            q=q+1

        p[channel + i] = p[channel] * (pow(A, i) / smalZnam)
        print('rr = ', abs(p[channel + i] - p[channel + (i - 1)]), eps)
        if (abs(p[channel + i] - p[channel + (i - 1)]) < eps):
            #print('tiis')
            break

        znam += p[channel + i]
        queue = i
        i=i+1

        #вычисление P0
        p[0] = 1.0 / znam

        i = 1
        while(i <= (channel + queue)):
            p[i] *= p[0]
            i=i+1

        queueLengh = 0.0
        i = channel + 1

        while(i <= (channel + queue)):
            queueLengh += (i - channel) * p[i]
            i=i+1

    print('queueLengh = ', queueLengh)
    queueLengh = float('{:.10f}'.format(queueLengh))
    queueLengh5_list.append(queueLengh)

    queueWait = queueLengh / A
    queueWait = float('{:.10f}'.format(queueWait))
    queueWait5_list.append(queueWait)
    busyOperator = 0.0
    i = 1
    while(i <= channel):
        busyOperator += i * p[i]
        i = i+1
    busyOperator_list.append(busyOperator)

    i = (channel + 1)
    while(i <= (channel + queue)):
        busyOperator += channel * p[i]
        i=i+1

    busyOperator = busyOperator / channel
    busyOperator = float('{:.10f}'.format(busyOperator))
    busyOperator5_list.append(busyOperator)
    return (channel)

channel = task_1_5(Tc, Ts, Tw, 12, 0)
while (channel < countOperator):
    print('channel_____________ = ', channel)
    channel = task_1_5(Tc, Ts, Tw, 12, channel)

'''Построение графиков'''

ql5 = len(queueLengh5_list)
qw5 = len(queueWait5_list)
b5 = len(busyOperator5_list)
print('ql5 = {0}, qw5 = {1}, b5 = {2}, p = {3}'.format(queueLengh5_list, queueWait5_list, busyOperator5_list, p))

z = [x for x in range(1,13)]
grafik()

plt.plot(z, queueLengh5_list[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,queueLengh5_list):
    plt.text(i, j, str(j))
plt.savefig('5_Математического ожидания длины очереди.png')

grafik()

plt.plot(z, queueWait5_list[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,queueWait5_list):
    plt.text(i, j, str(j))
plt.savefig('5_Математического ожидания времени пребывания клиентов.png')

grafik()

plt.plot(z, busyOperator5_list[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,busyOperator5_list):
    plt.text(i, j, str(j))
plt.savefig('5_Коэффициент загрузки операторов.png')

'2 задание'

'''Задача №2. Проектирование производственного участка.
Имеется участок с N станками. Среднее время между наладками составляет Tc минут,
среднее время наладки – Ts минут. Все потоки случайных событий считать пуассоновскими.
Построить график зависимости числа простаивающих станков от числа наладчиков.
Построить график зависимости коэффициента занятости наладчиков от их числа.'''

def getAvarageWorkChannels(n, m, r, P0):
    summ = n*P0
    k = n - 1; i = 1
    while(i < m):
        summ += k*P0*(math.pow(r, i) / math.factorial(i))*(math.factorial(n) / math.factorial(n-i))
        i=i+1; k=k-1

    i = m; j = 0
    while(i <= n):
        summ += k*P0*(math.pow(r, i) / (math.factorial(m)*math.pow(m, j)))*(math.factorial(n) / math.factorial(n-i))
        i=i+1; j=j+1; k=k-1

    return(summ)

def getAvarageWorkers(n, m, r, P0):
    summ = 0.0; i = 1
    while(i < m):
        summ += i*P0*(pow(r, i) / math.factorial(i))*(math.factorial(n) / math.factorial(n-i))
        i = i+1
    i = m; j = 0
    while(i <= n):
        #print('n = {}, i = {}'.format(n, i))
        summ += m*P0*(pow(r, i) / (math.factorial(m)*math.pow(m, j)))*(math.factorial(n) / math.factorial(n-i))
        i = i + 1; j = j + 1
    return(summ/m)

def getP0ForCloseSystems(n, m, r):
    sum = 1.0; i = 1
    while(i <= m):
        sum += (math.pow(r, i) / math.factorial(i))*(math.factorial(n) / math.factorial(n-i))
        i = i+1
    i = m + 1; j = 1
    while(i <= n):
        sum += (math.pow(r, i) / (math.factorial(m)*math.pow(m, j)))*(math.factorial(n) / math.factorial(n-i))
        i=i+1; j=j+1
    return(1.0/sum)

Po_list = []
Nprost_list = []
k_list = []

def solveSecondTask():
    n = 37
    Ts = 7
    Tc = 266
    r = Ts/Tc
    i = 1
    while(i <= n):
        P0 = getP0ForCloseSystems(n, i, r)
        P0 = float('{:.3f}'.format(P0))
        Po_list.append(P0)

        #среднее число простаивающих каналов
        Nprost = n - getAvarageWorkChannels(n, i, r, P0)
        Nprost = float('{:.3f}'.format(Nprost))
        Nprost_list.append(Nprost)

        #среднее число занятых наладчиков
        k = getAvarageWorkers(n, i, r, P0)
        k = float('{:.3f}'.format(k))
        k_list.append(k)
        i=i+1

solveSecondTask()

'''Построение графиков'''

grafik()

z = [x for x in range(1,17)]

plt.plot(z, Nprost_list[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,Nprost_list):
    plt.text(i, j, str(j))
plt.savefig('6(2)_Cреднее число простаивающих каналов.png')

grafik()

z = [x for x in range(1,17)]

plt.plot(z, k_list[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z, k_list):
    plt.text(i, j, str(j))
plt.savefig('6(2)_Cреднее число занятых наладчиков.png')

