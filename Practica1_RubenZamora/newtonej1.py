# -*- coding: utf-8 -*-

def newton(x,a):
    funcion = x**2-a
    derivada = 2*x
    epsilon = 1E-6
    
    if (a == 0):
     return a
    elif (funcion >= -epsilon) and (funcion <= epsilon):
        return x
    else:
        z = x-(funcion/derivada)
        return newton(z,a)
i = float(input())
print("%.4F"% newton(i,i))