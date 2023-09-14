#translate
from tkinter import *
from translate import Translator

Screen = Tk()
InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()
LanguageChoices = {'English','French','German'}

def Translate():
    translator = Translator(from_lang= InputLanguageChoice.get(),to_lang=TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)
            
InputLanguageChoiceMenu = OptionMenu(Screen,InputLanguageChoice,*LanguageChoices)
Label(Screen,text='Choose Language').grid(row=0,column=1)
InputLanguageChoiceMenu.grid(row=1,column=1)
NewLanguageChoiceMenu = OptionMenu(Screen,TranslateLanguageChoice,*LanguageChoices)

Label(Screen,text='Translate').grid(row=0,column=2)
NewLanguageChoiceMenu.grid(row=1,column=2)
Label(Screen,text='Enter Sentence').grid(row=2,column =0)
TextVar = StringVar()
TextBox = Entry(Screen,textvariable=TextVar).grid(row=2,column = 1)
Label(Screen,text='Output').grid(row=2,column =2)
OutputVar = StringVar()
TextBox = Entry(Screen,textvariable=OutputVar).grid(row=2,column = 3)
Button(Screen,text='Translation',command=Translate, relief = GROOVE).grid(row=3,column=1,columnspan = 3)

mainloop()
