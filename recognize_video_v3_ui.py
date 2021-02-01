#Author: God Bennett
#Title: Simple user interface on top of the God's modified version of recognize_video_v3.py.


from tkinter import Frame, Tk, BOTH, Label, Menu, filedialog, messagebox, Text
from PIL import Image, ImageTk

import os
import codecs

screenWidth = "1200"
screenHeight = "600"
windowTitle = "God's Artificial Intelligence Masked Face Recognition ATM App"

import cv2
import recognize_video_v3 as AI_DETECTION_APP

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        load = Image.open("app_icon_small.png").convert("RGBA") 
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=(int(screenWidth)/2)-load.width/2, y=((int(screenHeight)/2))-load.height/2)
  
        
        
root = Tk()
app = Window(root)



############
#screen window size, window title
root.wm_title(windowTitle)
root.geometry(screenWidth + "x" + screenHeight)

############
#menu bar
menubar = Menu(root)

# Adding a cascade to the menu bar:
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Files", menu=filemenu)



# Defining function to trigger file browser
def loadSuspectedCriminalVideoFileFromDialog():  
    currdir = os.getcwd()
    image_file = filedialog.askopenfile(mode ='r', parent=root, initialdir=currdir, title='Please select a video sample suspected to contain criminal presence:')

    root.wm_title(windowTitle + " : " + image_file.name)

    AI_DETECTION_APP.do_video_recognition ( image_file.name )
    
# Adding a load image button to the cascade menu "File"
filemenu.add_command(label="Load video sample suspected to contain criminal presence", command=loadSuspectedCriminalVideoFileFromDialog)


############
#root cycle
root.config(menu=menubar)
root.mainloop()
