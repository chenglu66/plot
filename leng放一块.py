# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 09:40:24 2017

@author: Lenovo-Y430p
"""
import numpy as np
from matplotlib.pyplot import *
from matplotlib import rc

time = np.arange(10)
data1,data2 = np.random.random(10)*30,np.random.random(10)*100-10

fig = plt.figure()
ax = fig.add_subplot(111)

lns1 = ax.plot(time, data1, '-', label = 'data1')

ax2 = ax.twinx()
lns2 = ax2.plot(time, data2, '-r', label = 'data2')
ax2.tick_params(axis='y', colors='red') # 刻度颜色
ax2.spines['right'].set_color('red') # 纵轴颜色
setp(ax2.get_yticklabels(),color='r') # label颜色

lns = lns1+lns2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)

ax.grid()
ax.set_xlabel("Time")
ax.set_ylabel(r"Radiation ")
ax2.set_ylabel(r"Temperature")

ax2.set_ylim(-20,100)
ax.set_ylim(0, 35)
