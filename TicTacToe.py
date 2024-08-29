import tkinter

# Initialize players and scores
playerX = "X"
playerO = "O"
curr_player = playerX
scoreX = 0
scoreO = 0

# Initialize game variables
board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

turns = 0
game_over = False

# GUI Colors
color_blue = "#0000FF"
color_gold = "#FFD700"
color_navyblue = "#000435"
color_red = "#FF0000"
color_Lblue = "#ADD8E6"

# Function to set tile and switch turns
def set_tile(row, column):
    global curr_player, turns

    if game_over:
        return
    
    if board[row][column]["text"] != "":
        return
    
    board[row][column]["text"] = curr_player

    check_winner()

    if not game_over:
        curr_player = playerO if curr_player == playerX else playerX
        label.config(text=curr_player + "'s turn")
    turns += 1

def check_winner():
    global game_over, scoreX, scoreO

    # Check rows, columns, and diagonals
    for row in range(3):
        if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] != "":
            highlight_winner([(row, 0), (row, 1), (row, 2)])
            end_game(board[row][0]["text"])
            return
    
    for column in range(3):
        if board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] != "":
            highlight_winner([(0, column), (1, column), (2, column)])
            end_game(board[0][column]["text"])
            return

    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != "":
        highlight_winner([(0, 0), (1, 1), (2, 2)])
        end_game(board[0][0]["text"])
        return

    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != "":
        highlight_winner([(0, 2), (1, 1), (2, 0)])
        end_game(board[0][2]["text"])
        return

    if turns == 8:
        label.config(text="Tie!", foreground=color_gold)
        game_over = True

def highlight_winner(winning_coords):
    for row, column in winning_coords:
        board[row][column].config(background=color_red)

def end_game(winner):
    global game_over, scoreX, scoreO

    label.config(text=winner + " is the winner!", foreground=color_gold)
    if winner == playerX:
        scoreX += 1
    else:
        scoreO += 1
    score_label.config(text=f"Score\nX: {scoreX}\nO: {scoreO}")
    game_over = True

def new_game():
    global turns, game_over, curr_player
    turns = 0
    game_over = False
    curr_player = playerX
    label.config(text=curr_player + "'s turn", foreground=color_gold)

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_gold, background=color_navyblue)

# GUI setup
window = tkinter.Tk()
window.title("BulldogsTTT 🐶 (tictactoe)")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player + "'s turn", font=("Consolas", 20),
                      background=color_navyblue, foreground=color_gold)
label.grid(row=0, column=0, columnspan=3, sticky="we")

score_label = tkinter.Label(frame, text=f"Score\nX: {scoreX}\nO: {scoreO}", font=("Consolas", 14),
                            background=color_navyblue, foreground=color_gold)
score_label.grid(row=1, column=0, columnspan=3, sticky="we")

board = [[None]*3 for _ in range(3)]
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=color_navyblue, foreground=color_gold, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+2, column=column)

button = tkinter.Button(frame, text="New Game", font=("Consolas", 20), background=color_navyblue,
                         foreground=color_gold, command=new_game)
button.grid(row=5, column=0, columnspan=3, sticky="we")

frame.pack()

# Center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
