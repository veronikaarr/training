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
for_del = 0
sigma = []; for_del_ind = []

def find_max_min():
    sum_val = []
    indexs = [x for x, y in notnull]  #записываем индексы изначальной строки
    notnull.pop()  #после удаляем индекс изнач строки
    notnull_sum = [e for i, e in enumerate(values_sum) if i in indexs] #записываем все суммы строк с этими индексами
    notnull_sum.remove(value_min_sum)
    for j in range(len(notnull)):  #проходимся по строкам с этими индексами
        index, value = notnull[j]
        for_sum = [e for i, e in enumerate(your_list[index]) if i in indexs]
        x = sum(for_sum) #записываем сумму элементов
        sum_val.append(x)  #добавляем в общий список
    print('kogo vihit:',notnull_sum)
    print('hto vihit:',sum_val)
    sigma = list(map(lambda a, b: a - b, notnull_sum, sum_val)) #считаем разность сумм
    print('Сигма',sigma)

    sigma_index = [(i,e) for i,e in zip(indexs,sigma)]
   # print("res vihit:",sigma_index)
    if sign == 1:
        ind,val = max(sigma_index, key=lambda x: x[1])
    else:
        ind,val = min(sigma_index, key=lambda x: x[1])
    return (ind, indexs)

def find_min_string():
    values_sum = list(map(lambda x: np.sum(x), your_list)) #суммы всех строчек
    print('Сумма всех строчек:',values_sum)
    values_sumn = np.array(values_sum)
    value_min_sum = np.min(values_sumn[np.nonzero(values_sumn)])
    index_min = values_sum.index(value_min_sum)  #найти среди них минимальную
    print('Строка с минимальной суммой:',index_min)
    notnull = [(i, e) for i, e in enumerate(your_list[index_min]) if e != 0] #записываем все ненулевые эл-ты
    notnull.append((index_min, your_list[index_min]))
    print('Индексы смежных элементов:', [i for i, e in notnull if i != index_min])
    # из неё в список
    return (values_sum,notnull,value_min_sum)

#your_list = np.array(your_list)
groups = [4,5,7,7,7]
#f = groups[0]

print(np.array(your_list))
print('\n')

for j in groups:
    print('etoooo j:',j)
    values_sum, notnull, value_min_sum = find_min_string()
    while(len(notnull) != j):
       # print(j,'eeetoooo takoe j')
        sign = np.sign(len(notnull) - j) #узнаем, больше или меньше число эл-ов в строке, чем очередное число из списка гр-п
        print(sign,'siiign')
        for_del, indexss = find_max_min()
        print(for_del)
        for_del_ind.append(for_del)
       # print('do delete:',np.array(your_list))
       # print('eto indexs:',indexss)
        for i in range(len(your_list[for_del])):
            your_list[for_del][i] = 0
            your_list[i][for_del] = 0
        #    print('eto for_del:', for_del, i)
        values_sum, notnull,value_min_sum = find_min_string()
       # print('after del:')
        #for k in range(len(your_list)):
           # if your_list[k]:
           #     print(your_list[k])
        print('\n')
    print('First groop------------------------------------:', [i for i,e in notnull])
    for h in range(len(your_list[for_del])):
        for i in for_del_ind:
            your_list[i][h] = 0
            your_list[h][i] = 0