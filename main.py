import tkinter as tk
from PIL import Image
import numpy as np

root = tk.Tk(screenName="Digit Recogniser GUI", baseName=None, className='Tk', useTk=1)
root.title("Digit Recognizer")

MNIST_SIZE = 28
SCALE = 10
CANVAS_SIZE = MNIST_SIZE*SCALE
grid = np.zeros((MNIST_SIZE, MNIST_SIZE), dtype=np.uint8)

def paint_on_canvas(event):
    x0,y0 = int(event.x//SCALE),int(event.y//SCALE)
    color = "black"
    if (0 <= x0 < MNIST_SIZE) and (0 <= y0 < MNIST_SIZE):
        canvas.create_rectangle((x0*SCALE,y0*SCALE),(x0*SCALE+SCALE,y0*SCALE+SCALE), fill=color, outline=color)
        grid[y0,x0] = 1

def clear_canvas():
    canvas.delete('all')

def get_canvas_as_pil():
    img = Image.fromarray(grid * 255)   # 0 → 0, 1 → 255
    img = img.convert("L")
    img.save("images/test.png")
    return img

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