user_name = input("Enter user name")
health = 100
print(f" {user_name} enters room 1 and spots a large wardrobe in the corner.")

wardrobe = input(f"Should {user_name} open the wardrobe?")

if wardrobe == "Yes":
    print(f"{user_name} opens the wardrobe hoping to find their clothes but stumbles upon a chest with a key laying beside it.")
    chest = input(f"Should {user_name} unlock the chest")
    if chest == "Yes":
        print(f"{user_name} picks up the heart shaped key and unlocks the chest.")
        print(f"{user_name} is met with an alien treat called a 'granola bar' wrapped in a shiny package. There is also a red apple and a green apple.")
        foodstats_1 = input(f"Which item will {user_name} eat?")
        if foodstats_1 == "granola bar":
            health += 25
            print(f"{user_name}'s health has increased to {health}.")
            print(f"{user_name} turns to leave room 1 after their delightful snack when a collection of three weapons descends from the ceiling.")
            print("The weapon choices are fists, sword, and a bow and arrow.")
            weapons1 = input("Choose your weapon")
            if weapons1 == "fists":
                print(f"{user_name} chose their old ole fashion fists as their weapon.")
            elif weapons1 == "sword":
                print(f"{user_name} chose the medieval longsword as their weapon.")
            elif weapons1 == "bow and arrow":
                print(f"{user_name} is feeling like Katniss Everdeen and chose the bow and arrow as their weapon.")
            else:
                print("Invalid choice. Choose fists, sword, or bow and arrow.")
        elif foodstats_1 == "green apple":
            health += 25
            print(f"{user_name}'s health has increased to {health}.")
            print(f"{user_name} turns to leave room 1 after their delightful snack when a collection of three weapons descends from the ceiling.")
            print("The weapon choices are fists, sword, and a bow and arrow.")
            weapons1 = input("Choose your weapon")
            if weapons1 == "fists":
                print(f"{user_name} chose their old ole fashion fists as their weapon.")
            elif weapons1 == "sword":
                print(f"{user_name} chose the medieval longsword as their weapon.")
            elif weapons1 == "bow and arrow":
                print(f"{user_name} is feeling like Katniss Everdeen and chose the bow and arrow as their weapon.")
            else:
                print("Invalid choice. Choose fists, sword, or bow and arrow.")
        elif foodstats_1 == "red apple":
            health += 25
            print(f"{user_name}'s health has increased to {health}.")
            print(f"{user_name} turns to leave room 1 after their delightful snack when a collection of three weapons descends from the ceiling.")
            print("The weapon choices are fists, sword, and a bow and arrow.")
            weapons1 = input("Choose your weapon")
            if weapons1 == "fists":
                print(f"{user_name} chose their old ole fashion fists as their weapon.")
            elif weapons1 == "sword":
                print(f"{user_name} chose the medieval longsword as their weapon.")
            elif weapons1 == "bow and arrow":
                print(f"{user_name} is feeling like Katniss Everdeen and chose the bow and arrow as their weapon.")
            else:
                print("Invalid choice. Choose fists, sword, or bow and arrow.")
        else:
            print(f"{user_name} is disappointed to see no hot cheetos, and decides to exit the room.")
    else:
        print(f"{user_name} fears there is something inside of the chest and decides to exit the room.")
else:
    print(f"{user_name} fears there is something inside of the wardrobe and decides to exit the room.")



