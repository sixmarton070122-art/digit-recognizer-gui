import tkinter as tk
import numpy as np
import torch
import model

#Model data
input_size = 28*28
hidden_size = 64
num_classes = 10
digit_recogniser = model.DigitClassifier(input_size=input_size, hidden_size=hidden_size, num_classes=num_classes)

#Load Model
model_name = "test.pth"
digit_recogniser.load_state_dict(torch.load(f"models/{model_name}"))
digit_recogniser.eval()

#TK Root
root = tk.Tk(screenName="Digit Recogniser GUI", baseName=None, className='Tk', useTk=1)
root.title("Digit Recognizer")

#MNIST and SCALE data
MNIST_SIZE = 28
SCALE = 10
CANVAS_SIZE = MNIST_SIZE*SCALE
grid = np.zeros((MNIST_SIZE, MNIST_SIZE), dtype=np.float32)

#Paint on the canvas
def paint_on_canvas(event):
    #Get mouse coordinates
    x0,y0 = int(event.x//SCALE),int(event.y//SCALE)
    if 0 <= x0 < MNIST_SIZE and 0 <= y0 < MNIST_SIZE:
        #Gets darker overtime
        grid[y0, x0] = min(1.0, grid[y0, x0] + 0.1)
        gray = int(255 * (1 - grid[y0, x0]))
        color = f"#{gray:02x}{gray:02x}{gray:02x}"
        canvas.create_rectangle(
            x0 * SCALE, y0 * SCALE,
            (x0 + 1) * SCALE, (y0 + 1) * SCALE,
            fill=color, outline=color
        )

def clean_on_canvas(event):
    x0,y0 = int(event.x//SCALE),int(event.y//SCALE)
    if (0 <= x0 < MNIST_SIZE) and (0 <= y0 < MNIST_SIZE):
        grid[y0, x0] = max(0, grid[y0, x0] - 0.1)
        gray = int(255 * (1 - grid[y0, x0]))
        color = f"#{gray:02x}{gray:02x}{gray:02x}"
        canvas.create_rectangle((x0*SCALE,y0*SCALE),(x0*SCALE+SCALE,y0*SCALE+SCALE), fill=color, outline=color)

#Clear canvas
def clear_canvas():
    canvas.delete('all')
    grid.fill(0.0)

#Predict the drawn digit
def predict_digit():
    image_tensor = torch.from_numpy(grid).float()
    image_tensor = image_tensor.unsqueeze(0).unsqueeze(0)

    with torch.no_grad():
        predictions = digit_recogniser(image_tensor)
        predicted_digit = predictions.argmax(dim=1)
        print(f"The predicted digit is {int(predicted_digit)}")


canvas = tk.Canvas(root, height=CANVAS_SIZE, width=CANVAS_SIZE, bg="white", highlightthickness=2, highlightbackground="red")
canvas.pack(padx=5,pady=5)
canvas.bind("<Button-1>", paint_on_canvas)
canvas.bind("<B1-Motion>", paint_on_canvas)
canvas.bind("<Button-3>", clean_on_canvas)
canvas.bind("<B3-Motion>", clean_on_canvas)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

clear_button = tk.Button(button_frame, text="Clear", width=12, command=clear_canvas)
clear_button.pack(side="left", padx=5)

predict_button = tk.Button(button_frame, text="Predict", width=12, command=predict_digit)
predict_button.pack(side="left", padx=5)

root.mainloop()