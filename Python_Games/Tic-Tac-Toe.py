import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [[None, None, None], [None, None, None], [None, None, None]]
player = "X"

def check_winner():
    for row in buttons:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] and row[0]["text"] != "":
            return True
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] and buttons[0][col]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] and buttons[0][0]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] and buttons[0][2]["text"] != "":
        return True
    return False

def on_click(row, col):
    global player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = player
        if check_winner():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {player} wins!")
            root.quit()
        player = "O" if player == "X" else "X"

for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(root, text="", width=10, height=3, command=lambda r=r, c=c: on_click(r, c))
        buttons[r][c].grid(row=r, column=c)

root.mainloop()
