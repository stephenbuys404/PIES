from tkinter import *

counter = 0
running = False
def counter_label(lbl):
    def count():
        if running:
            global counter
            display='0'
            if(counter>0):
                display=str(counter)
            lbl['text']=display
            lbl.after(500, count)
            counter += 0.5
    count()

def StartTimer(lbl):
    global running
    running=True
    counter_label(lbl)
    start_btn['state']='disabled'
    stop_btn['state']='normal'
    reset_btn['state']='normal'

def StopTimer():
    global running
    running = False
    start_btn['state']='normal'
    stop_btn['state']='disabled'
    reset_btn['state']='normal'

def ResetTimer(lbl):
    global counter
    counter=0
    lbl['text']=''
    if running==False:
        reset_btn['state']='disabled'
        lbl['text']='0'

ws = Tk()
ws.geometry('400x450+1000+300')
ws.title('Stopwatch')
ws.config(bg='#299617')
ws.iconbitmap()
ws.resizable(0,0)

bg = PhotoImage()
img = Label(ws, image=bg, bg='#299617')
img.place(x=75, y=50)

lbl = Label(ws,text='0',fg='black',bg='#299617',font='Verdana 40 bold')
lbl.place(x=160, y=170)

start_btn=Button(ws,text='Start',width=15,command=lambda:StartTimer(lbl))
start_btn.place(x=30, y=390)

label_msg = Label(ws,text='seconds',fg='black',bg='#299617',font='Verdana 10 bold')
label_msg.place(x=170, y=250)

stop_btn = Button(ws,text='Stop',width=15,state='disabled',command=StopTimer)
stop_btn.place(x=150, y=390)

reset_btn = Button(ws,text='Reset',width=15,state='disabled',command=lambda:ResetTimer(lbl))
reset_btn.place(x=270, y=390)

ws.mainloop()
