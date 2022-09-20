# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 19:17:03 2022

@author: Usuario
"""
from sys import setrecursionlimit
def lee_lista(n):
    a = []
    if n>0:
        cadenaEntrada = input()
        for i in range(0, n): 
            elemento = int(cadenaEntrada.split(" ")[i])
            a.append(elemento)
    return a

def imprime_lista(a):
    n = len(a)
    if n==0:
        pass
    elif n==1:
        print(a[0])
    else:
        print(a[0],end='')
        print(' ',end='')
        imprime_lista(a[1:])
        

def ordenacion(l):
    if len(l) > 1:
        mit = len(l) // 2
        a = l[:mit]
        b = l[mit:]
        ordenacion(a)
        ordenacion(b)
        i = 0
        j = 0
        k = 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                if ((a[i] % 2) != 0 or (b[j] % 2) == 0):
                    l[k] = a[i]
                    i += 1
                else:
                    l[k] = b[j]
                    j += 1
            else:
                if ((b[j] % 2) != 0 or (a[i] % 2) == 0):
                    l[k] = b[j]
                    j += 1
                else:
                    l[k] = a[i]
                    i += 1
            k += 1
        while i < len(a):
            l[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            l[k]=b[j]
            j += 1
            k += 1
        
setrecursionlimit(10500)
n=int(input())
c=lee_lista(n)
ordenacion(c)
imprime_lista(c)      