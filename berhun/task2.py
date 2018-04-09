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

sigma = []; for_del_ind = []

def find_max_min():
    q=0
    q1 = 0
    sum_val = []
    print(for_del,'etoooo for deeeeeel\n')
    print(notnull,'notnuuul after for')
    '''если в предыдущий вызов найден эл-т для удаления'''
    if for_del != 0:
        '''обходим циклом по всему notnull'''
        for x1, x2 in notnull:
            q = q + 1
            print(x1,'etoooooo x1')
            print(for_del,'etoooo for deeeeeel\n')
            if for_del == x1:
                q1 = q - 1
                print(q1, 'qqqqqqqqqq1\n')
                print(notnull,'notnuliiiiidze\n')
                del notnull[q1]
                del notnull_sum[q1]
                print('miii zdes\n')
    print(for_del,'fooooordeeeel\n')
    print(notnull, 'noooootnuuul\n')
    print(notnull_sum, 'notnuuuuuuuulsuum\n')
        #notnull[for_del]
      #  notnull_sum.remove(for_del_value)
    '''проходимся по строкам с этими индексами'''
    for j in range(len(notnull)):
        index, value = notnull[j]
        for_sum = [e for i, e in enumerate(your_list[index]) if i in indexs]
        '''записываем сумму элементов'''
        x = sum(for_sum)
        '''добавляем в общий список'''
        sum_val.append(x)
    print('kogo vihit:',notnull_sum)
    print('hto vihit:',sum_val)
    '''считаем разность сумм'''
    sigma = list(map(lambda a, b: a - b, notnull_sum, sum_val))
    print('Сигма',sigma)
    sigma_index = [(i,e) for i,e in zip(indexs,sigma)]
   # print("res vihit:",sigma_index)
    if sign == 1:
        ind,val = max(sigma_index, key=lambda x: x[1])
    else:
        ind,val = min(sigma_index, key=lambda x: x[1])
    print('Максимальное значение {0} для эл-та {1} \n'.format(val, ind))
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
    indexs = [x for x, y in notnull]  #записываем индексы изначальной строки
    print(notnull,'notnnnnnnnnnul')
    notnull.pop()  #после удаляем индекс изнач строки
    print(notnull,'notnnnnnnnnnul2')
    notnull_sum = [e for i, e in enumerate(values_sum) if i in indexs] #записываем все суммы строк с этими индексами
    notnull_sum.remove(value_min_sum)
    # из неё в список
    return (values_sum, notnull, value_min_sum, indexs, notnull_sum)

#your_list = np.array(your_list)
groups = [4,5,7,7,7]
#f = groups[0]

print(np.array(your_list))
print('\n')
for_del = 0
qwe = 0

'''проход по всем группам'''
for j in groups:
    print('etoooo j:',j)
    '''поиск миним элемента в группе'''
    values_sum, notnull, value_min_sum, indexs, notnull_sum = find_min_string()
    print(notnull,'notnuuuuul in for')
    '''пока кол-во эл-ов в группе не станет равным заданному числу'''
    while(qwe != 7):
        qwe = qwe +1
        print(j,'etooooo j\n')
        print(len(notnull),'etoooooooo len\n')
        sign = np.sign(len(notnull) - j) #узнаем, больше или меньше число эл-ов в строке, чем очередное
        # число из списка гр-п
        print(sign,'siiign\n')
        '''находим минимальное или максимальное число, в зависимости от sigma'''
        for_del, indexss = find_max_min()
        print(for_del)
        '''удалённые элементы добавляем в список'''
        for_del_ind.append(for_del)
       # print('do delete:',np.array(your_list))
       # print('eto indexs:',indexss)
        for p in range(len(your_list[for_del])):
            your_list[for_del][p] = 0
            your_list[p][for_del] = 0
        #    print('eto for_del:', for_del, i)
       # print('after del:')
        #for k in range(len(your_list)):
           # if your_list[k]:
           #     print(your_list[k])
        print('\n')
    print('First groop------------------------------------:', [i for i,e in notnull])
    for h in range(len(your_list[for_del])):
        for o in for_del_ind:
            your_list[o][h] = 0
            your_list[h][o] = 0