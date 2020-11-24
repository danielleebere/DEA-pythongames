#a game of knots and crosses, where player 2 is the computer

#importing random so I can randomise the computer's placing of it's counter
import random 

def initialise_display():
    display = [[' ',1,2,3,], #To make it clearer for the user the matrix is numbered, with the body of the matrix being intialised to 0s
               [1,"_","_","_"],
               [2,"_","_","_"],
               [3,"_","_","_"]]

    for row in range(len(display)): # allows for the matrix to be outputted in an organised and clear fashion
        for column in range(len(display[row])):
            print(display[row][column], end=" ")
        print()

    return(display) #returns the starting display

#takes the changing game display and outputs it at different points
def game_display(display): 
    #allows for the matrix to be organised clearly and orderly
    for row in range(len(display)): 
        for column in range(len(display[row])):
            print(display[row][column], end=" ")
        print()
    
    return(display) #returns the display at each point

#this function determines whether the game is over
def game_stage(game,winner,display): 

    #searches for three symbols in a line horizontally, vertically or diagonally.
    #horizontal
    for row in range(len(display)): 
        if (display[row][1] != "_" and (display[row][1] == display[row][2] == display[row][3])):
            game = "over"
            if display[row][column] == "X":
                winner = "Player 1"
            elif display[row][column] == "O":
                winner = "Player 2"
            break;

    #vertical
    for column in range(len(display[row])):
        if (display[1][column] != "_" and (display[1][column] == display[2][column] == display[3][column])):
            game = "over"
            if display[row][column] == "X":
                winner = "Player 1"
            elif display[row][column] == "O":
                winnner = "Player 2"
            break;
                
    #diagonal
    if (display[2][2] != "_") and ((display[2][2] == display[1][1] == display[3][3]) or (display[2][2] == display[3][1] == display[1][3])):
        game = "over"
        if display[row][column] == "X":
            winner = "Player 1"
        elif display[row][column] == "O":
            winnner = "Player 2"
    
    #considers draw scenario  
    if not any("_" in position for position in display) and game!="over": 
        game = "draw"
        winner = "Player 1 and Player 2"

    #returns whether the game is over and the winner
    return(game,winner) 

def main():
    #initialises variables
    game = "" 
    winner = ""
    
    #calls the initialise display function
    display = initialise_display() 

    print("\nWhere would you like to place your token?")

    #a while loop to keep the game going until the game is over/there is a winner
    while game != "over": 
        print()
        print("Player 1's Turn...")
        print()
        #prompts the user to input coordinates to place token
        r_coord = int(input("Input Row Coordinate: ")) 
        c_coord = int(input("Input Column Coordinate: "))
        #player 1 cannot occupy a square if it is occupied by a token
        while display[r_coord][c_coord] == "O" or display[r_coord][c_coord] == "X": 
            print("These coordinates are currently occupied, try again... \n") 
            r_coord = int(input("Input Row Coordinate: "))
            c_coord = int(input("Input Column Coordinate: "))

        display[r_coord][c_coord] = "X"  #places the X counter in the coordinates ther inputted.

        print()
        game_display(display) #calls 'game_display' function - prints an updated game display
        game,winner = game_stage(game,winner,display) #calls 'game_stage' function - checks whether the game is over

        #stops the while loop if Player 1 is the winner
        if game == "over":
            print()
            print("GAME OVER... \n")
            print(f"{winner} Wins!")
            break 

        elif game == "draw":
            print()
            print("GAME OVER... DRAW")
            break
      
        print()
        print("Player 2's Turn..")
        print()
        #computer's counter        
        #generates a random index for row
        #generates a random index for column
        rand_r_index = random.randrange(1,len(display)) 
        rand_c_index = random.randrange(1,4) 

        #prevents player 2 from replacing a token
        while display[rand_r_index][rand_c_index] == "O" or display[rand_r_index][rand_c_index] == "X": 
            rand_r_index = random.randrange(1,len(display)) 
            rand_c_index = random.randrange(1,4)

        #places the O counter in the randomly genrated coordinates
        display[rand_r_index][rand_c_index] = "O" 
      
        game_display(display) #prints an updated game display
       
        #checks whether game is over
        game,winner = game_stage(game,winner,display) 

        if game == "over":
            print()
            print("GAME OVER... \n")
            print(f"{winner} Wins!")                   
            #break isn't needed here as this condition is met by the end of the while loop
            
main()
