import tkinter as tk

root = tk.Tk(screenName="Digit Recogniser GUI", baseName=None, className='Tk', useTk=1)
root.title("Digit Recognizer")
root.geometry("300x300")

canvas = tk.Canvas(root, height=200, width=200, bg="white")
canvas.pack()

clear_button = tk.Button(root, text="Clear", width=10, height=1)
clear_button.pack()

root.mainloop()