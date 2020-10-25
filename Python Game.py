#Description: A game where the user is competing with the computer, by trying to create a square of 1's, the computer attempts to disturb this by randomly placing its counters.
import random #importing random so I can randomise the computer's placing of it's counter

def initialise_display():
    display = [[' ',1,2,3,4,5], #To make it clearer for the user the matrix is numbered, with the body of the matrix being intialised to 0s
               [1,0,0,0,0,0],
               [2,0,0,0,0,0],
               [3,0,0,0,0,0],
               [4,0,0,0,0,0],
               [5,0,0,0,0,0]]

    for row in range(len(display)): # allows for the matrix to be outputted in an organised and clear fashion
        for column in range(len(display[row])):
            print(display[row][column], end=" ")
        print()

    return(display) #returns the starting display

def game_display(display): #takes the changing game display and outputs it at different points
    for row in range(len(display)): # allows for the matrix to be organise clearly and orderly
        for column in range(len(display[row])):
            print(display[row][column], end=" ")
        print()
    
    return(display) #returns the display at each point

def game_stage(game,winner,display): #this fucntion determines whether the game is over
    for row in range(len(display)): #the for loop is used to aid in searching for a square
        for column in range(len(display[row])):           
            if (display[row][column]==1 and display[row+1][column]==1 and display[row][column+1]==1 and display[row+1][column+1] == 1): #checks to below first, then right and finally diagonally
                game = "over"
                winner = "Player 1"
                break 
            
        if game=="over" and winner=="Player 1":
            break #had to use two breaks to escape a nested for loop
        
    if not any(0 in position for position in display) and game!="over": #the computer (Player 2) is the winner if a square is not formed
        game = "over"
        winner = "Player 2"

    return(game,winner) #returns whether the game is over and the winner

def main():
    game = "" #initialises variables
    winner = ""
    
    display = initialise_display() #calls the initialise display function

    print("\nWhere would you like to place your token?")

    while game != "over": #a while loop to keep the game going until the game is over/there is a winner
        print()
        print("Player 1's Turn...")
        print()
        r_coord = int(input("Input Row Coordinate: ")) #prompts the user to input coordinates to place token
        c_coord = int(input("Input Column Coordinate: "))
        while display[r_coord][c_coord] == 2 or display[r_coord][c_coord] == 1: #player 1 cannot occupy a square if it is occupied by a 2 token, or...
            print("These coordinates are currently occupied, try again... \n") #...if it is occupied by it's own token
            r_coord = int(input("Input Row Coordinate: "))
            c_coord = int(input("Input Column Coordinate: "))

        display[r_coord][c_coord] = 1  #places the '1' counter in the coordinates ther inputted.

        print()
        game_display(display) #calls 'game_display' function - prints an updated game display
        game,winner = game_stage(game,winner,display) #calls 'game_stage' function - checks whether the game is over

        if game == "over":
            print()
            print("GAME OVER... \n")
            print(f"{winner} Wins!")
            break #stops the while loop if Player 1 is the winner
      
        print()
        print("Player 2's Turn..")
        print()
#computer's counter        
        rand_r_index = random.randrange(1,len(display)) #generates a random index for row
        rand_c_index = random.randrange(1,6) #generates a random index for column

        while display[rand_r_index][rand_c_index] == 2: #prevents player 2 from replacing it's own token
            rand_r_index = random.randrange(1,len(display)) 
            rand_c_index = random.randrange(1,6)

        display[rand_r_index][rand_c_index] = 2 #places the '2' counter in the randomly genrated coordinates
#to include an additional counter, you'd repeat this chunk of code       
      
        game_display(display) #prints an updated game display

        game,winner = game_stage(game,winner,display) #checks whether game is over

        if game == "over":
            print()
            print("GAME OVER... \n")
            print(f"{winner} Wins!") #break isn't needed here as this condition is met by the end of the while loop                  
        
main()


