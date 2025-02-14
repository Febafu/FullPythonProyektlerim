import tkinter as tk
import random

def move_target():
    x = random.randint(50, 350)
    y = random.randint(50, 350)
    canvas.coords(target, x, y, x + 30, y + 30)

def check_hit(event):
    x, y, x1, y1 = canvas.coords(target)
    if x <= event.x <= x1 and y <= event.y <= y1:
        score_label.config(text=f"Score: {int(score_label['text'].split(': ')[1]) + 1}")
        move_target()

root = tk.Tk()
root.title("Click the Target Game")
root.geometry("400x400")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

target = canvas.create_oval(100, 100, 130, 130, fill="red")
canvas.bind("<Button-1>", check_hit)

score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack()

move_target()
root.mainloop()
