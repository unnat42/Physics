# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:31:05 2020

@author: Unnat Antani

SpaceTime concept intuition 
"""
import time
import numpy as np
import random
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

#Parametic Equation of circle 

theta = np.linspace(-np.pi,np.pi)
centre = [20,20]

#Circle
R = 10 #radius
x = R*np.cos(theta) + centre[0]
y = R*np.sin(theta) + centre[1]

#Ellipse
a = 5
b = 1000
x_e = a*np.cos(theta)
y_e = b*np.sin(theta)

fig = plt.figure()
ax = fig.gca(projection='3d')
plt.title("3D SpaceTime Intuition")
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xlim(-20,20)
ax.set_ylim(-1500,1500)

# ax.scatter([],[],[])
k = True
for i in range(len(x_e)):
    
    # point_1 = ax.scatter(x[i],y[i],0)
    # point_2 = ax.scatter(x[i],y[i],i,c='red')
    if k:
        time.sleep(5)
        k = False
    point_1 = ax.scatter(x_e[i],y_e[i],0)
    point_2 = ax.scatter(x_e[i],y_e[i],i,c='red')
    

    plt.pause(0.05)
    fig.canvas.draw()
    # fig.canvas.flush_events()
    