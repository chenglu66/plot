# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 23:02:18 2017

@author: Lenovo-Y430p
"""
import matplotlib.pyplot as plt
import numpy as np

def f(x,y): 
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)+5


xx,yy = np.meshgrid(np.linspace(-3,3,50),np.linspace(-3,3,50))
zz = f(xx,yy)
plt.imshow(zz,origin='lower',extent=[xx.min(), xx.max(), yy.min(), yy.max()])
