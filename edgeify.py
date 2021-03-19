# -*- coding: utf-8 -*-
"""
Edge-ify

Created on Thu Mar 18 21:35:14 2021

@author: sofia
"""
from PIL import Image, ImageEnhance
import numpy as np
import tkinter  as tk
from tkinter import filedialog
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


#Defaults in case the user fucks up because ofc they will
DIRECTORY = "C:\\BINGO\\"
PDFPATH = "C:\\BINGO\\Test.pdf"
FILENAME = "Test.pdf"

#Actual Functional Stuff
def PdfToImages(Pdf):
    Images = convert_from_path(Pdf)
    return Images

def SaveImages(Directory, Filename, Images):
    ProcImages=[]
    for im in Images:
        enhancer = ImageEnhance.Brightness(im)
        im = enhancer.enhance(0.8)
        img_data = np.array(im)
        img_reversed_data = 255 - img_data
        img_reversed = Image.fromarray(img_reversed_data)
        ProcImages.append(img_reversed)
    ProcImages[0].save(Directory+Filename+".pdf" ,save_all=True, append_images=ProcImages[1:])
    
#Optimising for user a.k.a GUI because I can't be arsed with console
def BrowseFiles():
    global PDFPATH
    Filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("PDFs","*.pdf*"),("all files","*.*")))
    FilenameLabel.configure(text="File Opened: "+Filename)
    PDFPATH = Filename

def GetFolderPath():
    global DIRECTORY
    FolderSelected = filedialog.askdirectory()
    FilenameLabelResult.configure(text="Folder Selected: "+FolderSelected)
    Dir = FolderSelected+'\\'
    Dir.replace('\\', '/')
    DIRECTORY = Dir
    
def Done():
    global PDFPATH, DIRECTORY, FILENAME
    FILENAME = NewFilename.get()
    SaveImages(DIRECTORY,FILENAME,PdfToImages(PDFPATH))
    
def OKButtonFunc():
    global PDFPATH
    FilenameLabel.configure(text="File Opened: "+TextExplore.get())
    Path = TextExplore.get()
    Path.replace('\\', '/')
    PDFPATH = Path
    
def OKButtonFuncResult():
    global DIRECTORY
    FilenameLabelResult.configure(text="Folder Selected: "+TextExploreResult.get())
    Dir = TextExploreResult.get()+'\\'
    Dir.replace('\\', '/')
    DIRECTORY = Dir
    
    
#Widgeeeeets
Window = tk.Tk()
Window.title('Edge-ify')
Window.geometry("500x260")
PickFileFrame = tk.Frame()
  
Title = tk.Label(Window,text="EDGE-IFY BY SOFYA FEDKINA")
Title.config(font=("Courier", 20))

ButtonExplore = tk.Button(PickFileFrame, text = "Browse Files...",command = BrowseFiles)
TextExplore = tk.Entry(PickFileFrame)
OKButton = tk.Button(PickFileFrame,text= "OK",command=OKButtonFunc)
FilenameLabel = tk.Label(PickFileFrame, text="")

ButtonExploreResult = tk.Button(PickFileFrame, text = "Browse...",command = GetFolderPath) 
TextExploreResult = tk.Entry(PickFileFrame)
OKButtonResult = tk.Button(PickFileFrame,text= "OK",command=OKButtonFuncResult)
FilenameLabelResult = tk.Label(PickFileFrame, text="")
NewFilename = tk.Entry(PickFileFrame)
NewFilenameLabel = tk.Label(PickFileFrame, text="Enter a new filename: ")

ButtonEnter = tk.Button(PickFileFrame, text = "Done!",command = Done)


#Placement
Title.pack(padx=10,pady=20)
ButtonExplore.grid(row = 2, column = 1)
TextExplore.grid(row=2, column = 3)
OKButton.grid(row=2,column=4)
FilenameLabel.grid(row=3,column = 1)

ButtonExploreResult.grid(row=4,column=1)
TextExploreResult.grid(row=4, column = 3)
OKButtonResult.grid(row=4,column=4)
FilenameLabelResult.grid(row=5,column = 1)
NewFilenameLabel.grid(row=6,column = 1)
NewFilename.grid(row=6, column = 2)

ButtonEnter.grid(row=7,column=2,padx=10,pady=10)
PickFileFrame.pack(padx=10,pady=10)

Window.mainloop()



    
        