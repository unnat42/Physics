# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:31:48 2020

@author: Unnat Antani

To visualise the concept of Lorentz Lebgth contraction phenomenon
"""


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter
import numpy as np


class MyClass:
    
    
    def __init__(self, frame):
        self.frame = frame
        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        self.slider = tkinter.Scale(master=root,from_=0 , to=500,troughcolor = 'yellow',length = 500, orient='horizontal', command=self.plot_graph)
        self.slider.pack()

    def plot_graph(self,sldr):
        t = (float(sldr)/500)*299792458 #The velocity of light
        l = np.linspace(2,20,50,True) #length of X is 50
        y = np.ones((50,))*5 #Use constant values automatically so dont have to manually calculate the constants for any two points
        gamma = np.sqrt(1-((t**2)/(299792458**2)))
        l_cont = l*gamma
        lbl = "{0:.2f}c".format(t/299792458) + "\n Length = {0:.2f}l ".format(gamma)
        self.ax.cla()
        self.ax.set_xlim(0,30)
        
        clr = "red"
        
        self.ax.plot(l, y,color = "blue")
        self.ax.plot(l_cont+(l[0]-l_cont[0]), y-3,color = clr, label = lbl)
        self.ax.legend(loc='upper left', bbox_to_anchor=(0.2, 1.00), shadow=True, ncol=1)
        
        self.ax.set_ylim(0,15)
        self.canvas.draw()


root = tkinter.Tk()
root.title("Lorentz Contraction")
MyFrame = tkinter.Frame(root)
MyClass(MyFrame)
MyFrame.pack()
root.mainloop()


