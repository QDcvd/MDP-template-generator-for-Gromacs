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
root.title('NVT-Mdp模板生成器')
root.geometry('400x300')
# root.mainloop()

var = IntVar()

# lb1 = Label(root, text='simulation time(nsteps=simulation time *1000/dt)')
# # lb1.place(relx=0.1, rely=0.1, relwidth=0.45, relheight=0.1)
# lb1.pack()
# inp1 = Entry(root)
# inp1.place(relx=0.1, rely=0.2, relwidth=0.45, relheight=0.05)
# inp1.pack()
#
# lb2 = Label(root, text='dt(dt数，如500000*0.002是1ns)')
# # lb2.place(relx=0.1, rely=0.1, relwidth=0.45, relheight=0.1)
# lb2.pack()
# inp2 = Entry(root)
# inp2.insert(0, "0.002")
# inp2.place(relx=0.1, rely=0.2, relwidth=0.45, relheight=0.05)
# inp2.pack()

lb4 = Label(root, text='constraints(这个要看模型修改)')
lb4.pack()
# inp4 = Entry(root)
# inp4.insert(0, "all-bonds")
# inp4.place(relx=0.1, rely=0.2, relwidth=0.45, relheight=0.05)
# inp4.pack()

var = StringVar()
comb = Combobox(root,textvariable=var,values=['none','h-bonds','all-bonds','h-angles','all-angles'])
comb.place(relx=0.1,rely=0.5,relwidth=0.2)
comb.bind('<<ComboboxSelected>>')
comb.pack()

lb5 = Label(root, text='rcoulomb与rvdw(cutoff参数值)')
lb5.pack()
inp5 = Entry(root)
inp5.insert(0, "1.5")
inp5.place(relx=0.1, rely=0.2, relwidth=0.45, relheight=0.05)
inp5.pack()

# lb6 = Label(root, text='rvdw(rvdw是LJ或buckingham的阈值)')
# lb6.pack()
# inp6 = Entry(root)
# inp6.place(relx=0.1, rely=0.2, relwidth=0.45, relheight=0.05)
# inp6.pack()

lb7 = Label(root, text='tc-grps(这个是温度热浴的分组)')
lb7.pack()
inp7 = Entry(root)
inp7.insert(0, "Protein_0YA Water_and_ions")
inp7.place(relx=0.1, rely=0.2, relwidth=0.45, relheight=0.05)
inp7.pack()

lb8 = Label(root, text='tau-t(增加或减少组别数)')
lb8.pack()
inp8 = Entry(root)
inp8.insert(0, "0.1 0.1")
inp8.place(relx=0.1, rely=0.2, relwidth=0.45, relheight=0.05)
inp8.pack()

lb9 = Label(root, text='ref-t(单位是开氏温度K)')
lb9.pack()
inp9 = Entry(root)
inp9.insert(0, "323.15 323.15")
inp9.place(relx=0.1, rely=0.2, relwidth=0.45, relheight=0.05)
inp9.pack()

lb10 = Label(root, text='gen_temp(temperature for Maxwell distribution)')
lb10.pack()
inp10 = Entry(root)
inp10.insert(0, "300")
inp10.place(relx=0.1, rely=0.2, relwidth=0.45, relheight=0.05)
inp10.pack()
#获得文本中的内容
# nsteps_get = str(inp1.get())
# dt_get = str(inp2.get())
# compressed_get = str(inp3.get())
# constraints_get = str(inp4.get())
# rcoulomb_get = str(inp5.get())
# rvdw_get = str(inp6.get())
# tc_get = str(inp7.get())
# tau_get = str(inp8.get())
# ref_get = str(inp9.get())
# root.mainloop()

def function():
    #获得参数
    # SimulationTime_get = str(inp1.get())
    # dt_get = str(inp2.get())
    # compressed_get = str(inp3.get())
    constraints_get = str(comb.get())
    rcoulomb_get = str(inp5.get())
    rvdw_get = str(inp5.get())
    tc_get = str(inp7.get())
    tau_get = str(inp8.get())
    ref_get = str(inp9.get())
    gen_temp_get = str(inp10.get())
    #作一步计算
    #加载模板
    template = "./model/NVTmdp.docx"

    document = MailMerge(template)
    print("Fields included in {}: {}".format(template, document.get_merge_fields()))
    document.merge(
        constraints=constraints_get,         #这个要看模型
        rcoulomb=rcoulomb_get,            #这个为cutoff 参数值。rvdw是LJ或buckingham的阈值。默认为1.0 nm
        rvdw=rvdw_get,                #这个为cutoff 参数值。rvdw是LJ或buckingham的阈值。默认为1.0 nm
        tc_grps=tc_get,             #这个是温度热浴的分组
        tau_t=tau_get,               #只是增加或减少组别数
        ref_t=ref_get,               #这个是改温度的。单位是开氏温度K。(分组要对应好，tau_t有两个0.1就是两个组，ref_t也要两个组。)
        gen_temp=gen_temp_get       #这个温度要于ref_t对应
    )
    document.write('NVT-MdpOut.docx')
    path = "NVT-MdpOut.docx"
    doc = Document(path)
    print("----------生成模板中-----------")
    #批量写入到mdp中
    with open("NVT-MdpOut.mdp", "w") as file:
        for paragraph in doc.paragraphs:
            print(paragraph.text)
            file.write(paragraph.text + "\n")
    #别嘴臭我，我真的只会if和else........
    # answer = tkinter.messagebox.askokcancel('消息', '模板文件生成成功')
    # if nsteps_get == '':
    #     answer = tkinter.messagebox.askokcancel('警告', 'nsteps没有填写')
    # if dt_get == '':
    #     answer = tkinter.messagebox.askokcancel('警告', 'dt没有填写')
    # if compressed_get == '':
    #     answer = tkinter.messagebox.askokcancel('警告', 'compressed没有填写')
    if constraints_get == '':
        answer = tkinter.messagebox.askokcancel('警告', 'constraints没有填写')
    if rcoulomb_get == '':
        answer = tkinter.messagebox.askokcancel('警告', 'rcoulomb没有填写')
    if rvdw_get == '':
        answer = tkinter.messagebox.askokcancel('警告', 'rvdw没有填写')
    if tc_get == '':
        answer = tkinter.messagebox.askokcancel('警告', 'tc-grps没有填写')
    if tau_get == '':
        answer = tkinter.messagebox.askokcancel('警告', 'tau-t没有填写')
    if ref_get == '':
        answer = tkinter.messagebox.askokcancel('警告', 'ref-t没有填写')
    if gen_temp_get == '':
        answer = tkinter.messagebox.askokcancel('警告', 'gen_temp没有填写')
    else:
        answer = tkinter.messagebox.askokcancel('消息', '模板文件生成成功')
#方法-直接调用模板函数，写入参数，生成模板
btn1 = Button(root, text='生成模板', command=function)
btn1.place(relx=0.1, rely=0.2, relwidth=0.45, relheight=0.1)
btn1.pack()

root.mainloop()




