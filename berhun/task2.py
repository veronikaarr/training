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
        for x1 in notnull:
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
        index = notnull[j]
        for_sum = [e for i, e in enumerate(your_list[index]) if i in notnull]
        '''записываем сумму элементов'''
        x = sum(for_sum)
        '''добавляем в общий список'''
        sum_val.append(x)
    print('kogo vihit:',notnull_sum)
    print('hto vihit:',sum_val)
    '''считаем разность сумм'''
    sigma = list(map(lambda a, b: a - b, notnull_sum, sum_val))
    print('Сигма',sigma)
    sigma_index = [(i,e) for i,e in zip(notnull,sigma)]
    print("eto volshebny index:", notnull)
    print("res vihit:",sigma_index)
    if sign == 1:
        ind,val = max(sigma_index, key=lambda x: x[1])
    else:
        ind,val = min(sigma_index, key=lambda x: x[1])
    print('Максимальное значение {0} для эл-та {1} \n'.format(val, ind))
    print('etooo snova notnuuul', notnull)
    return (ind, notnull,notnull_sum)


def find_min_string():
    values_sum = list(map(lambda x: np.sum(x), your_list)) #суммы всех строчек
    print('Сумма всех строчек:',values_sum)
    values_sumn = np.array(values_sum)
    value_min_sum = np.min(values_sumn[np.nonzero(values_sumn)])
    index_min = values_sum.index(value_min_sum)  #найти среди них минимальную
    print('Строка с минимальной суммой:',index_min)

    notnull_f = [i for i, e in enumerate(your_list[index_min]) if e != 0] #записываем все ненулевые смежные эл-ты
    notnull_f.append(index_min)
    notnull_f.sort()
    print(notnull_f, 'srAAAAAAAAvn1')
    print('Индексы смежных элементов:', [i for i in notnull_f if i != index_min])
    print(notnull_f,'notnnnnnnnnnul')
    notnull_sum_f = [e for i, e in enumerate(values_sum) if i in notnull_f] #записываем все суммы строк с этими индексами
   # notnull_sum.remove(value_min_sum)
    # из неё в список

    '''а теперь делаем то же самое для несмежных эл-ов'''
    stroki_not_null = [i for i, e in enumerate(values_sumn) if e != 0] #записываем все ненулевые строки
    '''индексы всех элементов не из группы'''
    el_not_is_null_f = list(set(stroki_not_null) - set(notnull_f))
    print(el_not_is_null_f, 'etoooooooooooooooo2 !!!!!!!!!!!!!!!!!!!!!!')
    '''суммы для всех несмежных строк'''
    el_not_is_null_sum_f = [e for i, e in enumerate(values_sum) if i in el_not_is_null_f]
    return (values_sum, notnull_f, value_min_sum, notnull_sum_f, el_not_is_null_f, el_not_is_null_sum_f)

#your_list = np.array(your_list)
groups = [4,5]
#f = groups[0]

print(np.array(your_list))
print('\n')
for_del = 0
qwe = 0
k = 0
notnull_func = []
notnull_func_all_delete_el = []
flat = []

'''проход по всем группам'''
for j in groups:
    print('etoooo j:',j)
    '''поиск миним элемента в группе'''
    values_sum, notnull_f_, value_min_sum, notnull_sum_f_, el_not_is_null_f_, el_not_is_null_sum_f_ = find_min_string()
    notnull = list(notnull_f_)
    print(notnull_f_,'notnuuuuul in for')
    '''пока кол-во эл-ов в группе не станет равным заданному числу'''
    while(len(notnull)!= j):
        qwe = qwe +1
        print(j,'etooooo j\n')
        print(len(notnull),'etoooooooo len\n')
        sign = np.sign(len(notnull) - j) #узнаем, больше или меньше число эл-ов в строке, чем очередное
        # число из списка гр-п
        print(sign,'siiign\n')
        '''находим минимальное или максимальное число, в зависимости от sigma'''
        if sign == 1:
            notnull = list(notnull)
            notnull_sum = list(notnull_sum_f_)
            for_del, notnull,notnull_sum = find_max_min()
        if sign == 0:
            notnull = list(el_not_is_null_f_)
            notnull_sum = list(el_not_is_null_sum_f_)
            for_del, notnull,notnull_sum = find_max_min()
        print(notnull,'etooooo notnuuul_func')
        '''удалённые элементы добавляем в список'''
        for_del_ind.append(for_del)
       # print('do delete:',np.array(your_list))
       # print('eto indexs:',indexss)
        #    print('eto for_del:', for_del, i)
       # print('after del:')
        #for k in range(len(your_list)):
           # if your_list[k]:
           #     print(your_list[k])
        print('\n')
    k = k + 1
    print('{0} groop------------------------------------: {1}'.format(k, [i for i in notnull]))
    #otnull_func = ','.join(notnull_func)
  #  if k == 1:
    flat.clear()
    notnull_func_all_delete_el.append(notnull)
    flat = [item for sublist in notnull_func_all_delete_el for item in sublist] #объединение списка списков
    # в один список
    for h in range(len(your_list[0])):
        for o in notnull:
            your_list[o][h] = 0
            your_list[h][o] = 0