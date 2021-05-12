# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:05:03 2020

@author: 郝蛤蛤
"""
from mailmerge import MailMerge
import docx
from docx import Document
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import *

#写入gui界面
root = Tk()
root.title('EM-Mdp模板生成器')
root.geometry('400x200')
# root.mainloop()

var = IntVar()

lb3 = Label(root, text='energygrps(这个要看模型修改)')
lb3.pack()
inp3 = Entry(root)
inp3.insert(0, "Protein Non-protein")
inp3.place(relx=0.1, rely=0.2, relwidth=0.45, relheight=0.05)
inp3.pack()

lb4 = Label(root, text='rlist(这个要看模型修改)')
lb4.pack()
inp4 = Entry(root)
inp4.insert(0, "1.5")
inp4.place(relx=0.1, rely=0.2, relwidth=0.45, relheight=0.05)
inp4.pack()

lb5 = Label(root, text='rcoulomb与rvdw(cutoff参数值)')
lb5.pack()
inp5 = Entry(root)
inp5.insert(0, "1.5")
inp5.place(relx=0.1, rely=0.2, relwidth=0.45, relheight=0.05)
inp5.pack()


def function():
    #获得参数
    energygrps_get = str(inp3.get())
    rlist_get = str(inp4.get())
    rcoulomb_get = str(inp5.get())
    rvdw_get = str(inp5.get())
    #作一步计算
    #加载模板
    template = "./model/EMmdp.docx"

    document = MailMerge(template)
    print("Fields included in {}: {}".format(template, document.get_merge_fields()))
    document.merge(
        energygrps=energygrps_get,
        rlist=rlist_get,               #这个要看模型
        rcoulomb=rcoulomb_get,            #这个为cutoff 参数值。rvdw是LJ或buckingham的阈值。默认为1.0 nm
        rvdw=rvdw_get,                #这个为cutoff 参数值。rvdw是LJ或buckingham的阈值。默认为1.0 nm
    )
    document.write('EM-MdpOut.docx')
    path = "EM-MdpOut.docx"
    doc = Document(path)
    print("----------生成模板中-----------")
    #批量写入到mdp中
    with open("EM-MdpOut.mdp", "w") as file:
        for paragraph in doc.paragraphs:
            print(paragraph.text)
            file.write(paragraph.text + "\n")
    #别嘴臭我，我真的只会if和else........
    if energygrps_get == '':
        answer = tkinter.messagebox.askokcancel('警告', 'energygrps_get没有填写')
    if rlist_get == '':
        answer = tkinter.messagebox.askokcancel('警告', 'rlist没有填写')
    if rcoulomb_get == '':
        answer = tkinter.messagebox.askokcancel('警告', 'rcoulomb没有填写')
    if rvdw_get == '':
        answer = tkinter.messagebox.askokcancel('警告', 'rvdw没有填写')
    else:
        answer = tkinter.messagebox.askokcancel('消息', '模板文件生成成功')
#方法-直接调用模板函数，写入参数，生成模板
btn1 = Button(root, text='生成模板', command=function)
btn1.place(relx=0.1, rely=0.2, relwidth=0.45, relheight=0.1)
btn1.pack()

root.mainloop()




