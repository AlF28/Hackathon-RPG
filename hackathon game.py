
def prologue():
    print(""" 
                  *       +
            '                  |
        ()    .-.,="``"=.    - o -
              '=/_       \     |
           *   |  '=._    |
                \     `=./`,        '
             .   '=.__.=' `='      *
    +                         +
         O      *        '       .""")
    print(f"A lonely space cowboy travels the space in search of their home Earth. In an unforeseen turn of events, the" +
          "spaceship crashes with onto an unknown planet with a loud boom.")
    print("The space cowboy is now stranded on an unknown planet, and a broken ship. The player have no way of going back home.")
    print("The space cowboy is met with friendly faces, as humans on this planet came to help him after hearing the loud noise.")
    print("But alas! they were not humans! they were shape shifters of this planet, plotting to steal his items and ship parts. ")
    print("The player now awakes in a jail cell in their underwear, all their clothes and weapons are gone.")

def inventory():
    print(f"Select which inventory to open:\n"
          f"1. Weapons\n"
          "2. Stats\n"
          "3. Items\n"
          "4. Current Room")

def main():
    prologue()
    print()
    player_name = input("Enter the player's name: ")
    print(f"The jail cell door lay ajar,{player_name} walks out the jail cell door\n")
    print(f"{player_name} is faced with the choices:")
    menu= 0

    print(f"What will {player_name} do?: \n"
        "1. Go forward\n"
        "2. Check Inventory\n"
        "3. Observe the room\n")

    player_choice = input(f"What will {player_name} do?: ")

    if player_choice == "1":
            pass
    elif player_choice == "2":
            inventory()
    elif player_choice == "3":
            print(f"{player_name} observes the room. To {player_name}'s left is a small window, through which a slither of\n"
             f"moonlight shines. To {player_name}'s left is a toilet and sink, which looks very similar to earthly bathrooms,\n"
             f"makes {player_name} miss his home. In the corner,to the right, lays a pile of corpses. The smell coming from\n"
             f"the corpses makes {player_name} want to get out of here faster.\n")
            player_choice= input(f"Will {player_name} go to next room? ")
            if player_choice == "Yes" or "yes":
                pass
    else:
            print("Please enter a valid selection")



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








