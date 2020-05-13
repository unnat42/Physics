# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:26:56 2020

@author: Unnat Antani

Field Visualiser
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
        self.ax.set_xlim(-6,6)
        self.ax.set_ylim(-6,6)
        self.ax.plot([-2,2,0,0], [0,0,2,-2])
        
        self.canvas = FigureCanvasTkAgg(self.fig, self.frame)
        self.canvas.draw()
        
        self.text1 = tkinter.Label(master=root, text="Charge 1: -100 to 100")
        self.text1.pack()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        self.charge1 = tkinter.Scale(master=root,from_=-100 , to=100,troughcolor = 'yellow',length = 500, orient='horizontal', showvalue = 0,command=self.charge1)
        self.charge1.pack()
        
        self.text2 = tkinter.Label(master=root, text="Chare 2: -100 to 100")
        self.text2.pack()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        self.charge2 = tkinter.Scale(master=root,from_=-100 , to=100,troughcolor = 'red',length = 500, orient='horizontal', showvalue = 0,command=self.charge2)
        self.charge2.pack()
        
        self.text3 = tkinter.Label(master=root, text="Charge 3: -100 to 100")
        self.text3.pack()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        self.charge3 = tkinter.Scale(master=root,from_=-100 , to=100,troughcolor = 'blue',length = 500, orient='horizontal', showvalue = 0,command=self.charge3)
        self.charge3.pack()
        
        self.text4 = tkinter.Label(master=root, text="Charge 4: -100 to 100")
        self.text4.pack()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        self.charge4 = tkinter.Scale(master=root,from_=-100 , to=100,troughcolor = 'green',length = 500, orient='horizontal', showvalue = 0,command=self.charge4)
        self.charge4.pack()
        
        self.start = tkinter.Button(master=root,command=self.plot, text = " Start ")
        self.start.pack()
        
    def charge1(self,sldr):
        self.q1 = float(sldr)
        
    def charge2(self,sldr):
        self.q2 = float(sldr)
        
    def charge3(self,sldr):
        self.q3 = float(sldr)
    
    def charge4(self,sldr):
        self.q4 = float(sldr)
        
        
        
    def ef(self,q,r,x,y):
    
        den = np.hypot(x-r[0],y-r[1])**3
        ex = q*(x-r[0])/den
        ey = q*(y-r[1])/den
        
        
        return ex,ey
        
       
    
    def plot(self):
        self.ax.cla()
        self.ax.set_xlim(-6,6)
        self.ax.set_ylim(-6,6)
        self.ax.set_yticks([])
        self.ax.set_xticks([])
       
        
        self.charges = [self.q1,self.q2,self.q3,self.q4]
        self.loc = [[-2,0],[2,0],[0,2],[0,-2]]
        n = 50
        x = np.linspace(-6,6,n)
        y = np.linspace(-6,6,n)
        x, y = np.meshgrid(x,y)
        Ex = np.zeros((n,n))
        Ey = np.zeros((n,n))
        x_p = []
        y_p = []
        for i in range(len(self.charges)):
            
            ex, ey = self.ef(self.charges[i],self.loc[i],x,y)
            Ex += ex
            Ey += ey
            x_p.append(self.loc[i][0])
            y_p.append(self.loc[i][1])
            
        colors = 50*np.log(0.5*np.hypot(Ex,Ey)) 
        self.ax.scatter(x_p,y_p)
        self.ax.streamplot(x,y,Ex,Ey,color = colors, cmap=plt.cm.inferno, linewidth=1,density=3, arrowstyle='->', arrowsize=1)
        self.canvas.draw()
           
            
           
            
            
            
       


root = tkinter.Tk()
root.title("Electic Field Visualiser")
MyFrame = tkinter.Frame(root)
MyClass(MyFrame)
MyFrame.pack()
root.mainloop()

