import tkinter as tk

# Load data
with open("E:/vscode files/Verilog/Snake_&_ladder/output.txt") as f:
    lines = f.readlines()

data = [list(map(int, line.split())) for line in lines]

root = tk.Tk()
root.title("Snake & Ladder (Verilog Driven)")

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

size = 60
cells = {}

# Draw board
for i in range(10):
    for j in range(10):
        num = i * 10 + j + 1
        col = j if i % 2 == 0 else 9 - j

        x1 = col * size
        y1 = 540 - i * size
        x2 = x1 + size
        y2 = y1 + size

        canvas.create_rectangle(x1, y1, x2, y2, fill="#cceeff")
        canvas.create_text(x1 + 30, y1 + 30, text=str(num))

        cells[num] = (x1 + 10, y1 + 10)

# 🐍 Snakes (MATCH VERILOG)
snakes = {
    27: 5,
    40: 3,
    86: 20
}

for start, end in snakes.items():
    x1, y1 = cells[start]
    x2, y2 = cells[end]
    canvas.create_line(x1+10, y1+10, x2+10, y2+10, fill="red", width=3)

# 🪜 Ladders (MATCH VERILOG)
ladders = {
    4: 25,
    13: 46,
    35: 70,
    69: 80
}



for start, end in ladders.items():
    x1, y1 = cells[start]
    x2, y2 = cells[end]
    canvas.create_line(x1+10, y1+10, x2+10, y2+10, fill="green", width=3)

# Players
p1 = canvas.create_oval(5, 555, 20, 570, fill="red")
p2 = canvas.create_oval(25, 555, 40, 570, fill="blue")

# Info labels
info = tk.Label(root, text="Click Roll Dice", font=("Arial", 12))
info.pack()

legend = tk.Label(root, text="P1 = 🔴 Red    |    P2 = 🔵 Blue", font=("Arial", 10))
legend.pack()

index = 0

def roll_dice():
    global index

    if index >= len(data):
        return

    t, turn, dice, p1_pos, p2_pos, win = data[index]

    # Move players
    if p1_pos > 0:
        x, y = cells[min(p1_pos, 100)]
        canvas.coords(p1, x, y, x+15, y+15)

    if p2_pos > 0:
        x, y = cells[min(p2_pos, 100)]
        canvas.coords(p2, x, y, x+15, y+15)

    # Identify player
    player = "P1 (Red 🔴)" if turn == 0 else "P2 (Blue 🔵)"

    # Show info
    info.config(text=f"{player} rolled 🎲 {dice}")

    index += 1

    # WIN CONDITION
    if win == 1:
        if p1_pos >= 100:
            winner = "P1 (Red 🔴)"
        elif p2_pos >= 100:
            winner = "P2 (Blue 🔵)"

    info.config(text=f"🏆 {winner} WINS!")
    button.config(state="disabled")

# Button
button = tk.Button(root, text="ROLL DICE 🎲", command=roll_dice, font=("Arial", 12))
button.pack(pady=10)

root.mainloop()