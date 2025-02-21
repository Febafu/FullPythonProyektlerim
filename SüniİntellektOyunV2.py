import tkinter as tk
import random

EN_BOY, EN_HIGHT = 500, 500
TOP_SURET = 4
PADDLE_SURET = 6
FPS = 60

root = tk.Tk()
root.title("Pong Oyun")
root.resizable(False, False)

canva = tk.Canvas(root, width=EN_BOY, height=EN_HIGHT, bg="black")
canva.pack()

top = None
paddle = None
ai_paddle = None
top_dx, top_dy = TOP_SURET, -TOP_SURET
hesab = 0
top_hesab = 0
tekrar_düyməsi = None
frame_time = 1000 / FPS

paddle_x = (EN_BOY - 60) / 2
paddle_velocity = 0
ai_paddle_x = (EN_BOY - 60) / 2
ai_speed = 5

def oyun_basla():
    global top, paddle, ai_paddle, top_dx, top_dy, hesab, top_hesab, tekrar_düyməsi, paddle_x, paddle_velocity, ai_paddle_x
    hesab = 0
    paddle_x = (EN_BOY - 60) / 2
    paddle_velocity = 0
    ai_paddle_x = (EN_BOY - 60) / 2
    
    canva.delete("all")
    top = canva.create_oval(240, 240, 260, 260, fill="white")
    paddle = canva.create_rectangle(paddle_x, EN_HIGHT - 30, paddle_x + 60, EN_HIGHT - 20, fill="white")
    ai_paddle = canva.create_rectangle(ai_paddle_x, 20, ai_paddle_x + 60, 30, fill="red")
    top_dx, top_dy = TOP_SURET, -TOP_SURET
    
    if tekrar_düyməsi is not None:
        tekrar_düyməsi.destroy()
        tekrar_düyməsi = None

    oyun_update()

def paddle_hərəkət_et(event):
    global paddle_velocity
    if event.keysym == "Left":
        paddle_velocity = -PADDLE_SURET
    elif event.keysym == "Right":
        paddle_velocity = PADDLE_SURET

root.bind("<Left>", paddle_hərəkət_et)
root.bind("<Right>", paddle_hərəkət_et)

def oyun_update():
    global top_dx, top_dy, hesab, top_hesab, paddle_x, paddle_velocity, tekrar_düyməsi, ai_paddle_x
    canva.move(top, top_dx, top_dy)
    bx1, by1, bx2, by2 = canva.coords(top)
    px1, py1, px2, py2 = canva.coords(paddle)
    ai_px1, ai_py1, ai_px2, ai_py2 = canva.coords(ai_paddle)
    
    if bx1 <= 0 or bx2 >= EN_BOY:
        top_dx = -top_dx
    
    if by1 <= 0:
        top_dy = -top_dy
    
    if by2 >= EN_HIGHT:
        if hesab > top_hesab:
            top_hesab = hesab
        canva.create_text(EN_BOY/2, EN_HIGHT/2, text="Game Over", fill="red", font=("Arial", 24))
        canva.create_text(EN_BOY/2, EN_HIGHT/2 + 30, text=f"Score: {hesab}", fill="white", font=("Arial", 18))
        canva.create_text(EN_BOY/2, EN_HIGHT/2 + 60, text=f"Top Score: {top_hesab}", fill="white", font=("Arial", 18))
        
        if tekrar_düyməsi is None:
            tekrar_düyməsi = tk.Button(root, text="Yenidən Başla", command=oyun_basla)
            tekrar_düyməsi.pack()
        return
    
    if py1 <= by2 <= py2 and px1 <= bx1 <= px2:
        top_dy = -top_dy
        hesab += 1
        sürət_artir()
    
    if ai_py2 >= by1 >= ai_py1 and ai_px1 <= bx1 <= ai_px2:
        top_dy = -top_dy
        sürət_artir()
    
    paddle_x += paddle_velocity
    if paddle_x < 0:
        paddle_x = 0
    elif paddle_x > EN_BOY - 60:
        paddle_x = EN_BOY - 60
    
    ai_target_x = bx1 - 30
    if ai_target_x < ai_paddle_x:
        ai_paddle_x -= ai_speed
    elif ai_target_x > ai_paddle_x:
        ai_paddle_x += ai_speed
    
    canva.coords(paddle, paddle_x, EN_HIGHT - 30, paddle_x + 60, EN_HIGHT - 20)
    canva.coords(ai_paddle, ai_paddle_x, 20, ai_paddle_x + 60, 30)
    root.after(int(frame_time), oyun_update)

def sürət_artir():
    global top_dx, top_dy
    top_dx += random.choice([-1, 1]) * 0.1
    top_dy += random.choice([-1, 1]) * 0.1
    top_dx = min(max(top_dx, -TOP_SURET - 1), TOP_SURET + 1)
    top_dy = min(max(top_dy, -TOP_SURET - 1), TOP_SURET + 1)

oyun_basla()
root.mainloop()
