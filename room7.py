
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


# --------------------------------------------------------------------- ROOM 7 BEGIN
def room_7(player, inventory):
    print(player.playerName,"drags themselves into the next room, still coming down from the adrenaline of the last battle.")
    print("They can still feel the sweat on their brow, but they can only be thankful for their skill and a bit of luck "
          "that they've made it this far.")
    print(player.playerName,"closes their eyes and rests for a bit.")
    player.playerHealth = 100
    print(player.playerName,"'s health has been restored!")
    print("However,",player.playerName,"'s adventure is not over yet.")

    playerSleeping = 1
    while playerSleeping == 1:
        print("Wake", player.playerName, "up?")
        print("1. Yes")
        print("2. No")

        wakeChoice = input()
        if wakeChoice == "1":
            print(player.playerName,"yawns, and moves with a newfound energy.")
            playerSleeping = 0
        if wakeChoice == "2":
            print(player.playerName,"decides to nap for just a while longer.")
            print("Don't be lazy,", player.playerName,"!")

    print(player.playerName,"looks around, scanning for items. They spot an old woman, hunched over a fire in the corner.")
    print("""
            ( ( (                    ))
              ) ) )                 ((
                ( ( (           ___o___)
               '. ___ .'        |     |====O
              '  (> <) '        |_____|
            --ooO-(_)-Ooo--------------------
        
    """)
    print("Should", player.playerName,"approach her?")
    print("1. Yes")
    print("2. No")
    approachChoice = input()
    if approachChoice == "2":
        print(player.playerName,"recalls the shapeshifting nature of the Zaraleggian race, and decides against approaching her.")
        print("But....")
        print(player.playerName,"feels their stomach grumble. The aroma of her cooking reminds them of home, and they drift towards"
                                "the old woman anyways.")
    print(player.playerName,"approaches the old woman warily, seating themselves across her. She doesn't seem to"
                            "acknowledge them.")
    print("After a beat, she stops stirring her pot and speaks.")
    print("Old Woman: Many a traveler have set foot exactly where you have gone.")
    print("Old Woman: And every single one of them never achieve the ending they seek.")
    print("Old Woman: Perhaps if I were younger, I'd have done the same. But these bones would've never survived.")
    print("Old Woman: Your battles may have been tough so far, but they will be nothing like what is behind that door.")
    print("Old Woman: It may not be much, but I can offer you this.")
    print("The old woman hands", player.playerName,"a wooden bowl of soup.")
    print("Old Woman: Use it well. And hope that our paths never cross again.")
    print("The old woman turns her attention back to her pot. She doesn't seem to have anything else to say.")
    print(player.playerName,"saves the soup for later.")
    print("'Grandma's Soup' added to Bag!")
    soup = Food(100,"Grandma's Soup")
    inventory.append(soup)

    print(player.playerName,"stands up and looks around. In front of them towers an intimidating door. Perhaps there is still"
                            "something to discover before passing through.")
    print("What will", player.playerName,"do?")
    print("1. Enter through the door")
    print("2. Explore further")
    finalChoice = input()
    if finalChoice == "2":
        print(player.playerName, "moves around the corners of the room.")
        print(player.playerName,"finds a bag of Airplane Peanuts!")
        peanuts = Food(20,"AirplanePeanuts")
        inventory.append(peanuts)
        print(player.playerName,"finds a Twinkie on the ground!")
        twinkie = Food(15, "Twinkie")
        inventory.append(twinkie)
        print("The items have been added to Bag.")

    print(player.playerName,"knows they cannot delay the inevitable any longer.")
    print(player.playerName,"feels the anxiety weighing on them.")
    print(player.playerName,"knows this will be the hardest thing they've faced yet.")
    print(player.playerName, "opens the door and enters the Throne Room.")

# ----------------------------------------------------ROOM 7 END
#main
inputName = input()
player = Player(inputName, 100, 10, 10)
enemy1 = Enemy(500, 6, 8)

pizza = Food(35, "DeepDishPizza")
saltines = Food(10, "DrySaltines")

inventory = []
inventory.append(pizza)
inventory.append(saltines)

room_7(player,inventory)