#numpy
#pyaudio
#matplotlib
import wave
import pathlib
import pyaudio
import numpy as np
import matplotlib.pyplot as plt

def image(name):
    file=wave.open(name,'rb')
    nframes=file.getnframes()
    framerate=file.getframerate()
    time=nframes/framerate
    plt.figure(figsize=(15,5))
    plt.plot(np.linspace(0,time,num=nframes),np.frombuffer(file.readframes(-1),dtype=np.int32))
    plt.title('MyRecording!!')
    plt.ylabel('Wave')
    plt.xlabel('Time(s)')
    plt.xlim(0,time)
    plt.show()
    file.close()

def play(name):
    file=wave.open(name,'rb')
    filewidth=file.getsampwidth()
    nchannels=file.getnchannels()
    nrate=file.getframerate()
    chunk=1024
    play=pyaudio.PyAudio()
    stream=play.open(format=play.get_format_from_width(filewidth),channels=nchannels,rate=nrate,output=True)
    data=file.readframes(chunk)
    while(data!=bytes()):
        stream.write(data)
        data=file.readframes(chunk)
    stream.close()
    play.terminate()
    file.close()

def record(name):
    speed=44100
    chunk=1024
    channels=2
    seconds=5
    frames=[]
    play=pyaudio.PyAudio()
    stream=play.open(format=pyaudio.paInt16,channels=channels,rate=speed,frames_per_buffer=chunk,input=True)
    for i in range(0,int(speed/chunk*seconds)):
        data=stream.read(chunk)
        frames.append(data)
    stream.stop_stream()
    play.close(stream)
    stream.close()
    play.terminate()
    play=pyaudio.PyAudio()
    waves=wave.open(name,'wb')
    waves.setnchannels(channels)
    waves.setsampwidth(play.get_sample_size(pyaudio.paInt16))
    waves.setframerate(speed)
    waves.writeframes(bytes().join(frames))
    waves.close()
    play.terminate()
            

#play('myfile.wav')
#image('myfile.wav')
record('myfile.wav')