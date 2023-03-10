
class Player:
    def __init__(self, name, health, attack, defense):
        self.playerName = name
        self.playerHealth = health
        self.playerAttack = attack
        self.playerDefense = defense

class Enemy:
    def __init__(self, health, attack, defense):
        self.enemyHealth = health
        self.enemyAttack = attack
        self.enemyDefense = defense

class Food:
    def __init__(self,statValue, name):
        self.statBoost = statValue
        self.itemName = name

# ---------------------------------------------------------------------- ROOM 6 START FUNCTION
def room_6(player, inventory):
    # wish i could implement a ver where they explicitly have clothes or not but o well
    print(player.playerName,"walks into the room, and is met with a sudden and bitter cold. They shudder, deciding they"
                            "will spend as little time in this room as possible.")
    print("Where will",player.playerName,"go?")
    print("1. Left")
    print("2. Right")
    room6Input = input()

    if room6Input == "1":
        print(player.playerName,"decides on left. They find a mirror, one with a height that easily spans 3 feet above "
                                "their head.")
        print(player.playerName,"notices their dishevelled appearance, and quickly brushes the dirt off their face and body."
                                "They flash a quick smile in the mirror; much better.")
        print("""     
                     .------.        .------.
                    /        \      /        |
                   /_        _\    /_        _|
                  // \      / ||  // \      /  | 
                  |\__\    /__/|  |\__\    /__/|
                   \    ||    /    \    ||    /
                    \        /      \        /
                     \  __  /        \  __  /
                      '.__.'          '.__.'
                       |  |            |  |
                       |  |            |  |
            """)
        print("On the mirror,",player.playerName,"notices a photo of two Zaraleggians. Attached to the photo is a small "
                                                 "candy.")
        print("Take the candy?")
        print("1. Yes")
        print("2. No")

        candyChoice = input()
        if candyChoice == "1":
            print(player.playerName,"peels the candy off the photo. It's lemon flavored. They add it to their bag.")
            candy = Food(15,"LemonCandy")
            inventory.append(candy)
        elif candyChoice == "2":
            print(player.playerName,"leaves the candy. They'd rather not get cavities today.")


    elif room6Input == "2":
        print(player.playerName,"strides to the right, in the direction of a table. On it rests a slip of paper.")
        print("The paper reads, in messy Zaraleggian: ")
        print(" 'REMEMBER TO PAY HEATING BILLS' ")
        print("A box also rests on the desk. Grab it?")
        print("1. Yes")
        print("2. No")

        boxChoice = input()
        if boxChoice == "1":
            print(player.playerName,"grabs the box and examines it. It appears to be sealed by a lock, with a "
                                    "sequence needed to open it.")
            print("""
                       +--------------+
                      /              /|
                     /              / |
                    *--------------*  |
                    |     ____     |  |
                    |    |    |    |  |
                    |    |----|    |  |
                    |              |  |
                    |              | /
                    |              |/
                    *--------------*
            """)
            print("Text above the seal reads: How many letters are in the name of the resident of the third room?")
            boxCode = input()

            if boxCode == "5":
                print("Aha! The lid pops open. Inside is a packet of ramen! Take it? Y or N")
                ramenChoice = input()
                if ramenChoice == "Y" or "y":
                    print(player.playerName," takes the ramen.")
                    ramen = Food(55, "RamenNoodles")
                    inventory.append(ramen)
                elif ramenChoice == "N" or "n":
                    print(player.playerName,"chooses not to take the ramen. It looks like someone else treasures it, anyways.")
            else:
                print(player.playerName,"enters the code, but the lock doesn't seem to budge. As they struggle with the "
                                        "box, a rodent leaps into their bag!")
                if inventory:
                    print("It is too late by the time the rodent takes off with", player.playerName,"'s food. Lost the "
                                                                                                    "last item added to bag.")
                    lastItem = len(inventory)
                    inventory.remove(inventory[lastItem-1])

                else:
                    print("The rodent squirms around, before eventually jumping out and running away. How odd.")
        elif boxChoice == "2":
            print(player.playerName,"would rather not think about puzzles now. They leave the box.")

    print(player.playerName,"scans the room once more. If they're being honest, it is quite barren, aside from"
                            "one very long and large bed.")
    print(player.playerName,"would rather not search a bed for items of use.")
    print("The cold begins to become more bothersome.")
    print(player.playerName,"moves on to the next room.")

# -------------------------------------------------------------------------------ROOM 6 END FUNCTION
#main
inputName = input()
player = Player(inputName, 100, 10, 10)
enemy1 = Enemy(500, 6, 8)

pizza = Food(35, "DeepDishPizza")
saltines = Food(10, "DrySaltines")

inventory = []
inventory.append(pizza)
inventory.append(saltines)

room_6(player,inventory)
