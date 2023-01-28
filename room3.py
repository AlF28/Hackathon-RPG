def room_3():

    print("Player enters room 3")
    player_choice = input("Would Player like to observe the room? ")

    if player_choice == "Yes":
        print(f"Player looks around the room, it is unlike all the rooms he have been to. The room is filled with various books\n"
              f"of different languages. And on top of the pile of books sits a bunny\n")

        print("Would you look at that? A human appeared!. The last human I saw was millions of years ago.")
        print("The player stares with wide eyes.")
        print("Choose player input: "
              "1. How can the bunny talk?"
              "2. Hello nice to meet you Mr. Bunny")
        player_choice = input()

        if player_choice == "1":
            print("Bunny: How rude of you! I am not just any bunny, I am SIR BUNNY THE DISTINGUISHED. I have served\n"
                  "in the great thrice and have survived thrice, my grandfather has served in.....\n"
                  "The player decides to leave the room")
        else player_choice == "2":
            print("Bunny: Howdy human! I wonder how you ended up in this corner of galaxy. It is far away from\n"
                  "you home. But shoo now, I have to continue munching on these books ")

    else:
        print("The player leaves the room")

room_3()
