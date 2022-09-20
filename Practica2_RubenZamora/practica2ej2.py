# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:45:30 2022

@author: Usuario
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon


def sierpinski_carpet(ax, p, n, size):
 if n > 0:
     ax.add_patch(RegularPolygon(p,3,size/2,fill=False,orientation=np.pi,linewidth=0.5))
     q = np.array ([[0], [size/2]])
     sierpinski_carpet(ax, p + q, n - 1, size / 2)
     cateto = np.sqrt((size/2)**2 - (size/4)**2)
     q = np.array ([[-cateto], [-size/4]])
     sierpinski_carpet(ax, p + q, n - 1, size / 2)
     q = np.array ([[cateto], [-size/4]])
     sierpinski_carpet(ax, p + q, n - 1, size / 2)

fig = plt.figure()
fig.patch.set_facecolor('white')
ax = plt.gca()
p = np.array ([[0], [0]])
print("Orden del triangulo:")
n=int(input())
sierpinski_carpet(ax, p,n, 1)
ax.add_patch(RegularPolygon((0,0),3,1,fill=False,linewidth=0.5))
plt.axis('equal')
plt.axis('off')
plt.show()