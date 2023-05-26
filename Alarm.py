#pycaw
import time
import winsound
import datetime
from datetime import date
from comtypes import CLSCTX_ALL
from ctypes import cast,POINTER
from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume

now=datetime.datetime.now()
def up():
    devices=AudioUtilities.GetSpeakers()
    interface=devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL,None)
    volume=cast(interface, POINTER(IAudioEndpointVolume))
    currentVolumeDb=volume.GetMasterVolumeLevel()
    turnup=100.0
    master=currentVolumeDb+turnup
    while(master>0):
        turnup-=10
        master=currentVolumeDb+turnup
    volume.SetMasterVolumeLevel(master,None)

def alarm():
    winsound.Beep(820, 1800)

up()
hours=14
minutes=6
seconds=0
then=datetime.time(hours,minutes,seconds)
alarm_time=datetime.datetime.combine(now.date(),then)
if(now.hour<=then.hour):
    if(now.hour==then.hour)and(now.minute<then.minute):
        time.sleep((alarm_time - now).total_seconds())
    elif(now.hour<then.hour):
        time.sleep((alarm_time - now).total_seconds())
else:
    time.sleep((alarm_time + datetime.timedelta(days=1) - now).total_seconds())
alarm()
alarm()
alarm()
alarm()
alarm()