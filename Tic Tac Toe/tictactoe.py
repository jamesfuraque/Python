import tkinter

# MAKE A FUNCTION TO HANDLE THE TILES OF THE GAME
def set_tile(row, column):
    global current_player

    if (game_over):
        return
    
    if game_board[row][column]["text"] != "":
        return
    game_board[row][column]["text"] = current_player
    if current_player == player2:
        current_player = player1
    else:
        current_player = player2
    label["text"] = current_player+"'s turn"

    # CHECKK IF THERE'S WINNER
    check_winner()

# MAKE A FUNCTION TO CHECK FOR A WINNER
def check_winner():
    global turns, game_over
    turns += 1

    # HORIZONTAL WINNER
    for row in range(3):
        if (game_board[row][0]["text"] == game_board[row][1]["text"] == game_board[row][2]["text"]
            and game_board[row][0]["text"] != ""):
            label.config(text=game_board[row][0]["text"]+" is the winner!", foreground=color_yellow)
            for column in range(3):
                game_board[row][column].config(foreground=color_yellow,  background = color_light_gray)
            game_over = True
            return
        
    # VERTICAL WINNER
    for column in range(3):
        if (game_board[0][column]["text"] == game_board[1][column]["text"] == game_board[2][column]["text"]
            and game_board[0][column]["text"] != ""):
            label.config(text=game_board[0][column]["text"]+" is the winner!", foreground=color_yellow)
            for row in range(3):
                game_board[row][column].config(foreground=color_yellow,  background = color_light_gray)
            game_over = True
            return
        
    # DIAGONALLY WINNER
    if (game_board[0][0]["text"] == game_board[1][1]["text"] == game_board[2][2]["text"]
        and game_board[0][0]["text"] != ""):
        label.config(text = game_board[0][0]["text"]+ " is the winner!", foreground=color_yellow)
        for i in range(3):
            game_board[i][i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return
    
    if (game_board[0][2]["text"] == game_board[1][1]["text"] == game_board[2][0]["text"]
        and game_board[0][2]["text"] != ""):
        label.config(text = game_board[0][2]["text"]+ " is the winner!", foreground=color_yellow)
        game_board[0][2].config(foreground=color_yellow, background=color_light_gray)
        game_board[1][1].config(foreground=color_yellow, background=color_light_gray)
        game_board[2][0].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return
    
    # GAME IS TIE
    if turns == 9:
        game_over = True
        label.config(text="Tie!", foreground=color_yellow)


# MAKE A FUNCTION FOR STARTING A GAME
def new_game():
    global turns, game_over
    turns = 0
    game_over = False

    label.config(text=current_player+"'s turn", foreground="white")
    for row in range(3):
        for column in range(3):
            game_board[row][column].config(text="", foreground=color_blue, background=color_gray)

# SETUP THE GAME:
# MAKE VARIABLES FOR 2 PLAYERS
player1 = "X"
player2 = "O"

# MAKE A VARIABLE TO KEEP TRACK OF
# CURRENT PLAYER
current_player = player1

# DESIGN THE GAMING BOARD
game_board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

# MAKE THE COLORS OF THE PLAYERS
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

turns = 0
game_over = False   # GAME OVER IF THERE'S 3 DIAGONAL, VERTICAL OR HORIZONTAL OR 9 TURNS HAD PAST

# CREATE THE WINDOW
window = tkinter.Tk()
window.title("TIC TAC TOE")
window.resizable(False, False)

# CREATE A FRAME THAT WILL
# SAY WHO'S TURN IS IT
game_frame = tkinter.Frame(window)
label = tkinter.Label(game_frame, text = current_player+"'s turn", 
                      font=("Consolas", 20), 
                      background=color_gray,
                      foreground="white"
                      )
# SETUP WHERE THE TURN BUTTON WILL BE LOCATED
label.grid(row = 0, column = 0, columnspan = 3, sticky = "we")
for row in range(3):
    for column in range(3):
        game_board[row][column] = tkinter.Button(game_frame, text = "",
                                                 font = ("Consolas", 50, "bold"),
                                                 background=color_gray,
                                                 foreground=color_blue, width = 4, height = 1,
                                                 command=lambda row=row, column=column: set_tile(row, column))
        game_board[row][column].grid(row = row + 1, column = column)

# MAKE A RESTART BUTTON
# FOR THE GAME
button = tkinter.Button(game_frame, text="Restart",
                        font=("Consolas", 20),
                        background=color_gray,
                        foreground="white",
                        command=new_game)
# SETUP THE POSITION OF THE RESTART BUTTON
button.grid(row = 4, column = 0, columnspan = 3, sticky = "we")

game_frame.pack()

# WHENEVER WE RUN THE PROGRAM, WE WANT THE WINDOW TO ALWAYS OPEN IN THE CENTER
# SETUP THE POSITION OF OUR WINDOW
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

# FORMAT "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()