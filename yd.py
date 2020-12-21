import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox,filedialog

import time

def widgets():
    {tk.Label(root,
              text="Youtube downloader",
              bg="#ff4500",
              fg="white",
              font=("Times new roman", 25),


              ).place(x=200, y=10)}
    tk.Label(root,
                    text="Enter URL of youtube video:- ",
                    font=("Times new roman", 16),
                    bg="#FFBF00",
                    fg="#484848",
                    ).place(x=30, y=60)

    root.linkText = tk.Entry(root,
                             font=("Times new roman", 13),
                             width=43,
                             textvariable=link)
    root.linkText.place(x=280, y=60)

    tk.Label(root,
                    text="Enter path of you computer\n where to be stored :-",
                    font=("Times new roman,", 16),
                    bg = "#FFBF00",
                    fg = "#484848",
                    ).place(x=30,y=120)

    root.pathText = tk.Entry(root,
                             font=("Times new roman", 13),
                             width=35,
                             textvariable=path)
    root.pathText.place(x=280, y=126)

    button1 = tk.Button(root,
                        text=" Browse",
                        fg="red",
                        highlightbackground="yellow",
                        font=(" Gills Sans", 12),
                        height= 1,
                        width=6,
                        command=browse,
                     )
    button1.place(x=540, y=127.5)

    button2 = tk.Button(root,
                        text=" DOWNLOAD",
                        fg="red",
                        highlightbackground="yellow",
                        font=(" Gills Sans", 28),
                        height=2,
                        width=10,
                        command=download,
                        )
    button2.place(x=200, y=200)

def browse():
    d_path = filedialog.askdirectory(initialdir=" ")   # initial dir =" " --> where are you rn
    path.set(d_path)

def download():

    link_g = link.get()
    path_g = path.get()
    try:
        yo = YouTube(link_g)   # youtube() object

    # select the highest reso stream of the video
        ys = yo.streams.get_highest_resolution()
        tk.messagebox.showinfo(title="Congrats !", message= f'{yo.title} will start downloading shortly')

        ys.download(path_g)
        tk.messagebox.showinfo(title="Yipeee!", message= f" Your video{yo.title} has downloaded at \n{path_g}")
    except :
        tk.messagebox.showerror(title="FAILED", message= "Wrong values")
        time.sleep(3)
        root.destroy()

root = tk.Tk()
root.title("Yotube Downloader By Abrar")
root.resizable(False, False)
root.geometry('600x300')
root.config(bg="#ff4500")

link = tk.StringVar()
path = tk.StringVar()
widgets()

root.mainloop()
