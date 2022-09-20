# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:16:45 2022

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


def mochiladoble(i,p, c1,c2, vactual , opt_v):
    if i == len(p):
        if vactual > opt_v:
            opt_v = vactual
    else:
        for k in range(0, 3):
            if k==0 or k==1:
                if k * p[i] <= c1:
                    nc1 = c1 - k * p[i]
                    nvactual = vactual + k * p[i]
                    opt_v = mochiladoble(i + 1,p, nc1, c2, nvactual , opt_v)
            else:
                kaux = k-1
                if kaux * p[i] <= c2:
                    nc2 = c2 - kaux * p[i]
                    nvactual = vactual + kaux * p[i]
                    opt_v = mochiladoble(i + 1,p,c1, nc2 , nvactual, opt_v)
    return opt_v



n=int(input())
p = lee_lista(n)
c = lee_lista(2)
print(mochiladoble(0,p, c[0],c[1],0,-1))