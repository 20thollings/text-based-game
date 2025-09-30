player_name = ""
inventory = []
choice = 0
again = True

player_name = str(input("Hey you! You’re finally awake. What is your name adventurer?"))

print("I'm sure you're confused as to what is going on. You were arrested when you were found trying to cross the border, "
"and walked right into an imperial ambush. You banged your head on your way to this prison cell, seems you lost some of your memory.")
while again == True:
    choice = int(input("WOULD YOU LIKE TO: \n 1. Look under the bed \n 2. Lay on your bed and give up \n 3. try to open the door"))

    if choice == 1:
        if "spoon_handle" in inventory:
            print("Nothing else to find here")
            again = True
        else:
            print("You find a broken handle to a spoon. You put it in your inventory.")
            inventory.append("spoon_handle")
            again = True
    elif choice == 2:
        print("You lay on your bed and give up. Game Over.")
        exit()
    elif choice == 3:
        if "spoon_handle" in inventory:
            print("You jam the spoon handle right into the key-hole, and suddenly the door pops open.")
            again = False
        else:
            print("The door is locked. You need to find a way to open it.")
            again = True
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        again = True

print("As the door swings open, you step out into a tight corridoor, dimly lit by the orange light from lanturns that line the wall." \
"The corridoor appears to expand infinitely in both directions with no end in either direction.")

again = True
while again == True:
    choice = int(input("WOULD YOU LIKE TO: \n 1. Turn and go left \n 2. Turn and go right"))
    if choice == 1:
        inventory.append("left_1")
        again = False
    if choice == 2:
        inventory.append("right_1")
        again = False
    else:
        print("Invalid choice. Please choose 1 or 2.")

if "left_1" in inventory:
    print("As you turn left and walk down the corridoor, you see that to your left in just an endless wall of jail cells, all of which empty" \
    "\n...\nAfter seemingly walking for an hour, you find yourself standing in the doorway of a cafeteria, filled with empty tables and chairs." \
    "A warden paces around the cafeteria darting his eyes restlessly around the empty, despite there being no one to watch." \
    "The only way forward appears to be the double doors at the very opposite end of the cafeteria.")
    
