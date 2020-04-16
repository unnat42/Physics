# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:54:54 2020

@author: Unnat Antani

Scwartzchild Precession 
"""

import time
import numpy as np
import random
import matplotlib.pyplot as plt 


def transf(x,y,f,theta):

    x_new = []
    y_new = []
    theta = np.radians(theta)
    for i in range(len(x)):
        x_new.append((x[i]-f[0])*np.cos(theta) - (y[i]-f[1])*np.sin(theta) + f[0])
        y_new.append((x[i]-f[0])*np.sin(theta) + (y[i]-f[1])*np.cos(theta) + f[1])
  
    return(x_new,y_new)
        


theta = np.linspace(-np.pi,np.pi)



#Ellipse
a = 40
b = 20
phi = 0

x_e = a*np.cos(theta)
y_e = b*np.sin(theta)
fig = plt.figure()
ax = fig.gca()
plt.title("Schwartzchild Precession")


ax.set_xlim(-120,50)
ax.set_ylim(-100,100)



c = np.sqrt(abs(a**2 - b**2))


if b>a:
    f1 = [0,0-c]
    f2 = [0,0+c]
else:
    f1 = [0-c,0]
    f2 = [0+c,0]
    
focus = ax.scatter([f1[0]],[f1[1]],s=100,c='black')
rot = 60
times = int(360/rot)

for i in range(times):
    

    if i >0:
        x_e, y_e = transf(x_e, y_e, f1,rot)

    
    for i in range(len(x_e)):
        
        point_1 = ax.scatter(x_e[i],y_e[i])
        
    
        plt.pause(0.01)
        fig.canvas.draw()







