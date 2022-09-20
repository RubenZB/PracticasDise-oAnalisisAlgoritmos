# -*- coding: utf-8 -*-
"""
Created on Fri May  16 11:44:28 2022

@author: Usuario
"""

def lee_lista(n):
    a = []
    if n>0:
        cadenaEntrada = input()
        for i in range(0, n): 
            elemento = int(cadenaEntrada.split(" ")[i])
            if (elemento > 0) & (elemento <= 1000): #Lee numeros entre 1 y 1000
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
        
def minimaoperacion(l,sol,solu):
    if len(l)==1:
        return 0
    elif len(l)==2:
        solu = solu + (l[0]+l[1])
        return solu
    else:
            p1 = min(l)
            l.remove(p1)
            p2 = min(l)
            l.remove(p2)
            p3 = p1+p2
                
            l.append(p3)
            solu = p3 + solu
            return minimaoperacion(l,sol,solu)

n = int(input())
if (n > 0) & (n <= 100): #Lee numeros entre 1 y 100
    l = lee_lista(n)
    if(n == len(l)): #Comprobacion de que ningun valor de la lista se ha pasado del rango de 1 a 1000
     print(minimaoperacion(l, 0,0))

