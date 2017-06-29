# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 15:33:41 2017

@author: Lenovo-Y430p
"""
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
ycord0=[110,80,30,18,8]
label=[10,20,90,100,120]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(label,ycord0, '--',marker=r'$\boxdot$', markersize=20,
        linewidth=2, alpha=0.6, color='g', label=u'error')
ax.scatter(label,ycord0 ,marker='s', s=100)
lns1 = ax.plot(label,ycord0,'-', label = 'error')
ax.set_title(u'The relationship between depth and area ')
ax.annotate(u'As the area increases, the processing depth is decreasing',
         xy=(20,80), xycoords='data',
         xytext=(10, 20), textcoords='offset points', fontsize=12,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
ax.set_xlabel("area(mm2)")
ax.set_ylabel(r"depth(um)")
ax.grid()
lns1 = ax.plot(label,ycord0,'-', label = 'area')
