#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import numpy as np
import copy

'''your_list - общая матрица
'''

with open('82-1.csv', "r", encoding='utf-8') as f:
    reader = csv.reader(f)
    your_list = list(reader)
    your_list_iter = list(your_list)
    for i in range(len(your_list)):
        your_list[i] = list(map(int, your_list[i])) #текст из csv сделали цифрами
        your_list_iter[i] = list(map(int, your_list[i]))

sigma = []; for_del_ind = []

def find_max_min():
    q=0
    q1 = 0
    sum_val = []
    print(for_del_notnull,'etoooo for deeeeeel\n')
    print(notnull,'notnuuul after for')
    '''если в предыдущий вызов найден эл-т для удаления'''
    if for_del_notnull != 0:
        '''обходим циклом по всему notnull'''
        for x1 in notnull:
            q = q + 1
            print(x1,'etoooooo x1')
            print(for_del_notnull,'etoooo for deeeeeel\n')
            if for_del_notnull == x1:
                q1 = q - 1
                print(q1, 'qqqqqqqqqq1\n')
                print(notnull,'notnuliiiiidze\n')
                del notnull[q1]
                del notnull_sum[q1]
                print('miii zdes\n')
    if for_del_el_not != 0:
        print('XAXAXAXAXA')
        '''обходим циклом по всему el_not_is_null_'''
        for x1 in el_not_is_null_:
            q = q + 1
            print(x1,'etoooooo x1')
            print(for_del_el_not,'etoooo for deeeeeel\n')
            if for_del_el_not == x1:
                q1 = q - 1
                print(q1, 'qqqqqqqqqq1\n')
                print(el_not_is_null_,'notnuliiiiidze\n')
                del el_not_is_null_[q1]
                del el_not_is_null_sum_[q1]
                print('miii zdes\n')
    print(notnull, 'noooootnuuul\n')
    print(notnull_sum, 'notnuuuuuuuulsuum\n')
        #notnull[for_del]
      #  notnull_sum.remove(for_del_value)
    '''проходимся по строкам с этими индексами'''
    if sign == 1:
        ind = 0
        for j in range(len(notnull)):
            index = notnull[j]
            for_sum = [e for i, e in enumerate(your_list[index]) if i in notnull]
            '''записываем сумму элементов'''
            x = sum(for_sum)
            '''добавляем в общий список'''
            sum_val.append(x)
        print('kogo vihit:', notnull_sum)
        print('hto vihit:', sum_val)
        '''считаем разность сумм'''
        sigma = list(map(lambda a, b: a - b, notnull_sum, sum_val))
        print('Сигма', sigma)
        sigma_index = [(i, e) for i, e in zip(notnull, sigma) if e !=0]
        print("eto volshebny index:", notnull)
        print("res vihit:", sigma_index)
        ind_,val = max(sigma_index, key=lambda x: x[1])
        return (ind_, ind, notnull)
    else:
        ind_ = 0
        for j in range(len(el_not_is_null_)):
            index = el_not_is_null_[j]
            for_sum = [e for i, e in enumerate(your_list[index]) if i in el_not_is_null_]
            '''записываем сумму элементов'''
            x = sum(for_sum)
            '''добавляем в общий список'''
            sum_val.append(x)
        print('kogo vihitAXAXA:', el_not_is_null_sum_)
        print('hto vihit:', sum_val)
        '''считаем разность сумм'''
        sigma = list(map(lambda a, b: a - b, el_not_is_null_sum_, sum_val))
        print('Сигма', sigma)
        sigma_index = [(i, e) for i, e in zip(el_not_is_null_, sigma) if e !=0]
        print("eto volshebny index:", notnull)
        print("res vihit:", sigma_index)
        ind,val = min(sigma_index, key=lambda x: x[1])
        notnull.append(ind)
        print('Минимальное значение {0} для эл-та {1} \n'.format(val, ind))
        print('etooo snova notnuuul', notnull)
        print(ind, 'eTTTTTTTTTTTTTTTTTTTTTTTT')
        return (ind_, ind, notnull)

'''создание двумерного массива'''
R = [[0] * 26 for i in range(7)]
R_ = [[0] * 5 for i in range(5)]
a = 0
R_group = []


def summator(value_fix, gr):
    summ = 0
    for i in groups_result[gr]:
        summ = summ + your_list_iter[value_fix][i]
    return (summ)

def iteration():
    a = 0; b = 0
    for line_gr in range(len(groups_result)):
        flag = 0
        #max_el_list.clear()
        #ind_el_list.clear()
        groups_result_copy = copy.deepcopy(groups_result)
        while(flag != 1):
            b = 0
            for line_val in groups_result[line_gr]:
                a = 0
                '''считаем суммы по формуле'''
                for col_gr in range(len(groups_result)):
                    for col_val in groups_result[col_gr]:
                        if line_gr != col_gr:
                           # print('a = {0}, b = {1}'.format(a,b))
                            R[b][a] = (summator(line_val,col_gr) - summator(line_val,line_gr)) + \
                            (summator(col_val,line_gr) - summator(col_val,col_gr)) - 2 * your_list_iter[line_val][col_val]
                           # print('num gr p {0}, num gr q {1}'.format(line_gr,col_gr))
                            #print('k = {0} j = {1}'.format(line_val,col_val))
                            #print('a = ',a)
                           # print('b = ',b)
                            a = a + 1
                b = b + 1
            print('\n')
            print("Hello, R")
            '''поиск максимального эл-та'''
            max_el_list = []
            ind_el_list = []
            for m in range(len(R)):
                max_el = max(R[m])
                max_el_list.append(max_el)
                ind_el = R[m].index(max_el)
                ind_el_list.append(ind_el)
            print('max_el_list = ', max_el_list)
            max_el_res = max(max_el_list)
            '''если он найден и ненулевой'''
            if max_el_res > 0:
                line_max = max_el_list.index(max_el_res)
                column_max = ind_el_list[line_max]
                print('naidenny el maximus = ',R[line_max][column_max])
                print(np.array(R))
                print('line_max = ',line_max)
                print('column_max = ', column_max)

                '''произвести замену в списке списков'''
                gr_sum_al = 0
                gr_max_el = 0
                gr = 0
                #copy.deepcopy(a)
               # groups_result_copy = groups_result[:]
                print('Это тот groups_result_copy, что не удаляется = ',groups_result_copy)
                print('А это groups_result = ', groups_result)
                for gr in range(len(groups_result_copy)):
                    if gr == line_gr:
                        continue
                    '''длина группы'''
                    gr_sum = len(groups_result_copy[gr])
                    print('gr_sum = ',gr_sum)
                    '''длина всех эл-ов группы'''
                    gr_sum_al = gr_sum_al + gr_sum
                    if gr_sum_al > column_max:
                        print('gr_sum_al = ', gr_sum_al)
                        gr_max_el_back = gr_sum_al - column_max
                        print('column_max = ',column_max)
                        print('gr_max_el_back = ',gr_max_el_back)
                        gr_max_el = gr_sum - gr_max_el_back
                        break
                print('ono',gr, gr_max_el_back)
                print('Группа для рассмотрения: ', line_gr)
                #print(groups_result_copy[gr][gr_max_el])
                #print('line_gr = {0}, line_max = {1}'.format(line_gr, line_max))
                #replace1 = groups_result_copy[line_gr][line_max]
                print('before groups_result_copy = ', groups_result_copy)

                replace1 = groups_result_copy[gr][gr_max_el_back]
                replace2 = groups_result_copy[line_gr][line_max]
                print('replace1 = {0}, replace2 = {1}'.format(replace1, replace2))
                '''без двух последующих строк replace1 = 11, replace2 = 1
                потом почему-то они становятся 25 и 24
                однозначно здесь происходит что-то нечистое'''
                '''gr - группа из столбца
                line_gr - группа из строки'''
                groups_result_copy[gr][gr_max_el_back] = replace2
                groups_result_copy[line_gr][line_max] = replace1
                print('again: replace1 = {0}, replace2 = {1}'.format(replace1, replace2))

                print('after groups_result_copy = ',groups_result_copy)
                #groups_result_copy.clear()
                print('a = {0}, b = {1}'.format(a, b))
            else:
                flag = 1
            print(np.array(R))

            #print(groups_result_copy)
            '''очищаем список R'''
            for i in range(len(R)):
                for j in range(len(R[i])):
                    R[i][j] = 0
            '''очищаем список group_res_copy'''
        for i in range(len(groups_result_copy)):
            for j in range(len(groups_result_copy[i])):
                groups_result_copy[i][j] = 0
    print('line_gr = {0}, line_val = {1}, col_gr = {2}, col_val = {3}'.format(line_gr,line_val,col_gr,col_val))
    #print('etoo a1 = {0}, etoo b1 = {1}'.format(a, b))
   # print(np.array(R))
    print('\n')

    d_i = 0
    '''for d1 in range(len(R)):
        for d2 in R[d1]:
            print('d1 = {}, d2 = {}'.format(d1,d2))
    print('Hello, R1 = {}'.format(R_)) '''


def find_min_string():
    values_sum = list(map(lambda x: np.sum(x), your_list)) #суммы всех строчек
    print('Сумма всех строчек:',values_sum)
    values_sumn = np.array(values_sum)
    value_min_sum = np.min(values_sumn[np.nonzero(values_sumn)])
    index_min = values_sum.index(value_min_sum)  #найти среди них минимальную
    print('Строка с минимальной суммой:',index_min)
    notnull_ = [i for i, e in enumerate(your_list[index_min]) if e != 0] #записываем все ненулевые эл-ты
    notnull_.append(index_min)
    notnull_.sort()
    print('Индексы смежных элементов:', [i for i in notnull_ if i != index_min])
    print(notnull_,'notnnnnnnnnnul')
    notnull_sum_ = [e for i, e in enumerate(values_sum) if i in notnull_] #записываем все суммы строк с этими индексами

    '''а теперь делаем то же самое для несмежных эл-ов'''
    stroki_not_null = [i for i, e in enumerate(values_sumn) if e != 0]  # записываем все ненулевые строки
    '''индексы всех элементов не из группы'''
    el_not_is_null_ = list(set(stroki_not_null) - set(notnull_))
    print(el_not_is_null_, 'etoooooooooooooooo2 !!!!!!!!!!!!!!!!!!!!!!')
    '''суммы для всех несмежных строк'''
    el_not_is_null_sum_ = [e for i, e in enumerate(values_sum) if i in el_not_is_null_]
    return (values_sum, notnull_, value_min_sum, notnull_sum_, el_not_is_null_, el_not_is_null_sum_)

groups = [4,5,7,7,7]
#f = groups[0]

print(np.array(your_list))
print('\n')
for_del_notnull = 0
for_del_el_not = 0
qwe = 0
k = 0
'''для элементов, которые мы удаляем'''
notnull_func = []
groups_result = []

'''проход по всем группам'''
for j in groups:
    print('etoooo j:',j)
    '''поиск миним элемента в группе'''
    values_sum, notnull, value_min_sum, notnull_sum, el_not_is_null_, el_not_is_null_sum_= find_min_string()
    print(notnull_func,'notnuuuuul in for')
    '''пока кол-во эл-ов в группе не станет равным заданному числу'''
    while(len(notnull)!= j):
        qwe = qwe +1
        print(j,'etooooo j\n')
        print(len(notnull),'etoooooooo len\n')
        print(notnull,'eTOOOOOOO notnull')
        sign = np.sign(len(notnull) - j) #узнаем, больше или меньше число эл-ов в строке, чем очередное
        # число из списка гр-п
        print(sign,'siiign\n')
        '''находим минимальное или максимальное число, в зависимости от sigma'''
        for_del_notnull, for_del_el_not, notnull_func = find_max_min()
        print(notnull_func,'etoOOOOO notnuuul_func')
        '''удалённые элементы добавляем в список'''
        for_del_ind.append(for_del_notnull)
       # print('do delete:',np.array(your_list))
        #    print('eto for_del:', for_del, i)
       # print('after del:')
        #for k in range(len(your_list)):
           # if your_list[k]:
           #     print(your_list[k])
        print('\n')
    k = k + 1
    print('{0} groop------------------------------------: {1}'.format(k, [i for i in notnull]))
    groups_result.append(notnull)
    for h in range(len(your_list[0])):
        for o in notnull_func:
            your_list[o][h] = 0
            your_list[h][o] = 0

print("\n Uraaaaa, it is result posled etap!!! {} \n".format(groups_result))


iteration()

