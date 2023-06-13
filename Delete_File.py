import os
from tkinter import filedialog as dialog

file = dialog.askopenfilename()
while(file!=''):
    if(os.path.exists(file)):
        os.remove(file)
    file = dialog.askopenfilename()