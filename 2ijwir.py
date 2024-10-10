from tkinter import *
from tkinter import messagebox
root= Tk()
root.geometry("200x200")
def message():
    messagebox.showwarning("Alert","Stop virus found")
    button = Button(root,text="ScanForVirus",command=message)
button=Button(root,text="ScanForVirus", command=message)
button.place(x=40,y=80)
root.mainloop()
