# -implementing the player and enemy stats, as well as enemy counts,
# inventory also: weapon, food/items, weapon types with player
# and enemy stats (also enemy weapons),

# this will be gained from main beginning

# random is used for battle sequence
import random

# create the playerChar character that has health, att, def, name; should define inventory within main bc it
# will add user created objects inside
# limit the health value to be 100 or at least 0
class Player:
    def __init__(self,name, health, attack, defense):
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




# test n main
inputName = input()
player = Player(inputName, 100, 10, 10)
enemy1 = Enemy(50, 6, 8)

print(player.playerName, player.playerAttack, player.playerDefense, player.playerHealth)

pizza = Food(35, "DeepDishPizza")
pizza.displayDescription()

saltines = Food(10, "Saltine Crackers")

# inventory should be added in main to allow easy access
# add to inventory using .append()
# remove items somehow
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


# -------------------------------------------------------------- PLAYER FINDING WEAPON

print(player.playerName, "has found two weapons, a sword and a bow. Which will they choose?")
print("1. Sword")
print("2. Bow")
print("3.", player.playerName,"needs no weapon and will rely on their fists alone")

weaponChosen = True

while weaponChosen:
    choice = input()

    if choice == "1":
        print(player.playerName,"has received a sword! They equip the weapon for future use.")
        player.playerAttack = player.playerAttack + 5
        weaponChosen = False

    elif choice == "2":
        print(player.playerName,"has received a bow! They equip the weapon for future use.")
        player.playerAttack = player.playerAttack + 4
        weaponChosen = False

    elif choice == "3":
        print("Hard mode selected!")
        weaponChosen = False

    else:
        print("Not a valid input, silly! Try again: ")

# maybe add option to name the weapon?
print(player.playerName, "continues on.")

# ----------------------------------------------------- BEGINNING OF BATTLE SEQUENCE -----------------------------
# to start the battle sequence, change the variable battleBegin to = 1
# in addition, if we want to name the enemies (like actual names, or something like High Priestess (Alien race name) or
# General (Alien Race; you get the point), then change all instances of enemy1/ "Enemy" with that name

battleBegin = 0
print(player.playerName,"has encountered an enemy! The enemy glares menacingly and brandishes their weapon. The "
                        "blade gleams in the light.")
maxHealth = player.playerHealth
maxHealthE = enemy1.enemyHealth
# if player encounters an enemy, battleBegin = 1, i cant figure out boolean rn lol

while battleBegin == 1:

    print("What will", player.playerName, "do?")
    print(player.playerName,"'s Health:",player.playerHealth,"/",maxHealth)
    print("Enemy's Health:",enemy1.enemyHealth,"/",maxHealthE)
    print("1. Attack")
    print("2. Dodge")
    print("3. Open Inventory")
    playerChoice = input()
    if playerChoice == "1":
        # crit rand value = crit value == 1 then it crits, if anything else skip over; deal 50% more damage if crit
        # lucky hit! player swings and lands a lucky hit!
        damageDealt = random.randint(player.playerAttack-2,player.playerAttack+2) - enemy1.enemyDefense/4

        crit = random.randint(1,10)
        if crit == 1:
            damageDealt = damageDealt * 2
            print("Lucky hit!", player.playerName, "deals", damageDealt,"points of pain to the enemy!")
            enemy1.enemyHealth = enemy1.enemyHealth - damageDealt
        else:
            print(player.playerName,"attacks swiftly! They deliver", damageDealt,"damage to the enemy!")
            # can create a print line here that reads when enemy health is under 50%, and based on who the enemy is
            enemy1.enemyHealth = enemy1.enemyHealth - damageDealt

        if enemy1.enemyHealth >= 0:
            damageReceived = random.randint(enemy1.enemyAttack - 2, enemy1.enemyAttack +2) - player.playerDefense/4

            critE = random.randint(1, 10)
            if critE == 1:
                damageReceived = damageReceived * 2
                print("Unlucky! Enemy deals", damageDealt, "damage to", player.playerName,"!")
                player.playerHealth = player.playerHealth - damageReceived
            else:
                print("Enemy attacks",player.playerName,"! Enemy deals", damageReceived, "damage to", player.playerName,"!")
                player.playerHealth = player.playerHealth - damageReceived

        if (enemy1.enemyHealth < maxHealthE/3) and (enemy1.enemyHealth > 0):
            print("The enemy looks shaken! Deliver the final blow soon!")
        if enemy1.enemyHealth <= 0:
            print(player.playerName,"has defeated the enemy! They can progress to the next room!")
            battleBegin = 0

        if (player.playerHealth < maxHealth/3) and (player.playerHealth > 0):
            print("Oh no!", player.playerName,"feels themselves weakening. Don't give up,",player.playerName,"!")

        if player.playerHealth <= 0:
            print(player.playerName, "sputters, then collapses. They have been defeated by the enemy.")
            print("GAME OVER")
            battleBegin = 2;

    if playerChoice == 2:
        # dodge has a chance of dealing less damage without being hit, but has a higher chance of fail and being hit
        # not finished
        dodge = random.randint(1,10)

        if dodge >= 4:
            print("Enemy swings at",player.playerName,"")

    if playerChoice == 3:
        

    else:
        print(player.playerName,"grumbles. Give them a real choice, they only have so much time!")


