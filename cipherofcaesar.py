#! /usr/bin/env python3

import string

def encoder(text, key):
    "Function encoder. Adds a key in the letters and print"
    text.split()
    print(''.join(
        list(map(lambda x: chr(ord(x) + key) if x.isalpha() else x, text))))

def decoder(text):
    "Function decoder"
    letter = max(string.ascii_lowercase, key=lambda ch: text.lower().count(ch)) #find most popular letter
    key = ord(letter.lower())-101 #compare with 'e'
    for letters in text:
        if ord(letters)<64 and ord(letters)>91:  #if letter in the text in uppercase
            deletters = ord(letters) - 32 - key
        else:
            deletters = ord(letters) - key
        print(chr(deletters), end='')

if __name__ == '__main__':
    try:
        flag = int(input("Enter 1 if you need an encoder, 2 if a decoder --> "))
        if flag == 1:
            text = input("Enter the string --> ")
            key = int(input("Enter the key --> "))
            encoder(text, key)
        else:
            text = input("Enter the string in English --> ")
            decoder(text)
    except ValueError:
         print("Incorrectly entered data")