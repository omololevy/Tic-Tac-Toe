#!/usr/bin/env python3.9

from player import Player

player_obj=Player()
input_list=[" ", " ", " ", " ", " ", " ", " ", " ", " "]

def show_grid():
    """The method to draw the board"""
    print("\n")
    print(f'  {input_list[0]}  |  {input_list[1]}  |  {input_list[2]}  ')
    print("-"*5+"|"+"-"*5+"|"+"-"*5)
    print(f'  {input_list[3]}  |  {input_list[4]}  |  {input_list[5]}  ')
    print("-"*5+"|"+"-"*5+"|"+"-"*5)
    print(f'  {input_list[6]}  |  {input_list[7]}  |  {input_list[8]}  ')

def check_winner():
    if input_list[0]==input_list[1] and input_list[1]==input_list[2]:
        if input_list[0] != " ":
            return True

    elif input_list[3]==input_list[4] and input_list[4]==input_list[5]:
        if input_list[3] != " ":
            return True

    elif input_list[6]==input_list[7] and input_list[7]==input_list[8]:
        if input_list[6] != " ":
            return True

    elif input_list[0]==input_list[3] and input_list[3]==input_list[6]:
        if input_list[0] != " ":
            return True

    elif input_list[1]==input_list[4] and input_list[4]==input_list[7]:
        if input_list[1] != " ":
            return True

    elif input_list[2]==input_list[5] and input_list[5]==input_list[8]:
        if input_list[2] != " ":
            return True

    elif input_list[0]==input_list[4] and input_list[4]==input_list[8]:
        if input_list[0] != " ":
            return True

    elif input_list[2]==input_list[4] and input_list[4]==input_list[6]:
        if input_list[2] != " ":
            return True

    else:
        return False

def main():
  
    which_player=True #Checks which player should play.

    is_stalemate= True #This checks for a draw
    
        
    print("     TIC-TAC_TOE")
    print("This is how the grid looks like")
    print("\n")

    print(" 1   | 2   | 3   ")
    print("-"*5+"|"+"-"*5+"|"+"-"*5)
    print(" 4   | 5   | 6   ")
    print("-"*5+"|"+"-"*5+"|"+"-"*5)
    print(" 7   | 8   | 9   ")   
    print("\n")

    print("     START")
    while len(player_obj.moves_available)>0:
        value_error=False
        
        if which_player==True:
            print("\nPlayer 1:")
            print("Available moves:")
            player_obj.show_av_moves()
            show_grid() #prints the board on the terminal 
            print("Player 1, make a move")
            
            try:
                x=int(input()) #Accepts only input of type integer
            except ValueError:
                value_error=True
                print("Kindly use numbers 1-9!!") #What is to be displayed once the input iss wrong
            
            if value_error==False:
                if player_obj.validate_move(x):
                    input_list[x-1]="X"
                    player_obj.move_made(x)
                    which_player=False
                    
                    if check_winner():
                        show_grid()

                        print("\n-----(( PLAYER ONE WINS ))-----\n               END")                    
                        
                        is_stalemate=False
                        break
                else:
                    print("******Invalid move, try again******")
                    which_player=True   

if __name__ == "__main__":
    main ()