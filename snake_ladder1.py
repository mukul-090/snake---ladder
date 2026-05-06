import tkinter as tk
import random

# ---- Board settings ----
SIZE = 10
CELL = 60

# Snakes & Ladders
snakes = {
    27: 5,
    40: 3,
    86: 20
}

ladders = {
    4: 25,
    13: 46,
    33: 49
}

# ---- Game state ----
p1 = 0
p2 = 0
turn = 0  # 0 = P1, 1 = P2

# ---- UI ----
root = tk.Tk()
root.title("Snake & Ladder")

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

info = tk.Label(root, text="Click Roll Dice", font=("Arial", 14))
info.pack()

# ---- Draw board ----
def draw_board():
    canvas.delete("all")

    for i in range(SIZE):
        for j in range(SIZE):
            x1 = j * CELL
            y1 = i * CELL
            x2 = x1 + CELL
            y2 = y1 + CELL

            canvas.create_rectangle(x1, y1, x2, y2)

            num = (SIZE - i - 1) * SIZE + (j + 1)
            if (SIZE - i - 1) % 2 == 1:
                num = (SIZE - i) * SIZE - j

            canvas.create_text(x1+30, y1+30, text=str(num))

# ---- Convert position ----
def get_xy(pos):
    if pos == 0:
        return 30, 570

    pos -= 1
    row = pos // SIZE
    col = pos % SIZE

    if row % 2 == 1:
        col = SIZE - 1 - col

    x = col * CELL + 30
    y = (SIZE - 1 - row) * CELL + 30
    return x, y

# ---- Draw players ----
def draw_players():
    x1, y1 = get_xy(p1)
    x2, y2 = get_xy(p2)

    canvas.create_oval(x1-10, y1-10, x1+10, y1+10, fill="blue")
    canvas.create_oval(x2-10, y2-10, x2+10, y2+10, fill="red")

# ---- Draw snakes & ladders ----
def draw_snakes_ladders():
    for s, e in snakes.items():
        x1, y1 = get_xy(s)
        x2, y2 = get_xy(e)
        canvas.create_line(x1, y1, x2, y2, fill="red", width=3)

    for s, e in ladders.items():
        x1, y1 = get_xy(s)
        x2, y2 = get_xy(e)
        canvas.create_line(x1, y1, x2, y2, fill="green", width=3)

# ---- Game step ----
def roll_dice():
    global p1, p2, turn

    dice = random.randint(1, 6)

    if turn == 0:
        p1 += dice
        if p1 in snakes:
            p1 = snakes[p1]
        if p1 in ladders:
            p1 = ladders[p1]
        info.config(text=f"P1 rolled {dice}")

    else:
        p2 += dice
        if p2 in snakes:
            p2 = snakes[p2]
        if p2 in ladders:
            p2 = ladders[p2]
        info.config(text=f"P2 rolled {dice}")

    draw_board()
    draw_snakes_ladders()
    draw_players()

    # win check
    if p1 >= 100:
        info.config(text="P1 WINS!")
        return
    if p2 >= 100:
        info.config(text="P2 WINS!")
        return

    turn = 1 - turn

# ---- Button ----
btn = tk.Button(root, text="Roll Dice", command=roll_dice)
btn.pack()

# ---- Initial draw ----
draw_board()
draw_snakes_ladders()
draw_players()

root.mainloop() 