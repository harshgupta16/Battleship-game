"""A battleship game where you have to guess the location of a ship in a 5*5 grid of ocean
If you correctly guess the row and column number where the ship if located, you destroy and sink the battleship"""

from random import randint

board = []

for x in range(5): #specify no. of rows and columns
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row) #remove commas between list items

print "Cuban Missile Crises! You are the captain of an American ship and you have to destroy a nearby Russian ship!"
print_board(board)
print "This is the Pacific ocean, guess the correct position of the Russian ship to send a missile to destroy it."
print "You have five missiles. First up is Missile 0"

def random_row(board): #function to randomnly select a row number
    return randint(0, len(board) - 1)

def random_col(board): #function to randomnly select a column number
    return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row
#print ship_col

for turn in range(6): #5 turns per player
    guess_row = int(raw_input("Guess row number in ocean:")) #user input row number
    guess_col = int(raw_input("Guess column number in ocean:")) #user input column number
    
    if guess_row == ship_row and guess_col == ship_col: #condition if right combination guessed
        board[guess_row][guess_col] = "H"
        print "Geronimo! You sunk the Russian ship. The battle is won!"
        break #program finishes
    else:
        if guess_row not in range(0,len(board)-1) or guess_col not in range(0, len(board)-1): #condition if combination is out of ocean range
            print "Oh God, that's not even in the ocean, that ended up in the Cuban landmass."
        elif(board[guess_row][guess_col] == "X"): #condition if user enters a previous value
            print "No point in sending the missile to the same point as before."
        else: #condition if user enters value in range but incorrect
            print "You missed the Russian ship. Come on! Use some freakin' radars!"
            board[guess_row][guess_col] = "X" #to print X wherever missile fired in range
    print "Missile", turn + 1 #increases turn counter by one
if turn == 5: #game over after last turn
    print "Ammunition finished. Head back to base. You're good for nothing"
print_board(board)
