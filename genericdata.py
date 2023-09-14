#pickle
import os
import pickle

filename='file1.dat'
def Write():
    f=open(filename,'wb')
    list=[1,'Lovejot','Teacher']
    pickle.dump(list,f)
    f.close()

def Read():
    objects = []
    if(os.path.exists(filename)):
        openfile=open(filename,'wb')
        while(True):
            try:
                objects.append(pickle.load(openfile))
            except(EOFError):
                break
        openfile.close()
        print(objects)

#Write()
Read()
