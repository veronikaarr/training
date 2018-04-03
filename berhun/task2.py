#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import numpy as np

'''your_list - общая матрица
'''

with open('82-1.csv', "r", encoding='utf-8') as f:
    reader = csv.reader(f)
    your_list = list(reader)
    for i in range(len(your_list)):
        your_list[i] = list(map(int, your_list[i])) #текст из csv сделали цифрами

def maxx():
    sigmaa = [(9, 27), (13, 33), (15, 22), (24, 27), (25, 23), (26, 34), (28, 17), (29, 45)]
    print(max(sigmaa, key=lambda x: x[1]))

maxx()

#print(your_list)
sum_val = []
sigma = []

def find_max_min():
    indexs = [x for x, y in notnull]  #записываем индексы изначальной строки
    notnull_sum = [e for i, e in enumerate(values_sum) if i in indexs] #записываем все суммы строк с этими индексами
    for j in range(len(notnull)):  #проходимся по строкам с этими индексами
        index, value = notnull[j]
        x = sum([e for i, e in enumerate(your_list[index]) if i in indexs]) #записываем сумму элементов
        sum_val.append(x)  #добавляем в общий список
       # print(sum_val)
    sigma = list(map(lambda a, b: a - b, notnull_sum, sum_val)) #считаем разность сумм
    sigma_index = [(i,e) for i,e in zip(indexs,sigma)]
    print(sigma_index,"sf")
    #print(max(sigma_index, key=lambda x: x[1]))
    if sign == 1:
        max = sigma[0];pos = 0
        for i in range(len(sigma)):
            if sigma[i] > max:
                max = sigma[i]
                pos = i
    else:
        min = sigma[0];pos = 0
        for i in range(len(sigma)):
            if sigma[i] > min:
                min = sigma[i]
                pos = i
    return (pos)



#a = np.array(your_list)
#print(a)
values_sum = list(map(lambda x: np.sum(x), your_list)) #суммы всех строчек
index_min = values_sum.index(min(values_sum))  #найти среди них минимальную
#print(your_list[index_min])
notnull = [(i, e) for i, e in enumerate(your_list[index_min]) if e != 0] #записываем все ненулевые эл-ты из неё в список
groups = [4,5,5,7,7]
f = groups[0]
#while(len(notnull) != f):
sign = np.sign(len(notnull) - f) #узнаем, больше или меньше число эл-ов в строке, чем очередное число из списка гр-п
for_del = find_max_min()
#del notnull[1]
   # a = np.delete(a, 3, 0)  # delete second row of A
  #  print(a)
   # a = np.delete(a, for_del, 1)  # delete third row of B
