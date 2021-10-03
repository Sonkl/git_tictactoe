
#print board
def print_board(lst):

	for row in lst:
		print(" ".join(row))
	

#allowed input for player
allowed_input = ["1", "2", "3"]

#allowed input quit
allowed_input_quit = ["yes", "no"]

#draw input random player
import random

random_row = random.randint(0,2)
random_column = random.randint(0,2)


#input player
def player(input_one, input_two):

	player_one = input_one
	player_two = input_two

	if player_two == "":
		player_two = "Random Player"

	print ("Player one: ", player_one)
	print ("Player two: ", player_two)


#random player
def random_player(row, column,board):

	while board[row][column] != "-":
		row = random.randint(0,2)
		column = random.randint(0,2)

	board[row][column] = "0"

	return board

#draw input
def draw(row, column, board):

    row_draw = int(row) - 1

    column_draw = int(column) - 1

    board[int(row_draw)][int(column_draw)] = "X"

    return board

def draw2(row, column, board):

	row_draw = int(row) - 1

	column_draw = int(column) - 1

	board[int(row_draw)][int(column_draw)] = "0"

	return board
    

#defining winner
def winner(player1, player2, board):

    winner1 = player1 + " wins!"

    if player2 == "":
        winner2 = "Random Player wins!"

    else:
        winner2 = player2 + " wins!"

# winner 1
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        return winner1

    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        return winner1

    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        return winner1

    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        return winner1

    elif board [0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return winner1

    elif board [0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        return winner1

    elif board [0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return winner1

    elif board [0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return winner1

    elif board [0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        return winner1   

# winner 2
    elif board[0][0] == "0" and board[0][1] == "0" and board[0][2] == "0":
        return winner2

    elif board[1][0] == "0" and board[1][1] == "0" and board[1][2] == "0":
        return winner2

    elif board[2][0] == "0" and board[2][1] == "0" and board[2][2] == "0":
        return winner2

    elif board[0][0] == "0" and board[1][0] == "0" and board[2][0] == "0":
        return winner2

    elif board [0][2] == "0" and board[1][1] == "0" and board[2][0] == "0":
        return winner2

    elif board [0][2] == "0" and board[1][2] == "0" and board[2][2] == "0":
        return winner2

    elif board [0][0] == "0" and board[1][1] == "0" and board[2][2] == "0":
        return winner2

    elif board [0][1] == "0" and board[1][1] == "0" and board[2][1] == "0":
        return winner2
    
#draw()
def game():

    #defining board
    board = []

    for n in range(3):
	    board.append(["-"] * 3)
    
    #count draws
    count = 0

    #introduction
    print("""Let's play TicTacToe!
Pick a number between 1 and 3 for a row and a column to set your \"X\" or \"O\" on the board.
The first player who has three in a line wins!""")

    #input players
    input_one = input("Enter name: ")
    input_two = input("If you are playing alone, just press ENTER\nEnter name: ")

    print_board(board)

    player(input_one, input_two)

    while winner(input_one, input_two, board) == None:

        #player one and random player
        if input_two == "":

            print(input_one,"your turn!")        

            row_draw = input("Row: ")
         
            column_draw = input("Column: ")       

            while row_draw not in allowed_input or column_draw not in\
                allowed_input or board[int(row_draw) -1 ][int(column_draw) - 1]\
                     != "-":

                if row_draw not in allowed_input or column_draw not in\
                     allowed_input:

                    print("Please pick a number between 1 and 3!")    

                else:
                    
                    print ("Already taken. Try again!")                         

                row_draw = input("Row: ")
         
                column_draw = input("Column: ")
              
         
            draw(row_draw, column_draw, board)

            print_board(board)

            count += 1

            #defining a draw
            if count == 5 and winner(input_one, input_two, board) == None:

                print("It`s a draw!")

                break

            if winner(input_one, input_two, board) != None:

                print(winner(input_one, input_two, board))

                break
            
            else:
                print("Random Player your turn!")
                
                random_player(random_row, random_column, board)
            
                print_board(board)

                if winner(input_one, input_two, board) != None:

                    print(winner(input_one, input_two, board))

        else:
            print(input_one,"your turn!")
         
            row_draw = input("Row: ")
         
            column_draw = input("Column: ")
         
            #check the allowed input
            while row_draw not in allowed_input or column_draw not in\
                allowed_input or board[int(row_draw)-1][int(column_draw)-1] != "-":

                if row_draw not in allowed_input or column_draw not in\
                    allowed_input:

                    print("Please pick a number between 0 and 2!")    

                else:
                    
                    print ("Already taken. Try again!")                         

                row_draw = input("Row: ")
         
                column_draw = input("Column: ")
         
            draw(row_draw, column_draw, board)

            print_board(board)

            count += 1

            #defining a draw
            if count == 5 and winner(input_one, input_two, board) == None:
                
                print("It`s a draw!")

                break

            if winner(input_one, input_two, board) != None:

                print(winner(input_one, input_two, board))
            
                break
            
            else:
                
                print(input_two, "your turn!")  
             
                row_draw = input("Row: ")
             
                column_draw = input("Column: ")

            while row_draw not in allowed_input or column_draw not in\
                allowed_input or board[int(row_draw)-1][int(column_draw)-1] != "-":

                if row_draw not in allowed_input or column_draw not in\
                    allowed_input:

                    print("Please pick a number between 0 and 2!")    

                else:
                    
                    print ("Already taken. Try again!")                         

                row_draw = input("Row: ")
         
                column_draw = input("Column: ")
         
             
            draw2(row_draw, column_draw, board)
             
            print_board(board)
             
            if winner(input_one, input_two, board) != None:
                print(winner(input_one, input_two, board))


#play again   
def play_again():

    play_again = True

    while play_again == True:

        input_quit = input("Do you want to play again?\nEnter \"yes\" or \"no\"!\n")

        while input_quit not in allowed_input_quit:
            
            input_quit = input("Please enter \"yes\" or \"no\"!\n")

        if input_quit == "yes":

            game()
    
        if input_quit == "no":
            play_again = False
            print("Thanks for playing!")
        
#playing the game
game()
play_again()	