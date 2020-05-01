# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:52:11 2020

@author: Unnat Antani

Projectile motion
"""

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter
import numpy as np
import matplotlib.pyplot as plt


class MyClass:
    

        
    def __init__(self, frame):
        self.frame = frame
        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_yticks([])
        self.ax.set_xticks([])
        self.ax.set_xlim(-5,20)
        self.ax.set_ylim(-5,50)
        self.ax.plot([-50,50],[-0.2,-0.2])
        self.canvas = FigureCanvasTkAgg(self.fig, self.frame)
        self.canvas.draw()
        self.text1 = tkinter.Label(master=root, text="Angle: 0 to pi/2")
        self.text1.pack()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        self.angle = tkinter.Scale(master=root,from_=0 , to=100,troughcolor = 'yellow',length = 500, orient='horizontal', showvalue = 0,command=self.get_angle)
        self.angle.pack()
        self.text2 = tkinter.Label(master=root, text="Velocity: 0 to 15")
        self.text2.pack()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        self.velocity = tkinter.Scale(master=root,from_=0 , to=100,troughcolor = 'red',length = 500, orient='horizontal', showvalue = 0,command=self.get_vel)
        self.velocity.pack()
        self.start = tkinter.Button(master=root,command=self.plot, text = " Start ")
        self.start.pack()
        
    def get_angle(self,sldr):
        self.theta = float(sldr)*np.pi/(2*100)
        
    def get_vel(self,sldr):
        self.vel = float(sldr)*15/(100)
        
        
        

        
       
    
    def plot(self):
        self.ax.cla()
        self.ax.set_xlim(-5,20)
        self.ax.set_ylim(-5,50)
        self.ax.set_yticks([])
        self.ax.set_xticks([])
        self.ax.set_xlabel("Theta = {:.2f}, Vel = {}".format(np.degrees(self.theta),self.vel))
        self.ground = False
        self.ax.plot(0, 0, 'bo')
        self.ax.plot([-50,50],[-0.2,-0.2])
        dt = 0.05
        t = 0
        print("Theta = {}, Vel = {}".format(np.degrees(self.theta),self.vel))
        ground = False
        x = 0
        y = 0
        while True:
            x = self.vel * t * np.cos(self.theta)
            y = self.vel * t * np.sin(self.theta) -  0.5*9.81*(t**2)
            t += dt
            self.ax.set_xlim(-5,x+5)
            self.ax.set_ylim(-5,y+5)
            if y <0:
                break
            self.ax.plot(x, y, 'go')
            self.canvas.draw()
           
            
           
            
            
            
       


root = tkinter.Tk()
root.title("Projectile Motion")
MyFrame = tkinter.Frame(root)
MyClass(MyFrame)
MyFrame.pack()
root.mainloop()
