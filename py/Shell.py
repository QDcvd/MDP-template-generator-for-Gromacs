# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:05:03 2020

@author: 郝蛤蛤
"""
import tkinter as tk
import os

root = tk.Tk()
root.title('Mdp模板生成器')
root.geometry('300x200')

def Md():
    os.popen('python ./py/Mdmdp.py')
def NPT():
    os.popen('python ./py/NPTmdp.py')
def NVT():
    os.popen('python ./py/NVTmdp.py')
def EM():
    os.popen('python ./py/EMmdp.py')

ButMd = tk.Button(text='Md模板', width=20, height=2, command=Md)
ButMd.pack()
ButNPT = tk.Button(text='NPT模板', width=20, height=2, command=NPT)
ButNPT.pack()
ButNVT = tk.Button(text='NVT模板', width=20, height=2, command=NVT)
ButNVT.pack()
ButEM = tk.Button(text='EM模板', width=20, height=2, command=EM)
ButEM.pack()

root.mainloop()