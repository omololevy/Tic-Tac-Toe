#!/usr/bin/env python3.6

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