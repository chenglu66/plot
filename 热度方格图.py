# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 23:05:29 2017

@author: Lenovo-Y430p
"""
import matplotlib.pyplot as plt
import numpy as np
data = np.array([[ 0.45833279,  0.35737994,  0.54257486,  0.66908835],
                 [ 0.19544843,  0.48287855,  0.97316904,  0.25445816],
                 [ 0.44500619,  0.88060579,  0.74509425,  0.65703952],
                 [ 0.80474809,  0.48011234,  0.05086501,  0.47188907]])
fig, ax = plt.subplots()
heatmap = ax.pcolor(data, cmap=plt.cm.Greys)

# put the major ticks at the middle of each cell
ax.set_xticks(np.arange(data.shape[0])+0.5, minor=False)
ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()

ax.set_xticklabels(['a','b','c','d'], minor=False)
ax.set_yticklabels(['A','B','C','D'], minor=False)

cbar = plt.colorbar(heatmap)
