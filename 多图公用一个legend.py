# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 23:07:24 2017

@author: Lenovo-Y430p
"""
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.axislines import SubplotZero
import numpy as np
width = 1 # 两条柱之间的距离
num = 5 #柱的个数
ind = np.arange(num)

fig = plt.figure(figsize=(15, 4))
ax = SubplotZero(fig, 1, 3, 1)
ax1 = fig.add_subplot(ax)

means = [0.6481,0.6215,0.58,0.56,0.442] 
stds = [0.0129,0.0119,0.01,0.009,0.003]

plt.bar(0.2+ind, means, 0.6*width,color=['k','r','c','y','r'], linewidth = 0.1, yerr=stds,error_kw=dict(elinewidth=1.5,ecolor='green'))
plt.axis([0,5,0,1])
plt.ylabel(u'wPrecision')
plt.grid()
plt.xticks([])



ax = SubplotZero(fig, 1, 3, 2)
ax2 = fig.add_subplot(ax)
means = [0.341,0.39,0.42,0.48,0.582] 
stds = [0.0109,0.0149,0.02,0.011,0.009]
plt.bar(0.2+ind, means, 0.6*width, color=['k','r','c','y','r'], linewidth = 0.1, yerr=stds,error_kw=dict(elinewidth=1.5,ecolor='green'))
plt.axis([0,5,0,1])
plt.ylabel(u'wRecall')
plt.grid()
plt.xticks([])

ax = SubplotZero(fig, 1, 3, 3)
ax3 = fig.add_subplot(ax)
means = [0.68,0.6415,0.6,0.58,0.548] 
stds = [0.02,0.0119,0.0099,0.009,0.007]
label = plt.bar(0.2+ind, means, 0.6*width, color=['k','r','c','y','r'],linewidth = 0.1, yerr=stds,error_kw=dict(elinewidth=1.5,ecolor='green'))
plt.axis([0,5,0,1])
plt.ylabel(u'wF1')
plt.grid()
plt.xticks([])

fig.legend((label[0], label[1],label[2], label[3],label[4]), ('SVD-Single', 'SVD-Multiple','JNE','SNE','R2P'), 'upper center' ,ncol=5)
plt.savefig('comparison_baseline.png',dpi=250,bbox_inches='tight')
