# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 10:19:29 2017

@author: Lenovo-Y430p
"""

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  
#from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.axes_grid.axislines import SubplotZero
fig = plt.figure()
ax = SubplotZero(fig, 2, 2, 1)
ax1 = fig.add_subplot(ax)
#rect=[0.1,0.1,0.8,0.8]
#axprops = dict(xticks=[], yticks=[])

#ax0=fig.add_axes(rect, label='ax0',**axprops)
imgP = plt.imread("面积11.jpg")
ax1.imshow(imgP/256)
#ax1=fig.add_axes(rect, label='ax1',frameon=False)
#x = np.linspace(0,10,100)
#y = math.sin(x)
#ax1.plot(x,y)
ax1.set_title(" 10mm2 in 0.5h")
#ax1.set_ylim([-5,12])
ax = SubplotZero(fig, 2, 2, 2)
ax2 = fig.add_subplot(ax)
imgP = plt.imread("面积2211.jpg")
ax2.imshow(imgP/256)
ax2.set_title(" 15mm2 in 0.5h")
ax2.set_xlim([0,550])
ax = SubplotZero(fig, 2, 2, 3)
ax3 = fig.add_subplot(ax)
imgP = plt.imread("浓度11.jpg")
ax3.imshow(imgP/256) 
ax3.set_title(" 5g/l Nano3 in 2h ")

ax = SubplotZero(fig, 2, 2, 4)
ax4 = fig.add_subplot(ax)
imgP = plt.imread("浓度22111.jpg")
ax4.imshow(imgP/256) 
ax4.set_title(" 10g/l Nano3 in 2h ")
ax4.set_xlim([0,550])
#ax2=fig.add_axes(rect, label='ax2',frameon=False,**axprops)
#shodow_x = np.array([4.2, 4.2, 5.7, 5.8])
#shodow_y = np.array([5.6, 7.2, 7.2, 5.5])
#ax2.set_xlim([-2,12])
#ax2.set_ylim([-5,12])
#ax2.fill(shodow_x, shodow_y, linewidth=0, alpha=0.4, color='r')
#ax2.annotate('plot shadow area',xy=(5.7,7.2),xytext=(4.7,3.3),textcoords = 'offset points',arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),fontsize=20)

plt.show()
