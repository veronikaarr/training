#! /usr/bin/env python3
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
    try:
        for i in Fibonacci(int(input("Введите число -> "))):
           print(i)
    except ValueError:
        print("Это не цифра!")