# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 22:30:43 2017

@author: Lenovo-Y430p
"""
import numpy as np
from matplotlib.pyplot import *
#pylab
import random
def backcloud(cloudpara,n=1000):
    Ex = cloudpara[0]
    En = cloudpara[1]
    He = cloudpara[2]

    xd = []
    yd = []

    for i in range(n):
        Enn = random.gauss(0,1)*He + En
        x = random.gauss(0,1)*Enn + Ex
        y = np.exp(-(x-Ex)**2/(2*Enn**2))
        xd.append(x)
        yd.append(y)

    return xd,yd

def expcurve(myex=0,mydelta=1,myshift=4):
    x = np.arange(-myshift,myshift,0.01)
    y = np.exp(-0.5*(x-myex)**2/mydelta**2)
    return x,y

x,y = backcloud((0,1,0.1),3000)
plot(x,y,'.k')
x,y = expcurve(0,1.3,4)
plot(x,y,'b')
x,y = expcurve(0,0.7,4)
plot(x,y,'b')
annotate(u'$\mu_2$',xy=(-1.22,0.63),xytext=(-2.7,0.63),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),fontsize=20)
annotate(u'$\mu_1$',xy=(-0.889,0.47),xytext=(-2.7,0.47),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),fontsize=20)

plot([4,4],[0,0.4],'k')
plot([3.2,3.2],[0,0.2],'k')
plot([2.54,2.54],[0,0.3],'k')
plot([0,0],[0,0.2],'k')

text(4-0.5, 0.42, u'$3(E_n+3H_e)$', fontsize=14)
text(2.54-0.5, 0.32, u'$3(E_n-3H_e)$', fontsize=14)
text(3.2-0.1, 0.22, u'$3S$', fontsize=14)
text(0-0.1, 0.22, u'$E_x$', fontsize=14)

xlim(-4,5)
ax = gca()
xlabel('x')
ylabel(u'$\mu$')
savefig('cloudmodelfeature.png',dpi=700,bbox_inches='tight')
