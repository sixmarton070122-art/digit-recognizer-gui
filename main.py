import tkinter as tk

root = tk.Tk(screenName="Digit Recogniser GUI", baseName=None, className='Tk', useTk=1)
root.title("Digit Recognizer")
root.geometry("300x320")

def paint_on_canvas(event):
    x0,y0 = int(event.x//SCALE),int(event.y//SCALE)
    color = "#000000"
    if (0 <= x0 < 28) and (0 <= y0 < 28):
        canvas.create_rectangle((x0*SCALE,y0*SCALE),(x0*SCALE+SCALE,y0*SCALE+SCALE), fill="#000000")

def clear_canvas():
    canvas.delete('all')

MNIST_size = 28
SCALE = 10
CANVAS_SIZE = MNIST_size*SCALE

canvas = tk.Canvas(root, height=CANVAS_SIZE, width=CANVAS_SIZE, bg="white", highlightthickness=2, highlightbackground="red")
canvas.pack()
canvas.bind("<Button-1>", paint_on_canvas)
canvas.bind("<B1-Motion>", paint_on_canvas)


clear_button = tk.Button(root, text="Clear", width=10, height=1, command=clear_canvas)
clear_button.pack()

root.mainloop()