from asyncio import streams
from cgi import test
from email.mime import image
from importlib.metadata import packages_distributions
from importlib.resources import path
import string
from tkinter import*
from tkinter import Text, Tk
import tkinter as tk;
from tkinter import filedialog
from PIL import Image,ImageTk;
from pytube import YouTube;
import threading;
import urllib
import urllib.request, io
from io import BytesIO
threadPoint =0;
mp3 = False;
mp4 = False;

def SelectDirectory():
    path = filedialog.askdirectory();
    #instructLabel.config(text=path);
    ok = path.replace("/",">");
    dicInput.insert(0,ok);
    frame.pack();
    test = Button(frame, text="Audio",command=mp3);
    test1 = Button(frame, text="Video",command=mp4);
    test.grid(row=0, column=0,padx=15);
    test1.grid(row=0, column=1,padx=26);
    hold1.grid(row=0, column=2,padx=15);
    hold2.grid(row=0, column=3,padx=15);
    hold3.grid(row=0, column=4,padx=15);
    downloadButt.pack(pady=20);
    errorLabel.pack();
    
    
def thumbnail():
    yt = YouTube(input.get());
    url = yt.thumbnail_url;
    print(url);
    with urllib.request.urlopen(url) as u:
        raw_data = u.read();
    im = Image.open(BytesIO(raw_data));
    image= ImageTk.PhotoImage(im);
    label.config(image=image)
      
    
def percent(tem,total):
    perc = (float(tem)/total*float(100));
    
def progress(stream,chunk,bytes_remaining):
    size = stream.filesize;
    bytesDone = size - bytes_remaining;
    pct = bytesDone/size*100;
    stringPct= str(round(pct,2));
    errorLabel.config(text="Status:"+stringPct+"%");

def focusOut_1():
    dicInput.config(fg='grey');

    
def mp3():
    global mp4;
    global mp3;
    mp4 = False;
    mp3 = True;
    
def mp4():
    global mp3;
    global mp4;
    mp3 = False;
    mp4 = True;
    
def star():
    downloadButt.config(state=DISABLED);
    errorLabel.config(text="Download has started");
    t1 = threading.Thread(target=Download);
    t1.start();
    
def handle_click(event):
    if(event.widget.message == "butt1"):
        clear(1);
        
    if(event.widget.message == "directoryInput"):
        clear(2);
        SelectDirectory();
    
def clear(case) :
    if(case == 1):
        input.delete(0,'end');
        input.config(fg='black');
    if(case == 2):
        dicInput.delete(0,'end');
    
def Download():
    link = input.get();
    #path = instructLabel.cget("text");
    global threadPoint;
    try:
        if(mp4 or (mp4 == False and mp3 == False )):
            downloadVid = YouTube(link,on_progress_callback=progress).streams.get_highest_resolution().download(output_path=path);
        if(mp3):
            try:
                downloadVid = YouTube(link,on_progress_callback=progress).streams.get_audio_only().download(filename= YouTube(link).title+".mp3",output_path=path);
            except:
                downloadVid = YouTube(link,on_progress_callback=progress).streams.get_audio_only().download(output_path=path);
        errorLabel.config(text="Download completed");
    except:
        errorLabel.config(text="Please Enter a Valid Link");
    threadPoint= threadPoint+1;
    downloadButt.config(state=NORMAL);
#Setup
window = tk.Tk();
window.title("Youtube Downloader");
window.geometry("400x650");
window.config(bg='white');
frame = Frame(window);
frame.config(bg='white');
hold1 = Label(frame,text="",bg='white',highlightbackground='white');
hold2 = Label(frame,text="",bg='white',highlightbackground='white')
hold3 = Label(frame,text="",bg='white',highlightbackground='white')

#Asset
imgURL = "logomakr.com/app/1rviyv"
img = Image.open("youtube.png");

#Image editing
resize_img = img.resize((330,245),Image.ANTIALIAS);
Img =  ImageTk.PhotoImage(resize_img);
imgCanvas = Canvas(window,width=300,height=250);

#Initialization

title = Label(window, text="Youtube Downloader", justify="center", font=("Arial",20));
label = Label(window, image= Img,bg='white');
input = Entry(window, width=40,fg='grey');
dicInput = Entry(window,width=40,fg='grey');
dicInput.insert(0,"Select directory");
dicInput.bind("<1>",handle_click);
dicInput.bind("<FocusOut>",focusOut_1);
dicInput.message = "directoryInput"
input.insert(0,"Enter Download Link");
input.bind("<FocusIn>",handle_click);
input.message = "butt1";
#instructLabel = Label(window,text="Please select directory");
#dicButt = Button(window,text="Select",command=SelectDirectory);
inputLabel = Label(window, text="Enter Download Link", font=("Arial",15) );
downloadButt = Button(window, text="Download", command=star);
errorLabel = Label(window, text="");
#Show
label.pack();
#title.pack();
canvas = Canvas(window,width=400,height=50,bg='white',highlightbackground='white');
canvas.pack();
canvas.create_line(122,25,278,25,fill="red",width=1);
dicInput.pack()
input.pack(pady=15);
#instructLabel.pack(pady=10);
#dicButt.pack(pady=15);

#test
window.mainloop();
