from tkinter import *

win=Tk()

def DestroyWindow(e):
    win.destroy()
closeImage=PhotoImage(file='images/close-window-16.png')

CloseBtn=Button(win,image=closeImage)
CloseBtn.bind('<Button-1>',DestroyWindow)
CloseBtn.place(x=10,y=10)
