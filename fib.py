#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Задание от Кирилла: Напишите функцию чисел фибоначи на Python.
# Нужно ввести количество чисел, для которых будет расчитываться последовательность Фибоначчи

def Fibonacci(n):
    a = b = 1
    for _ in range(n):
        yield a
        c = a + b
        a = b
        b = c

if __name__ == '__main__':
    for i in Fibonacci(eval(input("Введите число -> "))):
        print(i)