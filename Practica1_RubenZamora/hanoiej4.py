# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 13:33:13 2022

@author: r.zamora.2018
"""

def hanoi(n,o,d,a):
    if (n>0)and(n<=9):
        if n==1:
            print('Mueve disco ',n,' desde torre ',o,' a torre ',d)
            print('Mueve disco ',n,' desde torre ',d,' a torre ',a)
        else:
            hanoi(n-1,o,d,a)
            print('Mueve disco ',n,' desde torre ',o,' a torre ',d)
            hanoi(n-1,a,d,o)
            print('Mueve disco ',n,' desde torre ',d,' a torre ',a)
            hanoi(n-1,o,d,a)
            
        
        
n = int(input())
hanoi(n,'1','2','3')