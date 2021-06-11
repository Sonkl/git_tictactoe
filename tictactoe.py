#defining board

board = []

for n in range(3):
	board.append(["-"] * 3)

def print_board(lst):
	for row in lst:
		print(" ".join(row))
	

#print_board(board)


#name input
import random

random_row = random.randint(0,2)
random_column = random.randint(0,2)


def player(input_one, input_two):
	player_one = input_one
	player_two = input_two

	if player_two == "":
		player_two = "Computer"

	print ("Player one: ", player_one)
	print ("Player two: ", player_two)



#board[1][0] = "X"
#board[1][1] = "X"
#board[1][2] = "X"

#computer player
def computer_player(row, column):
	while board[row][column] != "-":
		row = random.randint(0,2)
		column = random.randint(0,2)
	board[row][column] = "0"
	return board

#computer_player(random_row, random_column)

#print_board(board)

#Draw input
def draw(row, column):
    row_draw = int(row)
    column_draw = int(column)
    board[int(row_draw)][int(column_draw)] = "X"
    return board

def draw2(row, column):
	row_draw = int(row)
	column_draw = int(column)
	board[int(row_draw)][int(column_draw)] = "0"
	return board
    


def winner(player1, player2):
    winner1 = player1 + " wins!"
    if player2 == "":
        winner2 = "Computer wins!"
    else:
        winner2 = player2 + " wins!"

#winner 1
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        return winner1
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        return winner1
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        return winner1
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        return winner1
    elif board [0][2] == "X" and board[1][1] == "X" and board[2][1] == "X":
        return winner1
    elif board [0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        return winner1
    elif board [0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return winner1
    elif board [0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return winner1
    elif board [0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        return winner1   

    if board[0][0] == "0" and board[0][1] == "0" and board[0][2] == "0":
        return winner2
    elif board[1][0] == "0" and board[1][1] == "0" and board[1][2] == "0":
        return winner2
    elif board[2][0] == "0" and board[2][1] == "0" and board[2][2] == "0":
        return winner2
    elif board[0][0] == "0" and board[1][0] == "0" and board[2][0] == "0":
        return winner2
    elif board [0][2] == "0" and board[1][1] == "0" and board[2][1] == "0":
        return winner2
    elif board [0][2] == "0" and board[1][2] == "0" and board[2][2] == "0":
        return winner2
    elif board [0][0] == "0" and board[1][1] == "0" and board[2][2] == "0":
        return winner2
    elif board [0][1] == "0" and board[1][1] == "0" and board[2][1] == "0":
        return winner2




#für später
#if winner() != None:
	
input_one = input("Enter name: ")
input_two = input("Enter name: ")


#draw()

def game():
    
    print_board(board)
    player(input_one, input_two)
    while winner(input_one, input_two) == None:

        if input_two == "":

            print(input_one,"your turn!")
         
            row_draw = input("Row: ")
         
            column_draw = input("Column: ")
         
            draw(row_draw, column_draw)

            print_board(board)

            if winner(input_one, input_two) != None:

                return winner(input_one, input_two)
            
                break
            
            else:
                print("Computer your turn!")
                
                computer_player(random_row, random_column)
            
                print_board(board)

        else:
            print(input_one,"your turn!")
         
            row_draw = input("Row: ")
         
            column_draw = input("Column: ")
         
            draw(row_draw, column_draw)

            print_board(board)

            if winner(input_one, input_two) != None:

                return winner(input_one, input_two)
            
                break
            
            else:
                
                print(input_two, "your turn!")  
             
                row_draw = input("Row: ")
             
                column_draw = input("Column: ")
             
                draw2(row_draw, column_draw)
             
                print_board(board)
        


	

game()
print(winner(input_one, input_two))
