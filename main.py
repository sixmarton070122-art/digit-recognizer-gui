import tkinter as tk
from PIL import ImageGrab

root = tk.Tk(screenName="Digit Recogniser GUI", baseName=None, className='Tk', useTk=1)
root.title("Digit Recognizer")

def paint_on_canvas(event):
    x0,y0 = int(event.x//SCALE),int(event.y//SCALE)
    color = "#000000"
    if (0 <= x0 < MNIST_size) and (0 <= y0 < MNIST_size):
        canvas.create_rectangle((x0*SCALE,y0*SCALE),(x0*SCALE+SCALE,y0*SCALE+SCALE), fill="black", outline="black")

def clear_canvas():
    canvas.delete('all')

def get_canvas_as_pil():
    canvas.update()

    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    img = ImageGrab.grab().crop((x, y, x1, y1))
    img.resize((28,28))
    img.convert("L")
    img.save("images/test.png")

    

MNIST_size = 28
SCALE = 10
CANVAS_SIZE = MNIST_size*SCALE

canvas = tk.Canvas(root, height=CANVAS_SIZE, width=CANVAS_SIZE, bg="white", highlightthickness=2, highlightbackground="red")
canvas.pack(padx=5,pady=5)
canvas.bind("<Button-1>", paint_on_canvas)
canvas.bind("<B1-Motion>", paint_on_canvas)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

clear_button = tk.Button(button_frame, text="Clear", width=12, command=clear_canvas)
clear_button.pack(side="left", padx=5)

predict_button = tk.Button(button_frame, text="Predict", width=12, command=get_canvas_as_pil)
predict_button.pack(side="left", padx=5)

root.mainloop()