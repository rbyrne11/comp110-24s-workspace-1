"""ex_03_functional_battleship"""

__author__ = "730410363"

import random 

def input_guess (determine_grid_size: int, guess_spot: str) -> int:
    """User guess for row and column"""
    assert guess_spot == "row" or guess_spot == "column"

    grid_size: int = determine_grid_size

    Row = int(input("Guess a row: "))
    while Row > determine_grid_size:
        Row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return Row


secret_row: int = 3
secret_column: int = 2
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
Player_box: str = ""


def print_grid(size:int, row_guess: int, column_guess: int, correctness: bool) -> None:
    """Making grid and boxes"""
    x: int = 1
    y: int = 1
    z: str = ""
    while x <= size:
        if x != row_guess:
            print (BLUE_BOX * size)
        if x == row_guess:
            while y <= size: 
                if y!= column_guess:
                    z+=BLUE_BOX
                if y == column_guess:
                    if correctness == True:
                        z+= RED_BOX
                    if correctness == False:
                        z+= WHITE_BOX
                y+=1
            print(z)  
        x+=1
    

def correct_guess(secret_row:int, secret_column:int, row_guess: int, column_guess:int) -> bool:
    """Is the guess the same as the guesses spot."""
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:
        return False
    
def main(grid_size:int, secretrow:int, secretcolumn:int) -> None:
    """This is the main function with 5 correct inputs."""
    turn: int = 1
    maxnum_turns = 5
    while turn <= 5:
        turn +=1
        print (f"===Turn {turn}/5 ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        hit = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, hit)
        if hit: 
            print("Hit!")
            print(f"You won in {turn}/{maxnum_turns} turns!")
            return
        else: 
            print("Miss!")
    print(f"X/{maxnum_turns} - Better luck next time!")

if __name__ == "__main__":
    grid_size: int = random.randint (3,5)
    main(grid_size, random.randint(1, grid_size), random.randint (1, grid_size))


