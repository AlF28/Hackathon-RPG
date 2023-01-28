# -implementing the player and enemy stats, as well as enemy counts,
# inventory also: weapon, food/items, weapon types with player
# and enemy stats (also enemy weapons),

# this will be gained from main beginning


# create the playerChar character that has health, att, def, name; should define inventory within main bc it
# will add user created objects inside
class Player:
    def __init__(self, name, health, attack, defense):
        self.playerName = name
        self.playerHealth = health
        self.playerAttack = attack
        self.playerDefense = defense


# when callin to an enemy in main, will pass in stats per each enemy
class Enemy:
    def __init__(self, health, attack, defense):
        self.enemyHealth = health
        self.enemyAttack = attack
        self.enemyDefense = defense

class Food:
    def __init__(self,statValue, name):
        self.statBoost = statValue
        self.itemName = name
    # displayDescription can be changed, does not have to be set to this
    def displayDescription(self):
        print ("This item is " , self.itemName, ",which provides +", self.statBoost,"to", player.playerName, "'s health. ")
        print("Tastes a little stale, but at least it isn't Hawaiian.")


# in main, write this:
# <player> finds two weapons. what will they choose to use? 1. sword 2.
class Weapon:
    def __init__(self,statValue,name):
        self.weaponStat = statValue
        self.weaponName = name




# test n main
inputName = input()
player = Player(inputName, 100, 10, 10)
print(player.playerName, player.playerAttack, player.playerDefense, player.playerHealth)

pizza = Food(35, "DeepDishPizza")
pizza.displayDescription()

saltines = Food(10, "Saltine Crackers")

# inventory should be added in main to allow easy access
# add to inventory using .append()
inventory = []
inventory.append(pizza)
inventory.append(saltines)
if inventory:
    print(player.playerName, "looks in their inventory. They find: ")
    for x in range(len(inventory)):
        print(x+1,".",inventory[x].itemName)
    print("What item will they choose? ") # give option for player input based on number, and also option for no selection

else:
    print("No items in inventory!")


print(player.playerAttack)

print(player.playerName, "has found two weapons, a sword and a bow. Which will they choose?")
choice = input()
if input() == "sword":
    sword = Weapon(4, "sword")
if input() == "bow":
    bow = Weapon(3,"bow")

# maybe add option to name the weapon?