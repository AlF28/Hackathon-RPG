import sys,time, random


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)


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

# ----- ENDINGS
def ending_1(player):
    print_slow(f"{player.playerName} grasps the metal piece, gripping it firm in their hands before leaving.\n")
    print_slow(f"They make a quick exit, evading any vengeful Zaraleggians along the way.\n")
    print_slow(f"But before they leave,{player.playerName} stops to pick up one last cargo before they depart the planet.\n")
    print_slow(f"Surprisingly to {player.playerName}, the old woman does not seem shocked to see them victorious.\n")
    print_slow(f"{player.playerName} sets off with their new partner in search of Planet Earth once more.\n")
    print("YOU'VE DEFEATED THE ZARALEGGIANS AND ACHIEVED FREEDOM! FIN.")


def ending_2(player):
    print_slow(f"{player.playerName} grasps the crown, examining it before placing it atop their head. \n")
    print_slow(f"The headpiece is somewhat heavy, but {player.playerName} knows the value measured by such weight.\n")
    print_slow(f"Zaraleggians, upon learning of the transition of power, quickly accept the new ruler; whether it is\n"
               f"due to reverence or fear is contested.\n")
    print_slow(f"{player.playerName} is no longer the same lonely cowboy they once were; instead, they find purpose in \n"
               f"ruling the Zaraleggians and growing their power within the cosmos.\n")
    print("YOU'VE USURPED THE ZARALEGGIAN THRONE AND BECOME THEIR RULER! FIN.")

#main
inputName = input()
player = Player(inputName, 100, 10, 10)
enemy1 = Enemy(500, 6, 8)

pizza = Food(35, "DeepDishPizza")
saltines = Food(10, "DrySaltines")

inventory = []
inventory.append(pizza)
inventory.append(saltines)

# ------------- AFTER DEFEAT OF KING

print_slow(f"{player.playerName}watches as the Zaraleggian king collapses and doesn't get back up.\n")
print_slow(f"The energy from the battle still courses through {player.playerName}'s bones, but they succeeded. They won.\n")
print_slow(f"Now that the king has been slain, {player.playerName} has all they need to return back to their ship. They lean \n"
                                                            "to grab the missing ship component from the king's body.\n")
print_slow(f"However, {player.playerName}'s eyes are caught by the glimmer of the Zaralegglian crown, and all the power it holds.\n")
print("What will",player.playerName,"do?")
print("1. Return to their home and escape the alien planet")
print("2. Become the ruler of an alien race")

endingChoice = input()
if endingChoice == "1":
    ending_1(player)
elif endingChoice == "2":
    ending_2(player)