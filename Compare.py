import glob
from tkinter import filedialog as fd

file1=fd.askopenfilename()
file2=fd.askopenfilename()

def read(file):
    lines=""
    if(glob.glob(file)):
        f = open(file,'r',encoding='utf8')
        lines = f.read()
        f.close()
    return lines

def compare(lines,compares):
    x=0
    complete=False
    detected=""
    A = len(lines)
    B = len(compares)
    while(not complete):
        if(x<A)and(x<B):
            if(lines[x]!=compares[x]):
                detected+=lines[x]
            x+=1
        else:
            complete=True
    return detected

lines = read(file1)
compares = read(file2)
print(compare(lines,compares))