"""ex_01 - simple_battleship - A cute step towards Battleship."""

__author__ = "730410363"

Boat_location = int(input("Pick a secret boat location between 1 and 4: "))
if Boat_location < 1:
    print(f"Error! {Boat_location} too low!")
    exit()
if Boat_location > 4:
    print(f"Error! {Boat_location} too high!")
    exit()

Player_2_Boat_Location = int(input("Guess a number between 1 and 4: "))
if Player_2_Boat_Location < 1:
    print(f"Error! {Player_2_Boat_Location} too low!")
    exit()
if Player_2_Boat_Location > 4: 
    print(f"Error! {Player_2_Boat_Location} too high!")
    exit()

if Boat_location == Player_2_Boat_Location:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
Player_box: str = ""

if Boat_location == Player_2_Boat_Location:
    outcome = (RED_BOX)
else:
    outcome = (WHITE_BOX)

if Player_2_Boat_Location == 1: 
    Player_box += outcome
else: 
    Player_box += BLUE_BOX

if Player_2_Boat_Location == 2: 
    Player_box += outcome
else: 
    Player_box += BLUE_BOX

if Player_2_Boat_Location == 3: 
    Player_box += outcome
else: 
    Player_box += BLUE_BOX

if Player_2_Boat_Location == 4: 
    Player_box += outcome
else: 
    Player_box += BLUE_BOX

print(Player_box)