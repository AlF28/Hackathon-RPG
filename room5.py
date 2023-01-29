player = input("Enter player name:")

print(f"{player} hesistanly enters room 4.")
print(f"The room is pitch black.")

light_choice = input("Search for light switch: Yes or No")
if light_choice == "Yes":
    print(f"{player} searches the wall for a light switch, but accidentally pushes a button.")
    print(f"Pop! The lights turns on and a table with what looks to be food ascends from the ground.")
    print(f"A letter is propped up on the table with {player}'s name ")
    letter_choice = input("Read the letter: Yes or No")
    if letter_choice == "Yes":
        print(f"Dear {player},")
        print("Welcome to my world.")
        print(f"Since you've made it this far, I thought I'd treat you with my favorite dish.")
        print(f"I'm not sure how food affects humans, but I wouldn't want you to leave without exploring my culture.")
        print("Enjoy and see you soon,")
        print("You'll know me when you see me")
        print("")
        alien_food = input("Eat the alien food: Yes or No")
        if alien_food == "Yes":
            print(f"{player} eats the food and is disappointed by its paper like taste.")
            print(f"\"Bleh!\"")
            print(f"{player} leaves room 4.")
        else:
            print(f"{player} doesn't have time for this shenanigans.")
            print(f"{player} leaves room 4.")

    else:
        print(f"{player} doesn't have time for this shenanigans.")
        print(f"{player} leaves room 4.")
else:
    print(f"{player} stumbles through the darkness, stubbing their toes a few times.")
    print(f"Eventually, {player} finds a door handle.")
    print(f"{player} leaves room 4.")