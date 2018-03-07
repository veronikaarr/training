#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import string

#function encoder
def encoder(text, key):
    for q in text:
        if q.isalpha():
            print(chr(ord(q)+key),end='')
    print('\n')

#function decoder
def decoder(text):
    letter = max(string.ascii_lowercase, key=lambda ch: text.lower().count(ch)) #ищет наиболее часто встречающуюся букву
    print(letter)

if __name__ == '__main__':
    try:
        flag = int(input("Enter 1 if you need an encoder, 2 if the decoder --> "))
        if flag == 1:
            text = input("Enter the string --> ")
            key = int(input("Enter the key --> "))
            encoder(text, key)
        else:
            text = input("Enter the string in English --> ")
            decoder(text)
    except ValueError:
         print("Incorrectly entered data")