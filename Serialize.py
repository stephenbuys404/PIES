#pickle
import os
import pickle

filename='file1.dat'

def Write():
    f=open(filename,'wb')
    list=[1,'tA','tB','tC','tD','tE','tF','tG','tH','tI','tJ']
    pickle.dump(list,f)
    f.close()

def Read():
    objects = []
    if(os.path.exists(filename)):
        with(open(filename,'rb'))as openfile:
            while(True):
                try:
                    objects.append(pickle.load(openfile))
                except(EOFError):
                    break
            openfile.close()
            print(objects)

Write()
