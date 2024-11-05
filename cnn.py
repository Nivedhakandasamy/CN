import tkinter as tk
from tkinter import messagebox
import winsound 
def printBoard(gameValues):
    for i in range(9):
        buttons[i].config(text=gameValues[i])


def checkWin(gameValues):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    for win in wins:
        if gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == 'X':
            highlight_win(win)
            return 'X'
        if gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == 'O':
            highlight_win(win)
            return 'O'

    if all(isinstance(item, str) for item in gameValues):
        return 'Draw'
    
    return None


def highlight_win(win):
    for index in win:
        buttons[index].config(bg="green")  
def button_click(index):
    global chance
    if gameValues[index] != 'X' and gameValues[index] != 'O':
        if chance == 1:
            gameValues[index] = 'X'
            buttons[index].config(text="X", state="disabled")
            chance = 0
            turn_label.config(text="O's Turn", fg="blue")
        else:
            gameValues[index] = 'O'
            buttons[index].config(text="O", state="disabled")
            chance = 1
            turn_label.config(text="X's Turn", fg="red")
        
        printBoard(gameValues)

        winner = checkWin(gameValues)
        if winner == 'X':
            messagebox.showinfo("Game Over", "X Wins!")
            winsound.Beep(1000, 500) 
            reset_game()
        elif winner == 'O':
            messagebox.showinfo("Game Over", "O Wins!")
            winsound.Beep(1000, 500) 
            reset_game()
        elif winner == 'Draw':
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()

def reset_game():
    global gameValues, chance
    gameValues = [i for i in range(9)]  
    chance = 1  
    turn_label.config(text="X's Turn", fg="red")
    
    for button in buttons:
        button.config(text="", state="normal", bg="white") 
    
    printBoard(gameValues)

root = tk.Tk()
root.title("Tic-Tac-Toe")

root.config(bg="lightblue")  


gameValues = [i for i in range(9)]  
chance = 1  


turn_label = tk.Label(root, text="X's Turn", font=("Arial", 14), fg="red", bg="lightblue")
turn_label.grid(row=0, column=0, columnspan=3, pady=10)


buttons = []
for i in range(9):
    button = tk.Button(root, text=str(i), width=10, height=3, font=("Arial", 20), 
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3 + 1, column=i%3)  
    button.config(bg="white", fg="black", activebackground="lightgray")  
    buttons.append(button)


restart_button = tk.Button(root, text="Restart Game", font=("Arial", 14), bg="yellow", 
                           command=reset_game)
restart_button.grid(row=4, column=0, columnspan=3, pady=20)

printBoard(gameValues)
root.mainloop()
