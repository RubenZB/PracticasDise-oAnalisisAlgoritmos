# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 18:11:27 2022

@author: r.zamora.2018
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 13:51:54 2022

@author: Usuario
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
        
def sortrec(l,p):
    if(len(l)==0):
        return p
    else:
        n = l.pop(0)
        if(len(p)==0):
            p.insert(0,n)
            return sortrec(l, p)
        else:
            insertrec(p,n,0)
            return sortrec(l, p)
            
def insertrec(l,n,i):
   if i < len(l):
        if l[i] < n:
            return insertrec(l,n,i+1)
        else:
            l.insert(i,n)
   else:
        l.append(n)

n=int(input())
c=lee_lista(n)
b=[]
sortrec(c,b)
imprime_lista(b)
