import tkinter as tk
import random

WIDTH, HEIGHT = 500, 500
BALL_SPEED = 5
PADDLE_SPEED = 20

root = tk.Tk()
root.title("Pong Game")
root.resizable(False, False)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

ball = None
paddle = None
ball_dx, ball_dy = BALL_SPEED, -BALL_SPEED

def start_game():
    global ball, paddle, ball_dx, ball_dy
    canvas.delete("all")
    ball = canvas.create_oval(240, 240, 260, 260, fill="white")
    paddle = canvas.create_rectangle(220, 480, 280, 490, fill="white")
    ball_dx, ball_dy = BALL_SPEED, -BALL_SPEED
    update_game()

def move_paddle(event):
    if event.keysym == "Left":
        canvas.move(paddle, -PADDLE_SPEED, 0)
    elif event.keysym == "Right":
        canvas.move(paddle, PADDLE_SPEED, 0)

root.bind("<Left>", move_paddle)
root.bind("<Right>", move_paddle)

def update_game():
    global ball_dx, ball_dy
    canvas.move(ball, ball_dx, ball_dy)
    bx1, by1, bx2, by2 = canvas.coords(ball)
    px1, py1, px2, py2 = canvas.coords(paddle)
    
    if bx1 <= 0 or bx2 >= WIDTH:
        ball_dx = -ball_dx
    if by1 <= 0:
        ball_dy = -ball_dy
    if by2 >= HEIGHT:
        canvas.create_text(WIDTH/2, HEIGHT/2, text="Game Over", fill="red", font=("Arial", 24))
        replay_button = tk.Button(root, text="Replay", command=start_game)
        replay_button.pack()
        return
    if py1 <= by2 <= py2 and px1 <= bx1 <= px2:
        ball_dy = -ball_dy
    
    root.after(20, update_game)

start_game()
root.mainloop()
