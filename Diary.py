import os
from tkinter import *
from typing import Final
from itertools import groupby
from tkinter import messagebox
from cryptography.fernet import Fernet

NAME:Final[str]='Diary'
class window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.master.title(NAME)
        title=Label(self.master,text='Title').pack()
        self.title_box=Entry(self.master)
        self.title_box.pack()
        scrollbar=Scrollbar(self.master).pack(side=RIGHT,fill=Y)
        Label(self.master,text='Content').pack()
        self.content_box=Text(self.master)
        self.content_box.pack()
        save_button=Button(self.master,text='Save',width=10,command=self.save_file).pack()
    def save_file(self):
        file_name:str=self.title_box.get()+'-diary.txt'
        fbuffer=open(file_name,'w')
        fbuffer.write(self.content_box.get('1.0',END))
        fbuffer.close()
        messagebox.showinfo(NAME,'Your file is saved successfully!!')

class windowA(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.master.title(NAME)
        self.master.geometry('400x300')
        Label(self.master,text='Type in your file number!').pack(side=TOP)
        self.file_names=os.listdir(os.getcwd())
        self.srch_box=Entry(self.master)
        self.srch_box.pack()
        file_list=Listbox(self.master)
        file_list.pack()
        for at in range(len(self.file_names)):
            file_list.insert(END,str(at)+') '+self.file_names[at])
        read_button=Button(self.master,text='Read',width=20,command=self.read_file).pack(side=BOTTOM)
    def read_file(self):
        go=self.srch_box.get()
        ne:int=int(go)
        read_window=Tk()
        self.file_name=self.file_names[ne]
        read_window.title(self.file_name)
        talk=Text(read_window)
        fbuffer=open(self.file_name,'r')
        contents=fbuffer.read()
        fbuffer.close()
        talk.pack()
        talk.insert('end',contents)
        talk.config(state=DISABLED)
        read_window.mainloop()

class windowB(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master.title(NAME)
        self.master.geometry('400x300')
        Label(self.master,text='Type in your file number!').pack()
        self.file_names=os.listdir(os.getcwd())
        self.srch_box=Entry(self.master)
        self.srch_box.pack()
        file_list=Listbox(self.master)
        file_list.pack()
        for index in range(len(self.file_names)):
            file_list.insert(END,str(index)+') '+self.file_names[index])
        edit_button=Button(self.master,text='Edit File',width=20,command=self.edit_file).pack()
    def edit_file(self):
        go=self.srch_box.get()
        ne:int=int(go)
        edit_window=Tk()
        talk=Text(edit_window)
        self.file_name=self.file_names[ne]
        edit_window.title(self.file_name)
        fbuffer=open(self.file_name,'r')
        content=fbuffer.read()
        fbuffer.close()
        talk.pack()
        talk.insert('end',content)
        def save_file():
            fbuffer=open(self.file_name,'w')
            fbuffer.write(talk.get('1.0',END))
            fbuffer.close()
            messagebox.showinfo(NAME,'Saved Successfully')
        save_button=Button(edit_window,text='Save',command=save_file).pack()

class journal(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.master.title(NAME)
        self.pack(fill=BOTH,expand=1)
        write_button=Button(self,text='Write',width=100,height=10,command=self.write)
        write_button.pack()
        read_button=Button(self,text='Read',width=100,height=10,command=self.read)
        read_button.pack()
        edit_button=Button(self,text='Edit',width=100,height=10,command=self.edit)
        edit_button.pack()
    def write(self):
        abc=Tk()
        Book=window(abc)
        Book.mainloop()
    def read(self):
        abc=Tk()
        Book=windowA(abc)
        Book.mainloop()
    def edit(self):
        abc=Tk()
        Book=windowB(abc)
        Book.mainloop()
book=Tk()
book.geometry('500x500')
app_book=journal(book)
app_book.mainloop()
