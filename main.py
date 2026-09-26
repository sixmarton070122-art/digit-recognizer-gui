import tkinter as tk

root = tk.Tk(screenName="Digit Recogniser GUI", baseName=None, className='Tk', useTk=1)
root.title("Digit Recognizer")
root.geometry("300x300")

def paint_on_canvas(event):
    x0,y0,x1,y1 = (event.x),(event.y),(event.x+1),(event.y+1)
    color = "#000000"
    canvas.create_line(x0,y0,x1,y1, fill=color)

def clear_canvas():
    canvas.delete('all')

canvas = tk.Canvas(root, height=200, width=200, bg="white", highlightthickness=2, highlightbackground="red")
canvas.pack()
canvas.bind("<Button-1>", paint_on_canvas)
canvas.bind("<B1-Motion>", paint_on_canvas)


clear_button = tk.Button(root, text="Clear", width=10, height=1, command=clear_canvas)
clear_button.pack()

root.mainloop()