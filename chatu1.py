# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 21:51:28 2017

@author: Lenovo-Y430p
"""
import matplotlib.pyplot as plt
import numpy as np

# 空心框
boxcell_x = np.concatenate([np.arange(0,4)*1.5+4.2, np.arange(0,2)*1.5+7.2])#拼接数组
boxcell_y = np.concatenate([np.ones(4)*2.6, np.ones(2)*4.1])

#空心圆圈
circell_x = np.array([2.7, 4.2, 5.7, 7.2, 8.7])
circell_y = np.array([2.6, 4.1, 4.1, 5.6, 5.6])

#实心灰色圆
dotcell_x = np.array([2.7, 4.2, 2.7, 4.2, 5.7, 7.2, 8.7])
dotcell_y = np.array([5.6, 5.6, 7.2, 7.2, 7.2, 7.2, 7.2])

#阴影区
shodow_x = np.array([4.2, 4.2, 5.7, 5.8])
shodow_y = np.array([5.6, 7.2, 7.2, 5.5])

#带加号的小型圈
crosscell_x = np.array([2.5, 5.55])
crosscell_y = np.array([4.3, 5.89])

#不带加号的小型圈
sdotcell_x = np.array([5.3, 5.8])
sdotcell_y = np.array([6.3, 5.5])

# plot marks
#空心圆圈，alpha参数是透明度，一共5个
plt.plot(circell_x,circell_y, marker=r'$\bigodot$', markersize=22,
        linewidth=0, alpha=0.6, color='k', label='Gost-Cell')#linewidth表示线宽当为0时表示没有折线。

# 空心框，一共6个
plt.plot(boxcell_x,boxcell_y, marker=r'$\boxdot$', markersize=22,
        linewidth=0, alpha=0.6, color='k', label='Solid-Cell')

#实心灰色圆，一共7个
plt.plot(dotcell_x,dotcell_y, marker=r'$\bullet$', markersize=12, linewidth=0,
        alpha=0.5, color='k', label='Fluid-Cell')

#带加号的小型圈，两个
plt.plot(crosscell_x,crosscell_y, marker=r'$\oplus$', markersize=8,
        linewidth=0, label='Fresh-Cell')

#不带加号的小型圈，两个
plt.plot(sdotcell_x,sdotcell_y, marker=r'$\circ$', markersize=8,
        linewidth=1, alpha=0.8, color='k')

# plot shodow，一处
plt.fill(shodow_x, shodow_y, linewidth=0, alpha=0.2, color='k')

# textcoords属性设置为'offset points'，表示以xytext是以xy为起点的偏移量，偏移量是像素点，呵呵。
plt.annotate('BI', xy=(5.8, 5.5), xytext=(+5, +5), textcoords='offset points')
plt.annotate('IP', xy=(5.3, 6.3), xytext=(+5, +5), textcoords='offset points')

# plot curve
# connectionstyle表示曲线的弯曲程度；arrowstyle表示箭头的风格，这里实际上用的是虚线；xycoords和textcoords指示xy和xytext的位置关系
# 二者的参数是字符串'data'，表示使用被注释对象的坐标系统，也就是通常说的坐标。
plt.annotate(r'$n+1$',
         xy=(9.6, 6.5), xycoords='data',
         xytext=(1.4, 2.4), textcoords='data', fontsize=16,
         arrowprops=dict(arrowstyle="-", connectionstyle="arc3,rad=-.2"))
plt.annotate(r'$n$',
         xy=(9.4, 6.9), xycoords='data',
         xytext=(1.4, 3.5), textcoords='data', fontsize=16,
         arrowprops=dict(arrowstyle="-", connectionstyle="arc3,rad=-.2",
             linestyle='dashed'))
plt.grid(True, color='k', linewidth=2)

# set the figure style
ax = plt.gca()

#规定坐标轴的刻度
ax.set_xticks(np.arange(0,10,1.5)+0.4)
ax.set_yticks(np.arange(0,10,1.5)+0.4)

#设置周边的坐标轴的颜色为空白，如果不设置，图片四周就会有黑色的坐标线。
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['top'].set_color('none')

#调整图框的尺寸（而不是改变坐标轴取值范围），使x、y 轴长度一致
plt.axis('scaled')#没有此项，则图形为长方形

#下面连个参数规定了最终生成的图片的坐标范围
plt.xlim(0.5,10.5)
plt.ylim(-1,9)

#控制各个轴线是否显示刻度标签
#plt.tick_params(labelbottom='off', labelleft='off', left='off', right='off',bottom='off', top='off')

# add the legend
#numberpoints是标签中点的个数设置，用scatterpoints不起作用；ncol表示每行有两个标签；handlelength图例中xiant线条长度；
#handletextpad线条和文字间距；labelspacingtu图例的行距；fancybox图例边框是否花边。
ax.legend(loc='lower center',numpoints=1, handlelength=2.3, handletextpad=1, labelspacing=1,
        ncol=2,mode="None",borderpad=1, fancybox=True)

plt.savefig('myfig.png',dpi=400,bbox_inches='tight')
plt.show()
