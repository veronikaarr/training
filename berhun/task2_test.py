#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import numpy as np
import copy

'''your_list - общая матрица'''

with open('82-1_q.csv', "r", encoding='utf-8') as f:
    reader = csv.reader(f)
    your_list = list(reader)
    your_list_iter = list(your_list)
    for i in range(len(your_list)):
        your_list[i] = list(map(int, your_list[i])) #текст из csv сделали цифрами
        your_list_iter[i] = list(map(int, your_list[i]))

'''создание двумерного массива'''
R = [[0] * 26 for i in range(7)]
R_ = [[0] * 5 for i in range(5)]
a = 0
R_group = []


def summator(value_fix, gr):
    summ = 0
    '''проходимся по номерам не первой группы'''
    for i in groups_result[gr]:
        summ = summ + your_list_iter[value_fix][i]
    return (summ)

'''line_gr - номер 'первой' группы (группы по линии)
line_val - берутся все элементы из 'первой группы' (по этому индексу)
col_gr - номер 'не первой группы' (группы по столбцу)
col_val - берутся эл-ты из этой группы
'''

def iteration():
    a = 0; b = 0
    '''здесь groups_result, потому что проходимся по номерам группы'''
    for line_gr in range(len(groups_result)):
        flag = 0
        #max_el_list.clear()
        #ind_el_list.clear()
        groups_result_copy = copy.deepcopy(groups_result)
        while(flag != 1):
            b = 0
            for line_val in groups_result_copy[line_gr]:
                a = 0
                '''считаем суммы по формуле'''
                '''такой же цикл, но только не берутся во внимание те группы, где индекс совпадает с
                индексом, подсчитанным в предыдущем цикле'''
               # print('eto R = ', R)
                for col_gr in range(len(groups_result_copy)):
                    for col_val in groups_result_copy[col_gr]:
                        if line_gr != col_gr:
                            '''у сумматора - всегда первый эл-т - первая группа, второй - 'не первая группа'''
                            R[b][a] = (summator(line_val,col_gr)  #
                                       - summator(line_val,line_gr)) + \
                                      (summator(col_val,line_gr) -
                                       summator(col_val,col_gr)) - \
                                      2 * your_list_iter[line_val][col_val]
                            print('Мы здесь')
                            #print(R[a][b], 'eto R')
                           # print('num gr p {0}, num gr q {1}'.format(line_gr,col_gr))
                            #print('k = {0} j = {1}'.format(line_val,col_val))
                            #print('a = ',a)
                           # print('b = ',b)
                            a = a + 1
                b = b + 1
            print('\n')
          #  print("Hello, R = ", np.array(R))
            '''поиск максимального эл-та, определение его местоположения в первой группе)'''
            max_el_list = []
            ind_el_list = []
            for m in range(len(R)):
                max_el = max(R[m])
                #print('Максимальный элемент {0} найден здесь {1}'.format(max_el, R[m]))
                max_el_list.append(max_el)
                ind_el = R[m].index(max_el)
                ind_el_list.append(ind_el)
            print('max_el_list = ', max_el_list)
            max_el_res = max(max_el_list)
            '''если он найден и ненулевой'''
            if max_el_res > 0:
                print('max_el_res = ', max_el_res)
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
               # print('А это groups_result = ', groups_result)
                for gr in range(len(groups_result_copy)):
                    '''длина группы'''
                    print('start ---------------------------------------')
                    gr_sum = len(groups_result_copy[gr]) - 1
                    print('gr_sum = ',gr_sum)
                    '''длина всех эл-ов группы'''
                    gr_sum_al = gr_sum_al + gr_sum
                    print('column_max = ', column_max)

                    if gr_sum_al > column_max:
                        print('gr_sum_al = ', gr_sum_al)
                        gr_max_el_back = gr_sum_al - column_max

                        print('gr_max_el_back = ',gr_max_el_back)
                        gr_max_el = gr_sum - gr_max_el_back
                        print('gr_max_el = ', gr_max_el)
                        print('end ---------------------------------------')
                        break
                 #print('ono',gr, gr_max_el_back)
                print('Группа для рассмотрения: ', line_gr)
                #print(groups_result_copy[gr][gr_max_el])
                #print('line_gr = {0}, line_max = {1}'.format(line_gr, line_max))
                #replace1 = groups_result_copy[line_gr][line_max]

                #print('groups_result_copy = ', groups_result_copy)
                print('gr = ', gr)

                replace1 = groups_result_copy[gr][gr_max_el]
                replace2 = groups_result_copy[line_gr][line_max]
                print('replace1 = {0}, replace2 = {1}'.format(replace1, replace2))
                print('Это относится к replace1: gr = {0}, gr_max_el = {1}, line_gr = {2}, line_max = {3}'.
                      format(gr, gr_max_el, line_gr, line_max))
                '''без двух последующих строк replace1 = 11, replace2 = 1
                потом почему-то они становятся 25 и 24
                однозначно здесь происходит что-то нечистое'''
                '''gr - группа из столбца
                line_gr - группа из строки'''
                groups_result_copy[gr][gr_max_el] = replace2
                groups_result_copy[line_gr][line_max] = replace1
                print('again: replace1 = {0}, replace2 = {1}'.format(replace1, replace2))

                print('after groups_result_copy = ',groups_result_copy)

                '''меняем местами строки и столбцы в матрице'''

                print('before your_list_iter = ', np.array(your_list_iter))

                print('groups_result_copy = ',groups_result_copy)
                for j_ in range(len(groups_result_copy[line_gr])):
                    your_list_iter[j_][replace1] = your_list_iter[j_][replace2]
                    print('Это такой R1 {0}, от {1}, {2}'.format(your_list_iter[j_][replace1], j_, replace1))

                for j_1 in range(len(groups_result_copy[line_gr])):
                    your_list_iter[j_1][replace2] = your_list_iter[j_1][replace1]
                    print('Это такой R2 {0}, от {1}, {2}'.format(your_list_iter[j_1][replace2], j_1, replace2))

                print('after your_list_iter = ', np.array(your_list_iter))

                R[replace1] = copy.deepcopy(R[replace2])
                R[replace2] = copy.deepcopy(R[replace1])
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


groups_result = [[0,1],[2,3,4],[5,6,7]]

print('groups_result = ', groups_result)

iteration()

