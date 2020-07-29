from tkinter import *
from tkinter import filedialog, Text
from sys import exit
import eyed3
import os
from pygame import *
root=Tk()
root.title('Music Player')
root.geometry("800x670")
root.configure(bg='deep sky blue')
mixer.init()
root.resizable(0,0)
files=[]
n=0
index=0
label5=Label(root,text='Music Player',font=('bold',40),fg='black',bg='deep sky blue').place(x=250,y=30)
songs_listbox=StringVar()                        
def song_detail():
    global index
    audio=eyed3.load(files[index])
    label2=Label(root,text=audio.tag.title,font=(40),fg='black',bg='deep sky blue').place(x=250,y=250)
    label3=Label(root,text='Album: '+audio.tag.album,font=(30),fg='black',bg='deep sky blue').place(x=250,y=280)
    label4=Label(root,text='Artist: '+audio.tag.artist,font=(30),fg='black',bg='deep sky blue').place(x=250,y=310)


def directory():
    global index
    directory=filedialog.askdirectory()
    os.chdir(directory)
    for file in os.listdir(directory):
        if file.endswith('.mp3'):
            realdir=os.path.realpath(file)
            files.append(realdir)
            play(files[index])
    song()
    print(len(files))
            
    
def play(event):
    if(mixer.music.get_busy()):
        mixer.music.stop()
    mixer.music.load(songs_listbox.get())
    mixer.music.play(0)
    song_detail()

def play(song_name):
    if(mixer.music.get_busy()):
        mixer.music.stop()
    mixer.music.load(song_name)
    mixer.music.play(0)
    song_detail()

    
def next():
    global index
    if (index<len(files)-1):
        index+=1
        play(files[index])
    
def previous():
    global index
    if (index>0):
        index-=1
        play(files[index])        
    
def pause():
    global n;
    n+=1;
    if (n%2==0):
        mixer.music.unpause()
    else:
        mixer.music.pause()
        
def song():
    global songs_listbox
    songs_listbox.set(files[index])
    path=os.getcwd()
    menu=OptionMenu(root,songs_listbox,*files,command=play)
    menu['menu'].config(bg='deep sky blue')
    menu.place(x=250,y=2)
    
def rewind():
   mixer.music.rewind()
   
def stop():
   mixer.music.stop()
   
def set_vol():
    if(mixer.music.get_volume()<1.0):
        mixer.music.set_volume(mixer.music.get_volume()+0.1)

def set_vol2():
    if(mixer.music.get_volume()>0.0):
        mixer.music.set_volume(mixer.music.get_volume()-0.1)
def close_window():
    root.destroy()
    quit()
        
photoplay1=PhotoImage(file=r'/Users/user/Desktop/7049985_preview.png')
photoimage1=photoplay1.subsample(24,24)

open_file=Button(root,text="open file",image=photoimage1,padx=10,pady=5,fg="black",bg="deep sky blue" ,command=directory).place(x=0,y=0)

photoplay=PhotoImage(file=r'/Users/user/Desktop/2873-200.png')
photoimage=photoplay.subsample(3,3)

pause_play=Button(root,text='pause',image=photoimage,padx=10,pady=5,fg="grey",bg="deep sky blue" ,command=pause).place(x=350,y=605)


next= Button(root,text='next',padx=20,pady=20,fg='black',bg="deep sky blue" ,command=next).place(x=600,y=605)

previous= Button(root,text='previous',padx=10,pady=20,fg='black',bg="deep sky blue" ,command=previous).place(x=150,y=605)

rewind=Button(root,text='rewind',padx=10,pady=20,width=10,fg='black',bg='deep sky blue',command=rewind).place(x=700,y=605)

stop=Button(root,text='stop',padx=10,pady=20,width=10,fg='black',bg='deep sky blue',command=stop).place(x=0,y=605)

volume1=Button(root,text='volume+',padx=10,pady=20,width=0,fg='black',bg='deep sky blue',command=set_vol).place(x=720,y=400)

volume2=Button(root,text='volume-',padx=10,pady=20,width=0,fg='black',bg='deep sky blue',command=set_vol2).place(x=720,y=480)

exit=Button(root,text='exit',padx=10,pady=20,width=10,fg='black',bg='deep sky blue',command=close_window).place(x=720,y=2)

root.mainloop()
