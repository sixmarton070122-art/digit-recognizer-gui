import tkinter as tk

root = tk.Tk(screenName="Digit Recogniser GUI", baseName=None, className='Tk', useTk=1)
root.title("Digit Recognizer")
root.geometry("300x300")

def paint_on_canvas(event):
    if event:
        x0,y0,x1,y1 = (event.x-1),(event.y-1),(event.x+1),(event.y+1)
        color = "#000000"
        canvas.create_oval(x0,y0,x1,y1, fill=color)

canvas = tk.Canvas(root, height=200, width=200, bg="white")
canvas.pack()
canvas.bind("<B1-Motion>", paint_on_canvas)

clear_button = tk.Button(root, text="Clear", width=10, height=1, command=canvas.delete('all'))
clear_button.pack()

root.mainloop()