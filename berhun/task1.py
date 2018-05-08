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
n = 15
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


'''Второй пункт'''

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


'''Четвёртый пункт'''

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
plt.savefig('3_Длина_оч.png')

grafik()

plt.plot(z, q_list[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,q_list):
    plt.text(i, j, str(j))
plt.savefig('3_Коэф_загр.png')

grafik()

plt.plot(z, Tsr_list[0:n], color='red', marker='o', linestyle='--', markerfacecolor='blue')
for i,j in zip(z,Tsr_list):
    plt.text(i, j, str(j))
plt.savefig('3_Время_ожид.png')


'''Пятый пункт'''

eps = pow(10, -8)
Po_5 = 100
Po_5_next = 0
denomin_list = []
b_list = []
Po_5_list = []
m = 2
n = 16

def Po(n_):
    Po_promej1_5 = [math.pow(a, x) / math.factorial(x) for x in range(1, n_)]
    term1 = sum(Po_promej1_5)
    m = 2
    print(m, 'm before')
    for i in range(1, m):
        for q in range(1, i):
            denomin = n_*nu + i * (1/Tw)
            denomin_list.append(denomin)
        op = reduce(lambda res, x: res * x, denomin_list, 1)
        print(op, 'op')
        b = math.pow(lamda, i) / op
        b_list.append(b)
    term2 = math.pow(a, n_) * sum(b_list) /math.factorial(n)
    Po_5_next = 1 / (term1 + term2)
    m = m + 1
    print(m, 'm after')
    print(Po_5_next, 'Po_5_next')
    return (m, Po_5_next)

for i_ in range(1, n+1):
    m, Po_5_next = Po(i_)
    while(Po_5 - Po_5_next > eps):
        Po_promej1_5 = [math.pow(a, x) / math.factorial(x) for x in range(1, i_)]
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
        term2 = math.pow(a, i_) * sum(b_list) /math.factorial(i_)
        Po_5 = Po_5_next
        Po_5_list.append(Po_5)
        Po_5_next = 1 / (term1 + term2)
        m = m + 1
        print(m, 'm after')
        print(Po_5_next, 'Po_5_next')
       # print(Po_5, 'Po_5')

   # print('\netooooo POOOOOOO', Po_5)

print(Po_5_list, 'Po5___')

Loh_5_sum = 0
Loh_5_list = []

n = 16

for k_ in range(1, n+1):
    for z in range(1, k_):
            Pn_5 = math.pow(a, k_+z) / (math.pow(z, k_) * math.factorial(z))
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
