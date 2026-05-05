#!/usr/bin/env python3

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

def generateKey(i):
    start = i
    key = "".join([alphabet[start:], alphabet[0:start]])
    return key

def encrypt(plain, key):
    ciphertext = ""
    for k in range(len(plain)):
        character = plain[k]
 
        if ord(character) <= 90 and ord(character) >= 65: #lowercase
            key = "".join([key[len(key)-1:],key[0:len(key)-1]])
            characterDecrypted = chr(ord(key[i])-32)
            i = alphabet.index(chr(ord(character)+32))
            ciphertext = "".join([ciphertext,characterDecrypted])

        elif ord(character) <= 122 and ord(character) >= 97:
            key = "".join([key[len(key)-1:],key[0:len(key)-1]])
            characterDecrypted = key[i]
            i = alphabet.index(character)
            
            ciphertext = "".join([ciphertext,characterDecrypted])
        else:
            ciphertext = "".join([ciphertext,character])
        
    return ciphertext

def decrypt(ciphertext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plain = ""
    
    for k in range(len(ciphertext)):
        character = ciphertext[k]
 
        # Gestione MAIUSCOLE
        if 65 <= ord(character) <= 90:
            # Ruoto la chiave esattamente come nell'encryption
            key = key[-1:] + key[:-1]
            # Cerco dove si trova il carattere (portato in minuscolo) nella chiave
            idx = key.index(chr(ord(character) + 32))
            # Risalgo alla lettera originale nell'alfabeto e la riporto in maiuscolo
            plain += chr(ord(alphabet[idx]) - 32)

        # Gestione minuscole
        elif 97 <= ord(character) <= 122:
            key = key[-1:] + key[:-1]
            idx = key.index(character)
            plain += alphabet[idx]
            
        # Caratteri speciali (spazi, numeri, ecc.)
        else:
            plain += character
        
    return plain


def handle():
    plaintextFLAG = "xcqv{gvyavn_zvztv_etvtddlnxcgy}"

    ciphertext = "xcqv{gvyavn_zvztv_etvtddlnxcgy}"
    for i in range(1,25):
        key = generateKey(i)
        flag = decrypt(ciphertext, key)
        print(flag)
    return





if __name__ == "__main__":
    handle()
