# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 23:05:53 2020

@author: unnat
"""
import matplotlib.pyplot as plt
import time
import math


 
# xdata = []
# ydata = []
 
# plt.show()
 
# axes = plt.gca()
# axes.set_xlim(-500, 500)
# axes.set_ylim(-500, 500)

# line, = axes.plot(xdata, ydata, 'ro') #Scatter plot and not line plot


#Throwing an object at an anlge 45 degrees and initial velocity as 10 m/s from a height of 200 m
# pos_y = 0+200
# pos_x = 0-50


# for i in range(10):
#     pos_x = pos_x + 10*math.cos(math.pi/4)*i
#     pos_y =pos_y + 10*math.sin(math.pi/4)*i - 0.5*9.81*(i**2)
#     xdata.append(pos_x)
#     ydata.append(pos_y)
#     line.set_xdata(xdata)
#     line.set_ydata(ydata)
#     plt.draw()
#     plt.pause(1)
#     time.sleep(0.1)
 
# # add this if you don't want the window to disappear at the end
# plt.show()


#Free fall simulation

# pos_y = 0+200
# pos_x = 0-50

# i = 0
# while True:
    
#     pos_y =pos_y - 0.5*9.81*(i**2)
#     i = i + 0.1
#     if pos_y <= 0:
#         print(pos_y)
#         break
#     else:
#         xdata.append(pos_x)
#         ydata.append(pos_y)
#         line.set_xdata(xdata)
#         line.set_ydata(ydata)
#         plt.draw()
#         plt.pause(0.01)
#         time.sleep(0.1)
        
    
# plt.show()


#2 Bodies attracting: Gravity


xdata_1 = []
xdata_2 = []

ydata_1 = []
ydata_2 = []

plt.show()
 
axes = plt.gca()
axes.set_xlim(-500, 500)
axes.set_ylim(-500, 500)

line1, = axes.plot(xdata_1, ydata_1, 'ro', markersize = 50) 
line2, = axes.plot(xdata_2, ydata_2, 'bo')

pos_y_1= 0
pos_x_1= 0-200
m1 = 10e15   #mass of left dot

pos_y_2 = 0
pos_x_2 = 200
m2 = 10      #mass of right dot

G = 6.67428e-11

grav_force = G*m1*m2/((pos_x_2 - pos_x_1)**2 + (pos_y_2 - pos_y_1)**2)
a1 = grav_force/m1
a2 = grav_force/m2

i = 0
time.sleep(10)
while True:
    
    pos_x_1 = pos_x_1 + 0.5*a1*(i**2)
    pos_x_2 = pos_x_2 - 0.5*a2*(i**2)
    
    pos_x = [pos_x_1,pos_x_2]
    pos_y = [pos_y_1,pos_y_2]
    i = i + 0.1
    if (pos_x_2-pos_x_1) <= 0:

        break
    else:
        xdata_1.append(pos_x_1)
        ydata_1.append(pos_y_1)
        xdata_2.append(pos_x_2)
        ydata_2.append(pos_y_2)
        line1.set_xdata(xdata_1)
        line1.set_ydata(ydata_1)
        line2.set_xdata(xdata_2)
        line2.set_ydata(ydata_2)
        
        plt.xlabel("t = {}".format(i-0.1))
        plt.draw()
        plt.pause(0.01)
        time.sleep(0.1)
        
    
plt.show()

