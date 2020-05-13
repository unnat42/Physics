# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:14:25 2020

@author: Unnat Antani

Fields Visualization
"""
import matplotlib.pyplot as plt
import numpy as np

def ef(q,r,x,y):

    den = np.hypot(x-r[0],y-r[1])**3
    ex = q*(x-r[0])/den
    ey = q*(y-r[1])/den

    
    return ex,ey

n = 50
x = np.linspace(-6,6,n)
y = np.linspace(-6,6,n)
x, y  = np.meshgrid(x,y)

charges = [10,10,10,10]
loc = [[-2,0],[2,0],[0,2],[0,-2]]
Ex = np.zeros((n,n))
Ey = np.zeros((n,n))
for i in range(len(charges)):
    ex,ey = ef(charges[i],loc[i],x,y)
    
    
    Ex += ex
    Ey += ey


x_p = []
y_p = []
for p in loc:
    x_p.append(p[0])
    y_p.append(p[1])
    
    
fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_xlim(-6,6)
ax.set_ylim(-6,6)
colors = 5*np.log(np.hypot(Ex,Ey))
ax.scatter(x_p,y_p)
ax.streamplot(x,y,Ex,Ey, color = colors, cmap=plt.cm.inferno, linewidth=1,density=2, arrowstyle='->', arrowsize=1)
plt.show()