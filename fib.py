# Задание от Кирилла: Напишите функцию чисел фибоначи на Python.
# Нужно ввести количество чисел, для которых будет расчитываться последовательность Фибоначчи

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def Fibonacci(n):
    a = b = 1
    for i in range(n):
        yield a
        c = a + b
        a = b
        b = c

for i in Fibonacci(input(u"Введите число -> ")):
    print(i)