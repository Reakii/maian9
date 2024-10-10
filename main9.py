from tkinter import *
window = Tk()
window.title("Event")
window.geometry("100x100")
def handle_keypressed(Event):   
    print(Event.char)
window.bind("<Key>",handle_keypressed)
def handle_click(Event):
    print("The button was clicked")
button =Button(text="Click me")
button.pack()
button.bind("<Button-1>",handle_click)
window.mainloop()


