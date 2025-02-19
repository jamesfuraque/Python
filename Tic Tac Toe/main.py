# @author: James Furaque
# This file will handle the first window of our game.
# Instead of using the casual X and O for player's name, 
# I think it's better if we ask for the real names

import tkinter as tk
import subprocess

def start_game():
    firstPlayerName = entry_player1.get().strip()
    secondPlayerName = entry_player2.get().strip()

    if not firstPlayerName or not secondPlayerName:
        label_message.config(text="Please enter both player names!", fg="red")
        return
    subprocess.run(["python", "tictactoe.py", firstPlayerName, secondPlayerName])   # Run tictactoe.py and pass player names as arguments.
    root.destroy()                                                                  # After that, let's close the current window.

color_gray = "#343434"
color_white = "white"
color_darkgray = "darkgray"

root = tk.Tk()                                                                      # This will be our main window
root.title("TIC TAC TOE")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg=color_gray)

frame = tk.Frame(root, bg=color_gray)
frame.pack(expand=True, fill="both", padx=20, pady=20)
                                                                                    # Maybe, we can add labels and entry fields here as well
tk.Label(frame, text="Player 1's name (X):", bg=color_gray, fg=color_white, font=("Consolas", 12), 
         justify="center").pack(pady=5, fill="x")
entry_player1 = tk.Entry(frame, bg="white", fg="black", font=("Consolas", 12), width=25, justify="center")
entry_player1.pack(pady=5)

tk.Label(frame, text="Player 2's name (O):", bg=color_gray, fg=color_white, font=("Consolas", 12), 
         justify="center").pack(pady=5, fill="x")
entry_player2 = tk.Entry(frame, bg="white", fg="black", font=("Consolas", 12), width=25, justify="center")
entry_player2.pack(pady=5)

label_message = tk.Label(frame, text="", fg="red", bg=color_gray, font=("Consolas", 11))
label_message.pack(pady=5)

btn_start = tk.Button(frame, text="Start Game", bg=color_darkgray, fg="white", font=("Consolas", 12), width=20, height=1, command=start_game)
btn_start.pack(pady=15)

root.update()                                                                       # Oooops what is this??
window_width = root.winfo_width()                                                   # it's just a configuration to always center the frame
window_height = root.winfo_height()                                                 # whenever we start the game.
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

root.mainloop()