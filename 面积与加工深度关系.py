# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 13:09:38 2017

@author: Lenovo-Y430p
"""
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
ycord0=[0.2,2,24,60]
label=[5,10,15,20]
datamat=[30,100,300,670]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(label,ycord0, '--',marker=r'$\boxdot$', markersize=20,
        linewidth=2, alpha=0.6, color='g', label=u'error')
ax.scatter(label,ycord0 ,marker='s', s=100)
lns1 = ax.plot(label,ycord0,'--', label = 'error')
ax2 = ax.twinx()
ax2.scatter(label,datamat ,marker='s', s=100)
ax2.plot(label,datamat, marker=r'$\bullet$', markersize=20,
        linewidth=2, alpha=0.6, color='r', label=u'depth')
lns2 = ax2.plot(label, datamat, '-r', label = 'depth')
ax2.tick_params(axis='y', colors='red') # 刻度颜色
ax2.spines['right'].set_color('red') # 纵轴颜色
plt.setp(ax2.get_yticklabels(),color='r') # label颜色
lns = lns1+lns2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)
ax.set_xlabel("density(g/l)")
ax.set_ylabel(r"erroe% ")
ax2.set_ylabel(r"depth/um")
ax2.set_ylim(20,800)
ax.set_ylim(-5, 70)
ax.set_xlim(0,25)
ax.grid()
#ax.set_title(u'相同条件下电解质浓度与加工深度和加工精度的关系')
ax.set_title(u'The relationship between depth and error in differrnt dendity')
ax.annotate(u'the accuracy decreased greatly form this point',
         xy=(10,2), xycoords='data',
         xytext=(10, 20), textcoords='offset points', fontsize=10,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
#ax.plot([0,10],[2,2], color ='red', linewidth=1.5, linestyle="-.")      
ax2.annotate(u'efficiency is greatly improved form this point',
         xy=(15,300), xycoords='data',
         xytext=(10, 20), textcoords='offset points', fontsize=10,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
#ax2.plot([15,30],[300,300], color ='green', linewidth=1.5, linestyle="--")
plt.axes.labelsize=18
plt.show()