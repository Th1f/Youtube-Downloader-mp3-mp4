from importlib.metadata import packages_distributions
from importlib.resources import path
from tkinter import*
from tkinter import filedialog;
from PIL import Image,ImageTk;
from pytube import YouTube;
mp3 = False;
mp4 = False;

def SelectDirectory():
    path = filedialog.askdirectory();
    instructLabel.config(text=path);
    inputLabel.pack();
    input.pack(pady=15);
    frame.pack();
    test = Button(frame, text="Audio",command=mp3);
    test1 = Button(frame, text="Video",command=mp4);
    test.grid(row=0, column=0,padx=15);
    test1.grid(row=0, column=1,padx=15);
    downloadButt.pack(pady=20);
    
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
    
def Download():
    link = input.get();
    path = instructLabel.cget("text");
    try:
        if(mp4 or (mp4 == False and mp3 == False )):
            downloadVid = YouTube(link).streams.get_highest_resolution().download(output_path=path);
        if(mp3):
            try:
                downloadVid = YouTube(link).streams.get_audio_only().download(filename= YouTube(link).title+".mp3",output_path=path);
            except:
                downloadVid = YouTube(link).streams.get_audio_only().download(output_path=path);
        errorLabel.config(text="Download completed");
        errorLabel.pack();
    except:
        errorLabel.config(text="Please Enter a Valid Link");
        errorLabel.pack();
    
#Setup
window = Tk();
window.title("Youtube Downloader");
window.geometry("400x650");
frame = Frame(window);

#Asset
img = Image.open("youtube.png");

#Image editing
resize_img = img.resize((300,250),Image.ANTIALIAS);
Img =  ImageTk.PhotoImage(resize_img);

#Initialization
title = Label(window, text="Youtube Downloader", justify="center", font=("Arial",20));
label = Label(window, image= Img);
input = Entry(window, width=40);
dicButt = Button(window,text="Select",command=SelectDirectory);
instructLabel = Label(window, text="Please Select Directory");
inputLabel = Label(window, text="Enter Download Link", font=("Arial",15) );
downloadButt = Button(window, text="Download", command=Download);
errorLabel = Label(window, text="Please Enter a valid link");

#Show
title.pack(pady=10);
label.pack();
instructLabel.pack(pady=10);
dicButt.pack(pady=15);
#test
window.mainloop();
