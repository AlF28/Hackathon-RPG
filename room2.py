user_name = input("Enter user name")
health = 100
print(f" {user_name} has entered room 2.")
print(f"{user_name} sees what appears to be a locked picnic basket sitting on the floor.")

basket_choice = input("Choose to find the key or smash the basket")
if basket_choice == "find the key":
    print(f"{user_name} looks around the empty room puzzled.")
    print(f"{user_name} spots an odd floor vent in the bottom right corner of the room and a bouncy floorboard.")
    find_choice1 = input("Look in the floor vent or the floorboard")
    if find_choice1 == "floor vent":
        print(f"{user_name} peers into the floor vent only to inhale a bunch of dust.")
        print(f"{user_name} decides to look under the misplaced floorboard instead.")
        print(f"{user_name} lifts the floorboard and sees a silver key sitting in the middle.")
        print(f"{user_name} puts the key in their inventory.")
        print(
            f"{user_name} unlocks the basket and sees three food items: a granola bar, a  red apple, and a pizza slice.")
        foodstats_1 = input(f"Which item will {user_name} eat?")
        if foodstats_1 == "granola bar":
            health += 25
            print(f"{user_name}'s health has increased to {health}.")
        elif foodstats_1 == "pizza slice":
            health += 25
            print(f"{user_name}'s health has increased to {health}.")
        elif foodstats_1 == "red apple":
            health += 25
            print(f"{user_name}'s health has increased to {health}.")
        else:
            print("Invalid choice. Type granola bar, red apple, or pizza slice.")
    if find_choice1 == "floorboard":
        print(f"{user_name} lifts the floorboard and sees a silver key sitting in the middle.")
        print(f"{user_name} puts the key in their inventory.")
        print(f"{user_name} unlocks the basket and sees three food items: a granola bar, a  red apple, and a pizza slice.")
        foodstats_1 = input(f"Which item will {user_name} eat?")
        if foodstats_1 == "granola bar":
            health += 25
            print(f"{user_name}'s health has increased to {health}.")
        elif foodstats_1 == "pizza slice":
            health += 25
            print(f"{user_name}'s health has increased to {health}.")
        elif foodstats_1 == "red apple":
            health += 25
            print(f"{user_name}'s health has increased to {health}.")
        else:
            print("Invalid choice. Type granola bar, red apple, or pizza slice.")
    else:
        "Invalid choice. Choose floor vent or floorboard."
elif basket_choice == "smash the basket":
    print("f{user_name} punched the basket, but couldn't put a dent in it")
    print(f"{user_name} angrily chooses to find the key.")
    print(f"{user_name} looks around the empty room puzzled.")
    print(f"{user_name} spots an odd air vent in the bottom right corner of the room and a bouncy floorboard.")
    find_choice1 = input("Choose to look in floor vent or under the floorboard")
    if find_choice1 == "floor vent":
        print(f"{user_name} peers into the floor vent only to inhale a bunch of dust.")
        print(f"{user_name} decides to look under the misplaced floorboard instead.")
        print(f"{user_name} lifts the floorboard and sees a silver key sitting in the middle.")
        print(f"{user_name} puts the key in their inventory")
        print(
            f"{user_name} unlocks the basket and sees three food items: a granola bar, a  red apple, and a pizza slice.")
        foodstats_1 = input(f"Which item will {user_name} eat?")
        if foodstats_1 == "granola bar":
            health += 25
            print(f"{user_name}'s health has increased to {health}.")
        elif foodstats_1 == "pizza slice":
            health += 25
            print(f"{user_name}'s health has increased to {health}.")
        elif foodstats_1 == "red apple":
            health += 25
            print(f"{user_name}'s health has increased to {health}.")
        else:
            print("Invalid choice. Type granola bar, red apple, or pizza slice.")
    if find_choice1 == "floorboard":
        print(f"{user_name} lifts the floorboard and sees a silver key sitting in the middle.")
        print(f"{user_name} puts the key in their inventory.")
        print(
            f"{user_name} unlocks the basket and sees three food items: a granola bar, a  red apple, and a pizza slice.")
        foodstats_1 = input(f"Which item will {user_name} eat?")
        if foodstats_1 == "granola bar":
            health += 25
            print(f"{user_name}'s health has increased to {health}.")
        elif foodstats_1 == "pizza slice":
            health += 25
            print(f"{user_name}'s health has increased to {health}.")
        elif foodstats_1 == "red apple":
            health += 25
            print(f"{user_name}'s health has increased to {health}.")
        else:
            print("Invalid choice. Type granola bar, red apple, or pizza slice.")
    else:
        "Invalid choice. Choose floor vent or floorboard."


