# @author: James Furaque
# @description: in this file, we will configure the entirety
# of the game's function.
# aside from main methods that we're going to have,
# I always want to make some helper functions so it's 
# easier to read and understand the code.
import tkinter as tk
import sys

if len(sys.argv) < 3:                                                   # Before going straight to our game's codes
    print("Error: We need player's name. Please run main.py first.")  # we'll try to et player names from command-line arguments
    sys.exit(1)                                                         # so we can use it and apply it to the board

firstPlayerName = sys.argv[1]                                           # We can now expect player 1's name &
secondPlayerName = sys.argv[2]                                          # Player 2's name 
firstPlayerSymbol = "X"                                                 # After that, we can determine their symbols here
secondPlayerSymbol = "O"                                                # Player 1 should take X symbol and O for player 2.

currentPlayerName = firstPlayerName                                     # In this part, we're staring to create assignments for our players
currentPlayerSymbol = firstPlayerSymbol                                 # This way, we can track the current player in our board.

color_blue = "#4584b6"                                                  # This part, is just the colors that we want to use
color_yellow = "#ffde57"                                                # In order to visualize our board.
color_gray = "#343434"
color_light_gray = "#646464"

turns = 0                                                               # Setting the turns to 0 to help us out with tracking our turns.
game_over = False                                                       # initiating a variable as well so we can use it to track if game is over.

                                                                        # After setting up things, we can now start the functions of the game.
def set_tile(row, column):                                              # This function handles the tile clicks
    global currentPlayerName, currentPlayerSymbol, game_over            # so we can track the switches between player's turn
    if game_over or game_board[row][column]["text"] != "":
        return
    
    game_board[row][column]["text"] = currentPlayerSymbol
    if currentPlayerName == firstPlayerName:
        currentPlayerName = secondPlayerName
        currentPlayerSymbol = secondPlayerSymbol
    else:
        currentPlayerName = firstPlayerName
        currentPlayerSymbol = firstPlayerSymbol

    label["text"] = currentPlayerName + "'s turn"
    check_winner()

def get_player_name(symbol):                                                         # We will also create this function to help us 
    return firstPlayerName if symbol == firstPlayerSymbol else secondPlayerName      # for the next functions that we're going to create.

def check_winner():                                                     # Next, this function checkes the winnner
    global turns, game_over                                             # Not just in one places, but through horizontal, vertical and diagonal.
    turns += 1
    for row in range(3):                                                                                                    # First to check:
        if (game_board[row][0]["text"] == game_board[row][1]["text"] == game_board[row][2]["text"]                          # Horizontal Winner
            and game_board[row][0]["text"] != ""):
            label.config(text=f"{get_player_name(game_board[row][0]['text'])} is the winner!", foreground=color_yellow)
            game_over = True
            return
        
    for col in range(3):                                                                                                    # Next will be our
        if (game_board[0][col]["text"] == game_board[1][col]["text"] == game_board[2][col]["text"]                          # Vertical Winner
            and game_board[0][col]["text"] != ""):
            label.config(text=f"{get_player_name(game_board[0][col]['text'])} is the winner!", foreground=color_yellow)
            game_over = True
            return
        
    if (game_board[0][0]["text"] == game_board[1][1]["text"] == game_board[2][2]["text"]                                    # Checking digonal winner aswell
        and game_board[0][0]["text"] != ""):                                                                                # this quite tricky because you need 
        label.config(text=f"{get_player_name(game_board[0][0]['text'])} is the winner!", foreground=color_yellow)           # to check from top to bottom
        game_over = True                                                                                                    # and bottom to top
        return
    
    if (game_board[0][2]["text"] == game_board[1][1]["text"] == game_board[2][0]["text"]
        and game_board[0][2]["text"] != ""):
        label.config(text=f"{get_player_name(game_board[0][2]['text'])} is the winner!", foreground=color_yellow)
        game_over = True
        return
    
    if turns == 9:                                                                                                          # and if the board is full
        game_over = True                                                                                                    # we will tie the game
        label.config(text="Tie!", foreground=color_yellow)


def new_game():                                                                                 # Okay, now after we created the function to identify the winner
    global turns, game_over, currentPlayerName, currentPlayerSymbol                             # I think it's better if we have a function
    turns = 0                                                                                   # To restart the game as well.
    game_over = False
    currentPlayerName = firstPlayerName
    currentPlayerSymbol = firstPlayerSymbol

    label.config(text=currentPlayerName + "'s turn", foreground="white")
    for row in range(3):
        for col in range(3):
            game_board[row][col].config(text="", foreground=color_blue, background=color_gray)

window = tk.Tk()                                                                                # This is the window of our game
window.title("TIC TAC TOE")
window.resizable(False, False)
                                                         
game_frame = tk.Frame(window)                                                                   # In this frame, we also want to display 
label = tk.Label(game_frame, text=currentPlayerName + "'s turn", font=("Consolas", 20),         # whos turn is it right ?
                 background=color_gray, foreground="white")                                     # so we can easily track hehehe
label.grid(row=0, column=0, columnspan=3, sticky="we")
game_board = [[tk.Button(game_frame, text="", font=("Consolas", 50, "bold"),
                         background=color_gray, foreground=color_blue, width=4, height=1,
                         command=lambda r=row, c=c: set_tile(r, c)) for c in range(3)]
              for row in range(3)]
for row in range(3):
    for col in range(3):
        game_board[row][col].grid(row=row + 1, column=col)

btn_restart = tk.Button(game_frame, text="Restart", font=("Consolas", 20),
                        background=color_gray, foreground="white", command=new_game)
btn_restart.grid(row=4, column=0, columnspan=3, sticky="we")
game_frame.pack()

window.update()                                                                                 # Since for me, it's annoying to have the frame to be everywhere
window_width = window.winfo_width()                                                             # whenever we run the program, I made this just to be sure to
window_height = window.winfo_height()                                                           # setup the position of the window to always start at the center
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

# FORMAT "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()