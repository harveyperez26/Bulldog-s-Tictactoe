import tkinter #tk-interface (graphical user interface library)
def set_tile(row, column):
    global curr_player

    if (game_over):
        return
    
    if board[row][column]["text"] != "":
        #already taken spot
        return
    
    board[row][column]["text"] = curr_player #mark the board
    if curr_player == playerO: #switch player
        curr_player = playerX
    else:
        curr_player = playerO
    label["text"] = curr_player+"'s turn"

    #check winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    #Horizontally check 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_gold)
            for column in range(3):
                board[row][column].config(foreground=color_gold, background=color_red)
            game_over = True
            return
    
    #vertical check 3 rows
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=color_gold)
            for row in range(3):
                board[row][column].config(foreground=color_gold, background=color_red)
            game_over = True
            return
        
    #diagonally check 3 rows:
        if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
            and board[0][0]["text"] != ""):
            label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_gold)
            for i in range(3):
                board[i][i].config(foreground=color_gold, background=color_red)
            game_over = True
            return
    #antidiagonally check 3 rows
        if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
            and board[0][2]["text"] != ""):
            label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_gold)
            board[0][2].config(foreground=color_gold, background=color_red)
            board[1][1].config(foreground=color_gold, background=color_red)
            board[2][0].config(foreground=color_gold, background=color_red)
            game_over = True
            return
        #tie
        if(turns == 9):
            game_over = True
            label.config(text="Tie!", foreground=color_gold, background=color_red)
            
def new_game():
    global turns, game_over
    turns = 0
    game_over = False
    label.config(text=curr_player+"'s turn", foreground=color_gold)
     
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_gold, background=color_navyblue)

#game setup
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#0000FF"
color_gold = "#FFD700"
color_navyblue = "#000435"
color_red = "#FF0000"
color_Lblue = "#ADD8E6"

turns = 0
game_over = False

#window setup
window = tkinter.Tk() #create the game window
window.title("BULLDOG'S TICTACTOE")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player+"'s turn", font=("Consolas", 20), background=color_navyblue,
                      foreground="gold")
label.grid(row=0,column=0, columnspan=3, sticky="we")
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=color_navyblue, foreground=color_gold, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="restart", font=("Consolas", 20), background=color_navyblue,
                         foreground=color_gold, command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")
frame.pack()

#center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#forat "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()

