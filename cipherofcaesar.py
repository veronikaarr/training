#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import string

def encoder(text, key):
    """Function encoder. Adds a key in the letters and print
    If a letter has uppercase and value = letter - key goes beyond the bounds of the alphabet
    add to it 26 - so encryption of letters is provided only inside the alphabet.
    Similarly for a lowercase letter.
    If the character is not in the lowercase and not in the upper case, output it in its original form"""
    text.split()
    print(''.join(
        list(map(lambda x: chr(ord(x) - key) if (x.isupper() and ord(x) - key > 64)
        or (x.islower() and ord(x) - key > 96 )
        else (chr(ord(x) - key + 26) if x.isalpha()
              else x), text))))

def decoder(text):
    """ Function decoder. The position of the letters is determined by the ascii table.
    Find most popular letter.
    Compare of the position of the most popular letter with the position of the letter 'e' (in lower case).
    If the letter in the upper case is checked: if the value = letter + key does not go beyond the alphabet,
    add the key and print, otherwise - subtract the alphabet """
    letter = max(string.ascii_lowercase, key=lambda ch: text.lower().count(ch))
    key = 101 - ord(letter.lower())
    for letters in text:
        if letters.isupper():
            if 64 < ord(letters) + key < 91:
                letters = chr(ord(letters) + 32 + key)
            else:
                letters = сhr(ord(letters) + 32 + key - 26)
        elif letters.islower():
            if 97 < ord(letters) + key < 122:
                letters = chr(ord(letters) + key)
            else:
                letters = chr(ord(letters) + key - 26)
        print(letters,end='')

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
