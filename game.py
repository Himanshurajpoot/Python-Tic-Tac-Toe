import tkinter as tk
from tkinter import messagebox

def check_winner():
    # Check rows, columns, and diagonals for a winner
    #helo
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            messagebox.showinfo("Tic Tac Toe", f"Player {board[i][0]} wins!")
            reset_game()
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            messagebox.showinfo("Tic Tac Toe", f"Player {board[0][i]} wins!")
            reset_game()
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        messagebox.showinfo("Tic Tac Toe", f"Player {board[0][0]} wins!")
        reset_game()
        return True
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        messagebox.showinfo("Tic Tac Toe", f"Player {board[0][2]} wins!")
        reset_game()
        return True
    return False

def check_draw():
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def on_click(row, col):
    global player

    if board[row][col] == " ":
        if player == "X":
            board[row][col] = "X"
            buttons[row][col].config(text="X", state="disabled", bg="#90EE90")  # Light green color
            player = "O"
        else:
            board[row][col] = "O"
            buttons[row][col].config(text="O", state="disabled", bg="#87CEFA")  # Light sky blue color
            player = "X"

        if check_winner():
            return  # No need to check for draw after a winner is found

        if check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_game()

def reset_game():
    global board, player
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", state="normal", bg="SystemButtonFace")

root = tk.Tk()
root.title("Tic Tac Toe")

# Set a fixed window size
root.geometry("350x400")

board = [[" " for _ in range(3)] for _ in range(3)]
player = "X"

buttons = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", font=('Arial', 20), height=3, width=6,
                                  command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

reset_button = tk.Button(root, text="Reset", font=('Arial', 12), command=reset_game)
reset_button.grid(row=3, columnspan=3, pady=10)

root.mainloop()