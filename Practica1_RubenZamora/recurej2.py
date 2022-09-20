# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 13:51:54 2022

@author: r.zamora.2018
"""
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

def insertrec(l,n,i):
   if i < len(l):
        if l[i] < n:
            return insertrec(l,n,i+1)
        else:
            l.insert(i,n)
   else:
        l.append(n)
    
n=int(input())
c=lee_lista( n)
m=int(input())
insertrec(c,m,0)
imprime_lista(c)
