"""ex_02 - One Shot Battleship."""

__author__ = "730410363"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

Row = int(input("Guess a row: "))
while (Row > 4 or Row < 1):
    Row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

Column = int(input("Guess a column: "))
while (Column > 4 or Column < 1):
    Column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
Player_box: str = ""

if (Row == secret_row and Column == secret_column):
    Player_box = RED_BOX
else:
    Player_box = WHITE_BOX 

Row_counter_variable: int = 1
Column_counter_variable: int = 1
outcome: str = ""

while (Row_counter_variable <= grid_size):
    outcome = ""
    while (Column_counter_variable <= grid_size):
        if (Row_counter_variable == Row and Column_counter_variable == Column):
            outcome += Player_box
        else: 
            outcome += BLUE_BOX
        Column_counter_variable += 1

    print(outcome)
    Row_counter_variable += 1
    Column_counter_variable = 1

if (Row == secret_row and Column == secret_column):
    print("Hit!")
elif (Row != secret_row and Column == secret_column):
    print("Close! Correct column, wrong row.")
elif (Row == secret_row and Column != secret_column):
    print("Close! Correct row, wrong column.")
else:
    print("Miss!")