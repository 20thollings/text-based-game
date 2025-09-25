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
        print("You find a broken handle to a spoon. You put it in your inventory.")
        inventory.append("spoon_handle")
        again = False
    elif choice == 2:
        print("You lay on your bed and give up. Game Over.")
        exit()
    elif choice == 3:
        print("The door is locked. You need to find a way to open it.")
        again = False
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        again = True