import random
import sys,time

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)


#class player
class Player:
    def __init__(self, name, health, attack, defense):
        self.playerName = name
        self.playerHealth = health
        self.playerAttack = attack
        self.playerDefense = defense
#class food
class Food:
    def __init__(self,statValue, name):
        self.statBoost = statValue
        self.itemName = name

#enemy class
class Enemy:
    def __init__(self, health, attack, defense):
        self.enemyHealth = health
        self.enemyAttack = attack
        self.enemyDefense = defense

#prologue story
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
    print_slow(f"A lonely space cowboy travels the space in search of their home Earth. In an unforeseen turn of events, the" +
          "spaceship crashes with onto an unknown planet with a loud boom.\n")
    print_slow("The space cowboy is now stranded on an unknown planet, and a broken ship. The player have no way of going back home.\n")
    print_slow("The space cowboy is met with friendly faces, as humans on this planet came to help him after hearing the loud noise.\n")
    print_slow("But alas! they were not humans! they were shape shifters of this planet called the ZARALEGG,\n"
          "plotting to steal his items and ship parts.\n")
    print_slow("The player now awakes in a jail cell in their underwear, all their clothes and weapons are gone.\n")


#boss fight 1
def boss_fight1(player):
    print(f"{player.playerName} enters the next room. The floor creeks with each step.")
    print(f"{player.playerName} looks around and sees the walls covered with poisonous goo.\n"
          f"Something drops from above, and lands with a loud thud!.\n")
    print("""
       ______
         /_.  ._\
        (( \\// ))
         \\ \/ //
          \\/\//
     \\\  ( '' )  ///
      )))  \__/  (((
     (((.'__||__'.)))
      \\  )    (  //
       \\/.'  '.\//
        \/ |,,| \/
      |  |
           |  |
           //\\
          //  \\
         ||    ||
         ||    ||
         ||    ||
      ___))    ((___
     (____)    (____)             """)


    inventory = []
    zaralegg_general_1 = Enemy(60, 6, 8) #enemy stats
    battleBegin = 1
    print_slow(player.playerName, "has encountered an enemy! The enemy glares menacingly and brandishes their weapon. The\n"
                             "blade gleams in the light.\n")
    print_slow("I am the great first general of the Zaralegg race, and YOU! HOW DARE YOU TRY AND ESCAPE!!!\n"
          "I will show you puny human the power of the ZARALEGG RACE. MUAHAHAHA\n")
    print_slow(f"{player.playerName} readies their weapon, confident in their skills.\n")

    maxHealth = 100
    maxHealthE = 60
    # if player encounters an enemy, battleBegin = 1, i cant figure out boolean rn lol

    while battleBegin == 1:

        print("What will", player.playerName, "do?")
        print(player.playerName, "'s Health:", player.playerHealth, "/", maxHealth)
        print("Enemy's Health:", zaralegg_general_1.enemyHealth, "/", maxHealthE)
        print("1. Attack")
        print("2. Dodge")
        print("3. Open Inventory")

        playerChoice = input()

        if playerChoice == "1":
            playerMiss = random.randint(1, 20)
            enemyMiss = random.randint(1, 20)
            # player attacks here
            if playerMiss == 1:
                print("Oh no!", player.playerName, "slips, and misses!")
            else:
                damageDealt = random.randint(player.playerAttack - 2, player.playerAttack + 2) - zaralegg_general_1.enemyDefense / 4

                crit = random.randint(1, 10)
                if crit == 1:
                    damageDealt = damageDealt * 2
                    print("Lucky hit!", player.playerName, "deals", damageDealt, "points of pain to the enemy!")
                    zaralegg_general_1.enemyHealth = zaralegg_general_1.enemyHealth - damageDealt
                else:
                    print(player.playerName, "attacks swiftly! They deliver", damageDealt, "damage to the enemy!")
                    zaralegg_general_1.enemyHealth = zaralegg_general_1.enemyHealth - damageDealt

            if zaralegg_general_1.enemyHealth >= 0:
                # enemy attacks here
                damageReceived = random.randint(zaralegg_general_1.enemyAttack - 2,
                                                zaralegg_general_1.enemyAttack + 2) - player.playerDefense / 4

                if enemyMiss == 1:
                    print(player.playerName, "cheers as the enemy misses. Lucky turn!")
                else:
                    critE = random.randint(1, 10)
                    if critE == 1:
                        damageReceived = damageReceived * 2
                        print("Unlucky! Enemy deals", damageDealt, "damage to", player.playerName, "!")
                        player.playerHealth = player.playerHealth - damageReceived
                    else:
                        print("Enemy attacks", player.playerName, "and deals", damageReceived, "damage to",
                              player.playerName, "!")
                        player.playerHealth = player.playerHealth - damageReceived

            # now check if enemy or player are dead
            if (zaralegg_general_1.enemyHealth < maxHealthE / 3) and (zaralegg_general_1.enemyHealth > 0):
                print("The enemy looks shaken! Deliver the final blow soon!")
            if zaralegg_general_1.enemyHealth <= 0:
                print(player.playerName, "has defeated the enemy! They can progress to the next room!\n")
                battleBegin = 0
                room_2(player, inventory)

            if (player.playerHealth < maxHealth / 3) and (player.playerHealth > 0):
                print("Oh no!", player.playerName, "feels themselves weakening. Don't give up,", player.playerName, "!")

            if player.playerHealth <= 0:
                print(player.playerName, "sputters, then collapses. They have been defeated by the enemy.")
                print("GAME OVER")
                battleBegin = 2

        elif playerChoice == "2":
            # dodge has a chance of dealing less damage without being hit, but has a higher chance of fail and being hit
            # not finished
            dodge = random.randint(1, 10)

            if dodge >= 4:
                missHit = random.randint(zaralegg_general_1.enemyAttack - 2, zaralegg_general_1.enemyAttack + 2)
                print(player.playerName, "prepares to leap out of the way, but they miscalculate their enemy! "
                                         "The hit lands, dealing", missHit, "damage along the way.")
                player.playerHealth = player.playerHealth - missHit
            else:
                dodgeDamage = random.randint(player.playerAttack - 2, player.playerAttack + 2) - zaralegg_general_1.enemyDefense / 2
                print(player.playerName,
                      "readies themself and springs out of the way at the last second. They strike at "
                      "the enemy, and deal", dodgeDamage, "damage.")
                zaralegg_general_1.enemyHealth = zaralegg_general_1.enemyHealth - dodgeDamage

            if (zaralegg_general_1.enemyHealth < maxHealthE / 3) and (zaralegg_general_1.enemyHealth > 0):
                print("The enemy looks shaken! Deliver the final blow soon!")
            if zaralegg_general_1.enemyHealth <= 0:
                print(player.playerName, "has defeated the enemy! They can progress to the next room!\n")
                battleBegin = 0
                room_2(player, inventory)

            if (player.playerHealth < maxHealth / 3) and (player.playerHealth > 0):
                print("Oh no!", player.playerName, "feels themselves weakening. Don't give up,", player.playerName, "!")

            if player.playerHealth <= 0:
                print(player.playerName, "sputters, then collapses. They have been defeated by the enemy.")
                print("GAME OVER")
                battleBegin = 2

        elif playerChoice == "3":
            print(f"{player.playerName} opens their bag. They find:")

            if inventory:
                for x in range(len(inventory)):
                    print(x + 1, ".", inventory[x].itemName, ": Provides +", inventory[x].statBoost, " health")
                endValue = len(inventory)
                print(endValue + 1, ". Close inventory")
                print("What item will they choose?")

                inventoryChoice = input()
                convert = int(inventoryChoice)

                if convert != endValue + 1:
                    itemConsumed = inventory[convert - 1]
                    player.playerHealth = player.playerHealth + itemConsumed.statBoost
                    if player.playerHealth > 100:
                        player.playerHealth = 100

                    inventory.remove(itemConsumed)
                    print(f"{player.playerName}consumed the {itemConsumed.itemName}",
                          f"and smiles. Tastes good! Their health is now",
                          f"{player.playerHealth}out of 100.")

            else:
                print(player.playerName, "blinks, then tips their bag upside down. Nothing falls out.")

        else:
            print(player.playerName, "grumbles. Give them a real choice, they only have so much time!")
#boss fight 2
def boss_fight2(player, inventory):
    print(f"{player.playerName} slowly opens the door to the next room, checking for another anthropomorphic animal.\n")
    print(f"{player.playerName} determines the coast is clear and tip toes in.")
    print("Thud!")
    print("""
          _..._
         .'     '.
        /`\     /`\    |\
       (__|     |__)|\  \\  /|
       (     "     ) \\ || //
        \         /   \\||//
         \   _   /  |\|`  /
          '.___.'   \____/
           (___)    (___)
         /`     `\  / /
        |         \/ /
        | |     |\  /
        | |     | "`
        | |     |
        | |     |
        |_|_____|
       (___)_____)
       /    \   |
      /   |\|   |
     //||\\  Y  |
    || || \\ |  |
    |/ \\ |\||  |
        \||__|__|
         (___|___)
         /   A   \
        /   / \   \
       \___/   \___/    """)
    print(f"Suddenly {player.playerName} is lying on the floor when a figure appears out of the shadows.")
    print(f"{player.playerName} strains their head to look up at the tall, lanky alien standing in front of them. ")
    print_slow("\"Hello, human. You can call me Professor Z.\" the alien said plainly.\n")
    print_slow("\"I know you're thinking 'I don't care who you are. Let me go!', but let me finish.\" said Professor Z\n")
    print_slow("Professor Z turned around and pulled out what seemed to be chalk board that uses lasers.\n")
    print_slow("\"What you're wrapped in is my infalliable zaralegg fiber silk. I'm the first one to synthesize g chain amin... \\n"")
    print_slow(f"{player.playerName} could feel the silk melting, allowing them to slowly pull it off during the lecture.\n")
    print_slow("\"So that's all to say that my invention is perfect for capturing human speci-\"\n")
    print_slow("Professor Z turned around to find his specimen had freed themselves from the special unbreakable fiber.\n")
    print_slow("\"Impossible! I've been working on this for eleventeen gorbles. Well, now I have to kill you.\" Professor Z announced.\n")

    enemy2 = Enemy(100, 10, 15)
    battleBegin = 1
    maxHealth = 100
    maxHealthE = 100
    # if player encounters an enemy, battleBegin = 1, i cant figure out boolean rn lol

    while battleBegin == 1:

        print("What will", player.playerName, "do?\n")
        print(player.playerName, "'s Health:", player.playerHealth, "/", maxHealth)
        print("Enemy's Health:", enemy2.enemyHealth, "/", maxHealthE)
        print("1. Attack")
        print("2. Dodge")
        print("3. Open Inventory")
        playerChoice = input()
        if playerChoice == "1":
            playerMiss = random.randint(1, 20)
            enemyMiss = random.randint(1, 20)
            # player attacks here
            if playerMiss == 1:
                print("Oh no!", player.playerName, "slips, and misses!")
            else:
                damageDealt = random.randint(player.playerAttack - 2, player.playerAttack + 2) - enemy2.enemyDefense / 4

                crit = random.randint(1, 10)
                if crit == 1:
                    damageDealt = damageDealt * 2
                    print("Lucky hit!", player.playerName, "deals", damageDealt, "points of pain to the enemy!")
                    enemy2.enemyHealth = enemy2.enemyHealth - damageDealt
                else:
                    print(player.playerName, "attacks swiftly! They deliver", damageDealt, "damage to the enemy!")
                    enemy2.enemyHealth = enemy2.enemyHealth - damageDealt

            if enemy2.enemyHealth >= 0:
                # enemy attacks here
                damageReceived = random.randint(enemy2.enemyAttack - 2,
                                                enemy2.enemyAttack + 2) - player.playerDefense / 4

                if enemyMiss == 1:
                    print(player.playerName, "cheers as the enemy misses. Lucky turn!")
                else:
                    critE = random.randint(1, 10)
                    if critE == 1:
                        damageReceived = damageReceived * 2
                        print("Unlucky! Enemy deals", damageDealt, "damage to", player.playerName, "!")
                        player.playerHealth = player.playerHealth - damageReceived
                    else:
                        print("Enemy attacks", player.playerName, "and deals", damageReceived, "damage to",
                              player.playerName, "!")
                        player.playerHealth = player.playerHealth - damageReceived

            # now check if enemy or player are dead
            if (enemy2.enemyHealth < maxHealthE / 3) and (enemy2.enemyHealth > 0):
                print("The enemy looks shaken! Deliver the final blow soon!")
            if enemy2.enemyHealth <= 0:
                print(player.playerName, "has defeated the enemy! They can progress to the next room!")
                battleBegin = 0
                room_4(player, inventory)

            if (player.playerHealth < maxHealth / 3) and (player.playerHealth > 0):
                print("Oh no!", player.playerName, "feels themselves weakening. Don't give up,", player.playerName, "!")

            if player.playerHealth <= 0:
                print(player.playerName, "sputters, then collapses. They have been defeated by the enemy.")
                print("GAME OVER")
                battleBegin = 2

        elif playerChoice == "2":
            # dodge has a chance of dealing less damage without being hit, but has a higher chance of fail and being hit
            # not finished
            dodge = random.randint(1, 10)

            if dodge >= 4:
                missHit = random.randint(enemy2.enemyAttack - 2, enemy2.enemyAttack + 2)
                print(player.playerName, "prepares to leap out of the way, but they miscalculate their enemy! "
                                         "The hit lands, dealing", missHit, "damage along the way.")
                player.playerHealth = player.playerHealth - missHit
            else:
                dodgeDamage = random.randint(player.playerAttack - 2, player.playerAttack + 2) - enemy2.enemyDefense / 2
                print(player.playerName,
                      "readies themself and springs out of the way at the last second. They strike at "
                      "the enemy, and deal", dodgeDamage, "damage.")
                enemy2.enemyHealth = enemy2.enemyHealth - dodgeDamage

            if (enemy2.enemyHealth < maxHealthE / 3) and (enemy2.enemyHealth > 0):
                print("The enemy looks shaken! Deliver the final blow soon!")
            if enemy2.enemyHealth <= 0:
                print(player.playerName, "has defeated the enemy! They can progress to the next room!")
                battleBegin = 0
                room_4(player, inventory)

            if (player.playerHealth < maxHealth / 3) and (player.playerHealth > 0):
                print("Oh no!", player.playerName, "feels themselves weakening. Don't give up,", player.playerName, "!")

            if player.playerHealth <= 0:
                print(player.playerName, "sputters, then collapses. They have been defeated by the enemy.")
                print("GAME OVER")
                battleBegin = 2

        elif playerChoice == "3":
            print(player.playerName, "opens their bag. They find:")

            if inventory:
                for x in range(len(inventory)):
                    print(x + 1, ".", inventory[x].itemName, ": Provides +", inventory[x].statBoost, " health")
                endValue = len(inventory)
                print(endValue + 1, ". Close inventory")
                print("What item will they choose?")

                inventoryChoice = input()
                convert = int(inventoryChoice)

                if convert != endValue + 1:
                    itemConsumed = inventory[convert - 1]
                    player.playerHealth = player.playerHealth + itemConsumed.statBoost
                    if player.playerHealth > 100:
                        player.playerHealth = 100

                    inventory.remove(itemConsumed)
                    print(player.playerName, "consumed the", itemConsumed.itemName,
                          "and smiles. Tastes good! Their health is now",
                          player.playerHealth, "out of 100.")
            else:
                print(player.playerName, "blinks, then tips their bag upside down. Nothing falls out.")

        else:
            print(player.playerName, "grumbles. Give them a real choice, they only have so much time!")

def boss_fight3(player, inventory):
        print(f"The cold air follows, as {player.playerName} steps into the next room\n")
        print(f"Here {player.playerName} meets a man..err...alien")
        print(f"The alien just stares at {player.playerName}")
        print(f"{player.playerName}: Can I help you?")
        print(f"hsssssssssssssssssssssssssssss\n QUE EPIC MUSIC")
        print(""".     .       .  .   . .   .   . .    +  .
          .     .  :     .    .. :. .___---------___.
               .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
            .  :       .  .  .:../:            . .^  :.:\.
                .   . :: +. :.:/: .   .    .        . . .:\
         .  :    .     . _ :::/:               .  ^ .  . .:\
          .. . .   . - : :.:./.                        .  .:\
          .      .     . :..|:                    .  .  ^. .:|
            .       . : : ..||        .                . . !:|
          .     . . . ::. ::\(                           . :)/
         .   .     : . : .:.|. ######              .#######::|
          :.. .  :-  : .:  ::|.#######           ..########:|
         .  .  .  ..  .  .. :\ ########          :######## :/
          .        .+ :: : -.:\ ########       . ########.:/
            .  .+   . . . . :.:\. #######       #######..:/
              :: . . . . ::.:..:.\           .   .   ..:/
           .   .   .  .. :  -::::.\.       | |     . .:/
              .  :  .  .  .-:.":.::.\             ..:/
         .      -.   . . . .: .:::.:.\.           .:/
        .   .   .  :      : ....::_:..:\   ___.  :/
           .   .  .   .:. .. .  .: :.:.:\       :/
             +   .   .   : . ::. :.:. .:.|\  .:/|
             .         +   .  .  ...:: ..|  --.:|
        .      . . .   .  .  . ... :..:.."(  ..)"
         .   .       .      :  .   .: ::/  .  .::\              """)
        enemy3 = Enemy(120, 12, 10)
        battleBegin = 1
        maxHealth = player.playerHealth
        maxHealthE = enemy3.enemyHealth
        # if player encounters an enemy, battleBegin = 1, i cant figure out boolean rn lol

        while battleBegin == 1:

            print("What will", player.playerName, "do?\n")
            print(player.playerName, "'s Health:", player.playerHealth, "/", maxHealth)
            print("Enemy's Health:", enemy3.enemyHealth, "/", maxHealthE)
            print("1. Attack")
            print("2. Dodge")
            print("3. Open Inventory")
            playerChoice = input()
            if playerChoice == "1":
                playerMiss = random.randint(1, 20)
                enemyMiss = random.randint(1, 20)
                # player attacks here
                if playerMiss == 1:
                    print("Oh no!", player.playerName, "slips, and misses!")
                else:
                    damageDealt = random.randint(player.playerAttack - 2,
                                                 player.playerAttack + 2) - enemy3.enemyDefense / 4

                    crit = random.randint(1, 10)
                    if crit == 1:
                        damageDealt = damageDealt * 2
                        print("Lucky hit!", player.playerName, "deals", damageDealt, "points of pain to the enemy!")
                        enemy3.enemyHealth = enemy3.enemyHealth - damageDealt
                    else:
                        print(player.playerName, "attacks swiftly! They deliver", damageDealt, "damage to the enemy!")
                        enemy3.enemyHealth = enemy3.enemyHealth - damageDealt

                if enemy3.enemyHealth >= 0:
                    # enemy attacks here
                    damageReceived = random.randint(enemy3.enemyAttack - 2,
                                                    enemy3.enemyAttack + 2) - player.playerDefense / 4

                    if enemyMiss == 1:
                        print(player.playerName, "cheers as the enemy misses. Lucky turn!")
                    else:
                        critE = random.randint(1, 10)
                        if critE == 1:
                            damageReceived = damageReceived * 2
                            print("Unlucky! Enemy deals", damageDealt, "damage to", player.playerName, "!")
                            player.playerHealth = player.playerHealth - damageReceived
                        else:
                            print("Enemy attacks", player.playerName, "and deals", damageReceived, "damage to",
                                  player.playerName, "!")
                            player.playerHealth = player.playerHealth - damageReceived

                # now check if enemy or player are dead
                if (enemy3.enemyHealth < maxHealthE / 3) and (enemy3.enemyHealth > 0):
                    print("The enemy looks shaken! Deliver the final blow soon!")
                if enemy3.enemyHealth <= 0:
                    print(player.playerName, "has defeated the enemy! They can progress to the next room!")
                    print("The alien finally speaks: My liege I have failed you")
                    battleBegin = 0
                    room_6(player, inventory)

                if (player.playerHealth < maxHealth / 3) and (player.playerHealth > 0):
                    print("Oh no!", player.playerName, "feels themselves weakening. Don't give up,", player.playerName,
                          "!")

                if player.playerHealth <= 0:
                    print(player.playerName, "sputters, then collapses. They have been defeated by the enemy.")
                    print("GAME OVER")
                    battleBegin = 2

            elif playerChoice == "2":
                # dodge has a chance of dealing less damage without being hit, but has a higher chance of fail and being hit
                # not finished
                dodge = random.randint(1, 10)

                if dodge >= 4:
                    missHit = random.randint(enemy3.enemyAttack - 2, enemy3.enemyAttack + 2)
                    print(player.playerName, "prepares to leap out of the way, but they miscalculate their enemy! "
                                             "The hit lands, dealing", missHit, "damage along the way.")
                    player.playerHealth = player.playerHealth - missHit
                else:
                    dodgeDamage = random.randint(player.playerAttack - 2,
                                                 player.playerAttack + 2) - enemy3.enemyDefense / 2
                    print(player.playerName,
                          "readies themself and springs out of the way at the last second. They strike at "
                          "the enemy, and deal", dodgeDamage, "damage.")
                    enemy3.enemyHealth = enemy3.enemyHealth - dodgeDamage

                if (enemy3.enemyHealth < maxHealthE / 3) and (enemy3.enemyHealth > 0):
                    print("The enemy looks shaken! Deliver the final blow soon!")
                if enemy3.enemyHealth <= 0:
                    print(player.playerName, "has defeated the enemy! They can progress to the next room!")
                    print("The alien finally speaks: My liege I have failed you")
                    battleBegin = 0
                    room_6(player, inventory)

                if (player.playerHealth < maxHealth / 3) and (player.playerHealth > 0):
                    print("Oh no!", player.playerName, "feels themselves weakening. Don't give up,", player.playerName,
                          "!")

                if player.playerHealth <= 0:
                    print(player.playerName, "sputters, then collapses. They have been defeated by the enemy.")
                    print("GAME OVER")
                    battleBegin = 2

            elif playerChoice == "3":
                print(player.playerName, "opens their bag. They find:")

                if inventory:
                    for x in range(len(inventory)):
                        print(x + 1, ".", inventory[x].itemName, ": Provides +", inventory[x].statBoost, " health")
                    endValue = len(inventory)
                    print(endValue + 1, ". Close inventory")
                    print("What item will they choose?")

                    inventoryChoice = input()
                    convert = int(inventoryChoice)

                    if convert != endValue + 1:
                        itemConsumed = inventory[convert - 1]
                        player.playerHealth = player.playerHealth + itemConsumed.statBoost
                        if player.playerHealth > 100:
                            player.playerHealth = 100

                        inventory.remove(itemConsumed)
                        print(player.playerName, "consumed the", itemConsumed.itemName,
                              "and smiles. Tastes good! Their health is now",
                              player.playerHealth, "out of 100.")
                else:
                    print(player.playerName, "blinks, then tips their bag upside down. Nothing falls out.")

            else:
                print(player.playerName, "grumbles. Give them a real choice, they only have so much time!")
#final boss
def final_boss(player, inventory):
    print(f"{player.playerName} steps into the throne room, a chill runs down their spine")
    print(f"So you finally made it here, you have tasted the food I sent you,\n"
          f"but now you will taste DEATH")
    print("""
                                                              / /
                                                            | | |  /
                                                             \|_|_/
                                                           ,--/.__/--'
                           _.-/   _   \-._                    .'|
                         .'::(_,-' `-._)::`.                  |:|
                        (:::::::::::::::::::)                .':|
                         \_:::;;;::::;;;:::/    /            |::|
                 \        ,---'..\::/..`-.'    /             |::|
                  \       \_;:....|'...:_ )   /             .'=||
                   \.       )---. )_.--< (   /'             ||=||
                    \\     //|:: /--\:::\\\ //             _||= |
                     \\   ||::\:|----|:/:||/--.______,--==' \ - /
              -._     \`.  \\:|:|-- -|:\:/-.,,\\  .----'//'_.`-'
          \.     `-.   \ \ _|:|:|-- -|::||::\,,||-'////---' |/'
           \\       `._)\ / |\/:|-/|--\:/|. :\_,'---'       /
            \\_      /,,\/:.'\\/-.'`-.-//  \ |
            /`\-    //,,,' |-.\-'\--/|-/ ./| |             /
             /||-   ||, /| |\. |.-==-.| . /| |            | /
     __  |    /||-  ||,,\- | .  \;;;;/ .  .':/         _,-=/-'
    /  \//    /||-  ' `,-|::\ . \,..,/   /: /         /.-'
    ,--||      /||-/.-.'  \  `._ `--' _.' .'|        //
    .--||`.    /||//\ '   |-'.___`___' _,'|//       /;
      /\| \     ///\ /     \\_`-.`--`-'_==|'       /;'
     / |'\ \.   //\ /       \_\__)\`==-_'_|       / /
      .'  \.=`./|\ /          \`-- \--._/_/------( /
           \.=| `_/|-          |\`-| -/| `--------'
            \\` ./|-/-         |\`-| |-|     ________
             `--\ |=|'        _|\`-| |-|----'.-._ ..\`-.
                 -|-|-     .-':`-;-| |./.-.-( | ||..|=-\\
                 `'= /'   / ,--.:|-| ||_|_|_|_|-'__ .`-._)
                  /|-|- .' /\ \ \|-` \\ ____,---'  `-. ..|
                   /\=\/..'\ \_>-'`-\ \'              \ .|
                   `,-':/\`.>' |\/ \/\ \              `- |
                   //::/\ \/_/|-' \/| \ `.            / ||
                  / (:|\ \/) \ \|.'-'  `-\\          |;:|\_
                 || |:`-/:.'-|-' \|       \\          `;_\-`-._
                 \\=/:_/::/\| \|          |\\            `-._ =`-._
                  \_)' |:|                | //               `--.__`-.
                       |:|                                         )\|
                       /;/                                         / (\_
                      / /                                         |\\;;_`-.
                    _/ /                                          ' `---\.-\
                   /::||
                  /:::/
                 //;;'             
                 `-'                                                            """)

    enemy4 = Enemy(170, 14, 14)
    battleBegin = 1
    maxHealth = 100
    maxHealthE = 170
    # if player encounters an enemy, battleBegin = 1, i cant figure out boolean rn lol

    while battleBegin == 1:

        print("What will", player.playerName, "do?\n")
        print(player.playerName, "'s Health:", player.playerHealth, "/", maxHealth)
        print("Enemy's Health:", enemy4.enemyHealth, "/", maxHealthE)
        print("1. Attack")
        print("2. Dodge")
        print("3. Open Inventory")
        playerChoice = input()
        if playerChoice == "1":
            playerMiss = random.randint(1, 20)
            enemyMiss = random.randint(1, 20)
            # player attacks here
            if playerMiss == 1:
                print("Oh no!", player.playerName, "slips, and misses!")
            else:
                damageDealt = random.randint(player.playerAttack - 2,
                                             player.playerAttack + 2) - enemy4.enemyDefense / 4

                crit = random.randint(1, 10)
                if crit == 1:
                    damageDealt = damageDealt * 2
                    print("Lucky hit!", player.playerName, "deals", damageDealt, "points of pain to the enemy!")
                    enemy4.enemyHealth = enemy4.enemyHealth - damageDealt
                else:
                    print(player.playerName, "attacks swiftly! They deliver", damageDealt, "damage to the enemy!")
                    enemy4.enemyHealth = enemy4.enemyHealth - damageDealt

            if enemy4.enemyHealth >= 0:
                # enemy attacks here
                damageReceived = random.randint(enemy4.enemyAttack - 2,
                                                enemy4.enemyAttack + 2) - player.playerDefense / 4

                if enemyMiss == 1:
                    print(player.playerName, "cheers as the enemy misses. Lucky turn!")
                else:
                    critE = random.randint(1, 10)
                    if critE == 1:
                        damageReceived = damageReceived * 2
                        print("Unlucky! Enemy deals", damageDealt, "damage to", player.playerName, "!")
                        player.playerHealth = player.playerHealth - damageReceived
                    else:
                        print("Enemy attacks", player.playerName, "and deals", damageReceived, "damage to",
                              player.playerName, "!")
                        player.playerHealth = player.playerHealth - damageReceived

            # now check if enemy or player are dead
            if (enemy4.enemyHealth < maxHealthE / 3) and (enemy4.enemyHealth > 0):
                print("The enemy looks shaken! Deliver the final blow soon!")
            if enemy4.enemyHealth <= 0:
                print(player.playerName, "has defeated the ZARALEGGIAN KING!")
                battleBegin = 0

            if (player.playerHealth < maxHealth / 3) and (player.playerHealth > 0):
                print("Oh no!", player.playerName, "feels themselves weakening. Don't give up,", player.playerName,
                      "!")

            if player.playerHealth <= 0:
                print(player.playerName, "sputters, then collapses. They have been defeated by the enemy.")
                print("GAME OVER")
                battleBegin = 2

        elif playerChoice == "2":
            # dodge has a chance of dealing less damage without being hit, but has a higher chance of fail and being hit
            # not finished
            dodge = random.randint(1, 10)

            if dodge >= 4:
                missHit = random.randint(enemy4.enemyAttack - 2, enemy4.enemyAttack + 2)
                print(player.playerName, "prepares to leap out of the way, but they miscalculate their enemy! "
                                         "The hit lands, dealing", missHit, "damage along the way.")
                player.playerHealth = player.playerHealth - missHit
            else:
                dodgeDamage = random.randint(player.playerAttack - 2,
                                             player.playerAttack + 2) - enemy4.enemyDefense / 2
                print(player.playerName,
                      "readies themself and springs out of the way at the last second. They strike at "
                      "the enemy, and deal", dodgeDamage, "damage.")
                enemy4.enemyHealth = enemy4.enemyHealth - dodgeDamage

            if (enemy4.enemyHealth < maxHealthE / 3) and (enemy4.enemyHealth > 0):
                print("The enemy looks shaken! Deliver the final blow soon!")
            if enemy4.enemyHealth <= 0:
                print(player.playerName, "has defeated the ZARALEGGIAN KING!")
                battleBegin = 0

            if (player.playerHealth < maxHealth / 3) and (player.playerHealth > 0):
                print("Oh no!", player.playerName, "feels themselves weakening. Don't give up,", player.playerName,
                      "!")

            if player.playerHealth <= 0:
                print(player.playerName, "sputters, then collapses. They have been defeated by the enemy.")
                print("GAME OVER")
                battleBegin = 2

        elif playerChoice == "3":
            print(player.playerName, "opens their bag. They find:")

            if inventory:
                for x in range(len(inventory)):
                    print(x + 1, ".", inventory[x].itemName, ": Provides +", inventory[x].statBoost, " health")
                endValue = len(inventory)
                print(endValue + 1, ". Close inventory")
                print("What item will they choose?")

                inventoryChoice = input()
                convert = int(inventoryChoice)

                if convert != endValue + 1:
                    itemConsumed = inventory[convert - 1]
                    player.playerHealth = player.playerHealth + itemConsumed.statBoost
                    if player.playerHealth > 100:
                        player.playerHealth = 100

                    inventory.remove(itemConsumed)
                    print(player.playerName, "consumed the", itemConsumed.itemName,
                          "and smiles. Tastes good! Their health is now",
                          player.playerHealth, "out of 100.")
            else:
                print(player.playerName, "blinks, then tips their bag upside down. Nothing falls out.")

        else:
            print(player.playerName, "grumbles. Give them a real choice, they only have so much time!")

    if battleBegin == 0:
        print_slow(f"{player.playerName} watches as the Zaraleggian king collapses and doesn't get back up.\n")
        print_slow(f"The energy from the battle still courses through {player.playerName}'s bones, but they succeeded. They won.\n")
        print_slow(
            f"Now that the king has been slain, {player.playerName} has all they need to return back to their ship. They lean \n"
            "to grab the missing ship component from the king's body.\n")
        print_slow(
        f"However, {player.playerName}'s eyes are caught by the glimmer of the Zaralegglian crown, and all the power it holds.\n")
        print(f"What will {player.playerName} do?")
        print("1. Return to their home and escape the alien planet")
        print("2. Become the ruler of an alien race")

        endingChoice = input()
        if endingChoice == "1":
            ending_1(player)
        elif endingChoice == "2":
            ending_2(player)

#ending 1
def ending_1(player):
    print_slow(f"{player.playerName} grasps the metal piece, gripping it firm in their hands before leaving.\n")
    print_slow(f"They make a quick exit, evading any vengeful Zaraleggians along the way.\n")
    print_slow(f"But before they leave,{player.playerName} stops to pick up one last cargo before they depart the planet.\n")
    print_slow(f"Surprisingly to {player.playerName}, the old woman does not seem shocked to see them victorious.\n")
    print_slow(f"{player.playerName} sets off with their new partner in search of Planet Earth once more.\n")
    print("YOU'VE DEFEATED THE ZARALEGGIANS AND ACHIEVED FREEDOM! FIN.")

#ending 2
def ending_2(player):
    print_slow(f"{player.playerName} grasps the crown, examining it before placing it atop their head. \n")
    print_slow(f"The headpiece is somewhat heavy, but {player.playerName} knows the value measured by such weight.\n")
    print_slow(f"Zaraleggians, upon learning of the transition of power, quickly accept the new ruler; whether it is\n"
               f"due to reverence or fear is contested.\n")
    print_slow(f"{player.playerName} is no longer the same lonely cowboy they once were; instead, they find purpose in \n"
               f"ruling the Zaraleggians and growing their power within the cosmos.\n")
    print("YOU'VE USURPED THE ZARALEGGIAN THRONE AND BECOME THEIR RULER! FIN.")

#room 1
def room_1(player):

    print(f"{player.playerName} enters room one and spots a large lever on the left.\n")
    lever = input(f"Should {player.playerName} push the lever down?\n"
                  f"1. Yes or 2. No, Enter 1 or 2: ")

    # first if
    if lever == "1":
        print("Upon pushing the lever down, a collection of three weapons descends from the ceiling\n")
        print("The weapon choices are 1.fists, 2.sword, and 3.bow and arrow.\n")
        choice = input(f"Which weapon will they choose?\n"
                       f"Pick 1, 2, or 3: ")

        weaponChosen = True
        while weaponChosen:
            if choice == "1":
                print("""
                (ง ͠° ͟ل͜ ͡°)ง
                               """)
                weaponChosen = False
                print("No attacks added to player attack, you are on your own buddy!")
                print(f"Player attack:{player.playerAttack}\n")
                print(f"{player.playerName} chose their good ole fashion fists as their weapon, aka HARDCORE MODE")
                print(f"{player.playerName} does some quick jabs, and enters the next room feeling slightly confident.")
                boss_fight1(player)

            elif choice == "2":
                print("""        
                       D
                       I
                    ___E___
                      | |
                      | |
                      | |
                      | |
                      | |
                      | |
                      | |
                      \ /           """)
                player.playerAttack = player.playerAttack + 5
                weaponChosen = False
                print("Add +5 to player attack")
                print(f"Player attack:{player.playerAttack}\n")
                print(f"{player.playerName} chose the medieval longsword as their weapon.")
                print(f"{player.playerName} slashes the wind the sword to test it's sharpness "
                    f"then enters the next room feeling confident.")
                boss_fight1(player)

            elif choice == "3":
                print("""  
                >>>>>----------------------->
                       """)
                player.playerAttack = player.playerAttack + 4
                weaponChosen = False
                print("Add +4 to player attack!")
                print(f"Player attack:{player.playerAttack}\n")
                print(f"{player.playerName} is feeling like Katniss Everdeen and chose the bow and arrow as their weapon")
                print(f"{player.playerName} aims with the bow to test it's strength.{player.playerName} then enters \n"
                      f"the next room, feeling confident.")
                boss_fight1(player)

            else:
                print("Not a valid input, silly! Try again: ")

    elif lever == "2":
        print(f"{player.playerName} ponders whether or not they should pull the lever.")
        print(f"{player.playerName} goes near the lever to get a closer look. However, {player.playerName} slips\n"
              f"and pushes on the lever on accident.")
        print(f"{player.playerName}'s surprise a collection of three weapons descends from the ceiling\n")
        print("The weapon choices are 1.fists, 2.sword, and 3.bow and arrow.\n")
        choice = input(f"Which weapon will they choose?\n"
                       f"Pick 1, 2, or 3: ")

        weaponChosen = True
        while weaponChosen:
            if choice == "1":
                print("""
                        (ง ͠° ͟ل͜ ͡°)ง
                                       """)
                weaponChosen = False
                print("No attacks added to player attack, you are on your own buddy!")
                print(f"Player attack:{player.playerAttack}\n")
                print(f"{player.playerName} chose their good ole fashion fists as their weapon, aka HARDCORE MODE")
                print(f"{player.playerName} does some quick jabs, and enters the next room feeling slightly confident.")
                boss_fight1(player)

            elif choice == "2":
                print("""        
                               D
                               I
                            ___E___
                              | |
                              | |
                              | |
                              | |
                              | |
                              | |
                              | |
                              \ /           """)
                player.playerAttack = player.playerAttack + 5
                weaponChosen = False
                print("Add +5 to player attack")
                print(f"Player attack:{player.playerAttack}\n")
                print(f"{player.playerName} chose the medieval longsword as their weapon.")
                print(f"{player.playerName} slashes the wind the sword to test it's sharpness "
                      f"then enters the next room feeling confident.")
                boss_fight1(player)

            elif choice == "3":
                print("""  
                        >>>>>----------------------->
                               """)
                player.playerAttack = player.playerAttack + 4
                weaponChosen = False
                print("Add +4 to player attack!")
                print(f"Player attack:{player.playerAttack}\n")
                print(
                    f"{player.playerName} is feeling like Katniss Everdeen and chose the bow and arrow as their weapon")
                print(f"{player.playerName} aims with the bow to test it's strength.{player.playerName} then enters \n"
                      f"the next room, feeling confident.")
                boss_fight1(player)

            else:
                print("Not a valid input, silly! Try again: ")
#room 2
def room_2(player, inventory):
    print(f"{player.playerName} has entered room two.\n")
    print(f"{player.playerName} sees what appears to be a locked picnic basket sitting on the floor.")

    basket_choice = input(f"Choose to 1. find the key or 2.smash the basket\n"
                          f"Pick 1 or 2: ")

    if basket_choice == "1":
        print(f"{player.playerName} looks around the empty room puzzled.\n")
        print(f"{player.playerName} spots an odd floor vent in the bottom right corner of the room and a bouncy floorboard.")
        find_choice1 = input("Look in the 1.floor vent or the 2. floorboard ")

        if find_choice1 == "1":
            print(f"{player.playerName} peers into the floor vent only to inhale a bunch of dust.\n")
            print(f"{player.playerName} decides to look under the misplaced floorboard instead.")
            print(f"{player.playerName} lifts the floorboard and sees a silver key sitting in the middle.")
            print(f"{player.playerName} puts the key in their inventory.")
            print(f"{player.playerName} unlocks the basket and sees three food items: 1.granola bar, 2.Pizza slice, and 3.Red Apple.")
            foodstats_1 = input(f"Which item will {player.playerName} take? Pick 1, 2, or 3: ")

            if foodstats_1 == "1":
                print("""
                     _____________,-.___     _
                     |____        { {]_]_]   [_]
                     |___ `-----.__\ \_]_]_    . `
                     |   `-----.____} }]_]_]_   ,
                     |_____________/ {_]_]_]_] , `
                               `-'                    """)
                granola_bar = Food(20, "Granola Bar")
                print(f"Heals for:{granola_bar.statBoost} health\n")
                inventory.append(granola_bar)
                print(f"{player.playerName} then moves on to the next room")
                room_3(player, inventory)
            elif foodstats_1 == "2":
                print("""
                // ""--.._
                ||  (_)  _ "-._
                ||    _ (_)    '-.
                ||   (_)   __..-'
                 \\__..--""
                                 """)

                pizza = Food(30, "Pizza")
                print(f"Heals for:{pizza.statBoost} health\n")
                inventory.append(pizza)
                print(f"{player.playerName} then moves on to the next room")
                room_3(player, inventory)
            elif foodstats_1 == "3":
                print("""
                  ,--./,-.
                 / #      \
                |          |
                 \        /    
                  `._,._,'    """)
                apple = Food(15, "Red apple")
                print(f"Heals for:{apple.statBoost} health\n")
                inventory.append(apple)
                print(f"{player.playerName} then moves on to the next room")
                room_3(player, inventory)
            else:
                print("Invalid choice. Pick 1.granola bar, 2.red apple, or 3.pizza slice.")

        elif find_choice1 == "2":
            print(f"{player.playerName} lifts the floorboard and sees a silver key sitting in the middle.\n")
            print(f"{player.playerName} puts the key in their inventory.")
            print(f"{player.playerName} unlocks the basket and sees three food items: 1.granola bar, 2.Pizza slice, and 3.Red Apple.")
            foodstats_1 = input(f"Which item will {player.playerName} take? Pick 1, 2, or 3: ")
            if foodstats_1 == "1":
                print("""
                     _____________,-.___     _
                     |____        { {]_]_]   [_]
                     |___ `-----.__\ \_]_]_    . `
                     |   `-----.____} }]_]_]_   ,
                     |_____________/ {_]_]_]_] , `
                               `-'                    """)
                granola_bar = Food(20, "Granola Bar")
                print(f"Heals for:{granola_bar.statBoost} health\n")
                inventory.append(granola_bar)
                print(f"{player.playerName} then moves on to the next room")
                room_3(player,inventory)
            elif foodstats_1 == "2":
                print("""
                // ""--.._
                ||  (_)  _ "-._
                ||    _ (_)    '-.
                ||   (_)   __..-'
                 \\__..--""
                                              """)
                pizza = Food(30, "Pizza")
                print(f"Heals for:{pizza.statBoost} health\n")
                inventory.append(pizza)
                print(f"{player.playerName} then moves on to the next room")
                room_3(player, inventory)
            elif foodstats_1 == "3":
                print("""
                  ,--./,-.
                 / #      \
                |          |
                 \        /    
                  `._,._,'    """)
                apple = Food(15, "Red Apple")
                print(f"Heals for:{apple.statBoost} health\n")
                inventory.append(apple)
                print(f"{player.playerName} then moves on to the next room")
                room_3(player, inventory)
            else:
                print("Invalid choice. Pick 1.granola bar, 2.Pizza slice, and 3.Red Apple.")

    elif basket_choice == "2":
        print(f"{player.playerName} punched the basket, but couldn't put a dent in it\n")
        print(f"{player.playerName} angrily chooses to find the key.")
        print(f"{player.playerName} looks around the empty room puzzled.")
        print(f"{player.playerName} spots an odd air vent in the bottom right corner of the room and a bouncy floorboard.\n")
        find_choice1 = input("Choose to look in 1.floor vent or under the 2.floorboard \n")

        if find_choice1 == "1":
            print(f"{player.playerName} peers into the floor vent only to inhale a bunch of dust.\n")
            print(f"{player.playerName} decides to look under the misplaced floorboard instead.")
            print(f"{player.playerName} lifts the floorboard and sees a silver key sitting in the middle.")
            print(f"{player.playerName} puts the key in their inventory")
            print(f"{player.playerName} unlocks the basket and sees three food items: 1.granola bar, 2.Pizza slice, and 3.Red Apple.\n")
            foodstats_1 = input(f"Which item will {player.playerName} take? Pick 1, 2, or 3: ")

            if foodstats_1 == "1":
                print("""
                     _____________,-.___     _
                     |____        { {]_]_]   [_]
                     |___ `-----.__\ \_]_]_    . `
                     |   `-----.____} }]_]_]_   ,
                     |_____________/ {_]_]_]_] , `
                               `-'                    """)
                granola_bar = Food(20, "Granola Bar")
                print(f"Heals for:{granola_bar.statBoost} health\n")
                inventory.append(granola_bar)
                print(f"{player.playerName} then moves on to the next room")
                room_3(player, inventory)
            elif foodstats_1 == "2":
                print("""
                // ""--.._
                ||  (_)  _ "-._
                ||    _ (_)    '-.
                ||   (_)   __..-'
                 \\__..--""
                                              """)
                pizza = Food(30, "Pizza")
                print(f"Heals for:{pizza.statBoost} health\n")
                inventory.append(pizza)
                print(f"{player.playerName} then moves on to the next room")
                room_3(player, inventory)
            elif foodstats_1 == "3":
                print("""
                  ,--./,-.
                 / #      \
                |          |
                 \        /    
                  `._,._,'    """)
                apple = Food(15, "Red apple")
                print(f"Heals for:{apple.statBoost} health\n")
                inventory.append(apple)
                print(f"{player.playerName} then moves on to the next room")
                room_3(player, inventory)
            else:
                print("Invalid choice. Pick 1.granola bar, 2.Pizza slice, and 3.Red Apple.")

        elif find_choice1 == "2":
            print(f"{player.playerName} lifts the floorboard and sees a silver key sitting in the middle.")
            print(f"{player.playerName} puts the key in their inventory.")
            print(f"{player.playerName} unlocks the basket and sees three food items: 1.granola bar, 2.Pizza slice, and 3.Red Apple.\n")
            foodstats_1 = input(f"Which item will {player.playerName} eat? Pick 1, 2, or 3:")

            if foodstats_1 == "1":
                print("""
                     _____________,-.___     _
                     |____        { {]_]_]   [_]
                     |___ `-----.__\ \_]_]_    . `
                     |   `-----.____} }]_]_]_   ,
                     |_____________/ {_]_]_]_] , `
                               `-'                    """)
                granola_bar = Food(20, "Granola Bar")
                print(f"Heals for:{granola_bar.statBoost} health\n")
                inventory.append(granola_bar)
                print(f"{player.playerName} then moves on to the next room")
                room_3(player, inventory)
            elif foodstats_1 == "2":
                print("""
                // ""--.._
                ||  (_)  _ "-._
                ||    _ (_)    '-.
                ||   (_)   __..-'
                 \\__..--""
                                              """)
                pizza = Food(30, "Pizza")
                print(f"Heals for:{pizza.statBoost} health\n")
                inventory.append(pizza)
                print(f"{player.playerName} then moves on to the next room")
                room_3(player, inventory)
            elif foodstats_1 == "3":
                print("""
                  ,--./,-.
                 / #      \
                |          |
                 \        /    
                  `._,._,'    """)
                apple = Food(15, "Red apple")
                print(f"Heals for:{apple.statBoost} health\n")
                inventory.append(apple)
                print(f"{player.playerName} then moves on to the next room")
                room_3(player, inventory)
            else:
                print("Invalid choice. Pick 1.granola bar, 2.Pizza slice, and 3.Red Apple.")
#room 3
def room_3(player, inventory):

    print(f"{player.playerName} enters room three\n")
    player_choice = input(f"Would {player.playerName} like to observe the room?"
                          f"1. Yes or 2.No\n"
                          f"Pick 1 or 2: ")

    if player_choice == "1":
        print(f"Player looks around the room, it is unlike all the other rooms he have been to. The room is filled with various books\n"
              f"of different languages. And on top of the pile of books sits a bunny\n")
        print("""
                /|      __
               / |   ,-~ /
              Y :|  //  /
              | jj /( .^
              >-"~"-v"
             /       Y
            jo  o    |
           ( ~T~     j
            >._-' _./
           /   "~"  |
          Y     _,  |
         /| ;-"~ _  l
        / l/ ,-"~    \
        \//\/      .- \
         Y        /    Y    
         l       I     !
         ]\      _\    /"\
        (" ~----( ~   Y.  )
                                     """)
        print_slow("Bunny: Would you look at that? A human appeared!. The last human I saw was millions of years ago.\n")
        print("The player stares with wide eyes.")
        print("Choose player input:\n"
              "1. How can the bunny talk??!?\n"
              "2. Hello nice to meet you Mr. Bunny")
        player_choice = input()

        if player_choice == "1":
            print("Bunny: How rude of you! I am not just any bunny, I am SIR BUNNY THE DISTINGUISHED. I have served\n"
                  "in the great galaxy war thrice and have survived thrice, my grandfather has served in.....\n"
                  "The player decides to leave the room")
            boss_fight2(player, inventory)
        elif player_choice == "2":
            print(f"Bunny: Howdy human! I wonder how you ended up in this corner of the galaxy. It is quite far away from\n"
                  f"your home. Here take these clothes, you can't be walking around naked like that\n "
                  f"But shoo now, I have to continue munching on these books.")
            print(f"{player.playerName} receives clothes and heads on to the next room")
            boss_fight2(player, inventory)
        else:
            print("Please select the correct choice")

    else:
        print(f"{player.playerName} stands at the doorway, and someone calls out to him")
        print(f"{player.playerName} turns towards the voice and sees a bunny talking.")
        print("""
                        /|      __
                       / |   ,-~ /
                      Y :|  //  /
                      | jj /( .^
                      >-"~"-v"
                     /       Y
                    jo  o    |
                   ( ~T~     j
                    >._-' _./
                   /   "~"  |
                  Y     _,  |
                 /| ;-"~ _  l
                / l/ ,-"~    \
                \//\/      .- \
                 Y        /    Y    
                 l       I     !
                 ]\      _\    /"\
                (" ~----( ~   Y.  )
                                             """)
        print(f"A bunny talking??!??, {player.playerName} rushes towards the next room,"
              f"questioning his own sanity.")
        boss_fight2(player, inventory)
#room 4
def room_4(player, inventory):
    print(f"{player.playerName} hesistanly enters room four.\n")
    print(f"The room is pitch black.")

    player.playerHealth = player.playerHealth + 70
    if player.playerHealth > 100:
        player.playerHealth = 100

    light_choice = input("Search for light switch: 1.Yes or 2.No")
    if light_choice == "1":
        print(f"{player.playerName} searches the wall for a light switch, but accidentally pushes a button.\n")
        print(f"Pop! The lights turns on and a table with what looks to be food ascends from the ground.")
        print(f"A letter is propped up on the table with {player.playerName}'s name")
        letter_choice = input("Read the letter: 1.Yes or 2.No")
        if letter_choice == "1":
            print_slow(f"Dear {player.playerName},\n")
            print_slow("Welcome to my world.\n")
            print_siw(f"Since you've made it this far, I thought I'd treat you with my favorite dish.\n")
            print_slow(f"I'm not sure how food affects humans, but I wouldn't want you to leave without exploring my culture.\n")
            print_slow("Enjoy and see you soon,\n")
            print_slow("You'll know me when you see me\n")
            print()
            alien_food = input("Eat the alien food: 1.Yes or 2.No\n")
            if alien_food == "1":
                print(f"{player.playerName} eats the food and is disappointed by its paper like taste.")
                print(f"\"Bleh!\"")
                print(f"{player.playerName} leaves room 4.")
                room_5(player, inventory)
            elif alien_food == "2":
                print(f"{player.playerName} doesn't have time for this shenanigans.")
                print(f"{player.playerName} leaves room 4.")
                room_5(player, inventory)

        elif letter_choice == "2":
            print(f"{player.playerName} doesn't have time for this shenanigans.\n")
            print(f"{player.playerName} leaves room 4.")
            room_5(player, inventory)
    elif light_choice == "2":
        print(f"{player.playerName} stumbles through the darkness, stubbing their toes a few times.")
        print(f"Eventually, {player} finds a door handle.")
        print(f"{player.playerName} leaves room 4.\n")
        room_5(player, inventory)
#room 5
def room_5(player, inventory):
    print(f"{player.playerName} walks into the room , and is met with a sudden and bitter cold. They shudder, deciding they\n"
        "will spend as little time in this room as possible.")
    print(f"Where will {player.playerName} go?")
    print("1. Left")
    print("2. Right")
    room6Input = input("Enter 1 or 2: ")

    if room6Input == "1":
        print(f"{player.playerName} decides on left. They find a mirror, one with a height that easily spans 3 feet above"
              "their head.")
        print(f"{player.playerName} notices their dishevelled appearance, and quickly brushes the dirt off their face and body.\n"
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
        print(f"On the mirror {player.playerName} notices a photo of two Zaraleggians. Attached to the photo is a small\n"
              "candy.")
        print("Take the candy?")
        print("1. Yes")
        print("2. No")

        candyChoice = input("Enter 1 or 2")
        if candyChoice == "1":
            print(f"{player.playerName} peels the candy off the photo. It's lemon flavored. They add it to their bag.\n")
            candy = Food(20, "LemonCandy")
            inventory.append(candy)
        elif candyChoice == "2":
            print(f"{player.playerName} leaves the candy. They'd rather not get cavities today.")


    elif room6Input == "2":
        print(f"{player.playerName} strides to the right, in the direction of a table. On it rests a slip of paper.\n")
        print("The paper reads, in messy Zaraleggian: ")
        print_slow(" 'REMEMBER TO PAY HEATING BILLS' \n")
        print("A box also rests on the desk. Grab it?")
        print("1. Yes")
        print("2. No")

        boxChoice = input("Enter 1 or 2")
        if boxChoice == "1":
            print(f"{player.playerName} grabs the box and examines it. It appears to be sealed by a lock, with a "
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
            print("Text above the seal reads: How many letters are in the name of the friendly resident of the fourth room?\n")
            boxCode = input("Enter the answer: ")

            if boxCode == "5":
                print("Aha! The lid pops open. Inside is a packet of ramen! Take it? Y or N\n")
                ramenChoice = input("Enter Y or N: ")
                if ramenChoice == "Y" or "y":
                    print(player.playerName, " takes the ramen.")
                    ramen = Food(60, "RamenNoodles")
                    inventory.append(ramen)
                elif ramenChoice == "N" or "n":
                    print(player.playerName,
                          "chooses not to take the ramen. It looks like someone else treasures it, anyways.")
            else:
                print(f"{player.playerName} enters the code, but the lock doesn't seem to budge. As they struggle with the\n"
                      "box, a rodent leaps into their bag!\n")
                if inventory:
                    print(f"It is too late by the time the rodent takes off with {player.playerName} food. Lost the\n"
                          "last item added to bag.")
                    lastItem = len(inventory)
                    inventory.remove(inventory[lastItem - 1])

                else:
                    print("The rodent squirms around, before eventually jumping out and running away. How odd.\n")
        elif boxChoice == "2":
            print(player.playerName, "would rather not think about puzzles now. They leave the box.")

    print(f"{player.playerName} scans the room once more. If they're being honest, it is quite barren, aside from"
            "one very long and large bed.")
    print(f"{player.playerName} would rather not search a bed for items of use.")
    print("The cold begins to become more bothersome.")
    print(player.playerName, "moves on to the next room.")
    boss_fight3(player, inventory)

def room_6(player, inventory):
        print(f"{player.playerName} drags themselves into the next room, still coming down from the adrenaline of the last battle.\n")
        print("They can still feel the sweat on their brow, but they can only be thankful for their skill and a bit of luck"
            "that they've made it this far.")
        print(f"{player.playerName} closes their eyes and rests for a bit.\n")
        player.playerHealth = 100
        print(f"{player.playerName}'s health has been restored!")
        print(f"However {player.playerName}'s adventure is not over yet.\n")

        playerSleeping = 1
        while playerSleeping == 1:
            print(f"Wake {player.playerName} up?")
            print("1. Yes")
            print("2. No")

            wakeChoice = input("Enter 1 or 2: ")
            if wakeChoice == "1":
                print(f"{player.playerName} yawns, and moves with a newfound energy.")
                playerSleeping = 0
            if wakeChoice == "2":
                print(player.playerName, "decides to nap for just a while longer.")
                print("Don't be lazy,", player.playerName, "!")

        print(player.playerName,
              "looks around, scanning for items. They spot an old woman, hunched over a fire in the corner.")
        print("""
                ( ( (                    ))
                  ) ) )                 ((
                    ( ( (           ___o___)
                   '. ___ .'        |     |====O
                  '  (> <) '        |_____|
                --ooO-(_)-Ooo--------------------

        """)
        print("Should", player.playerName, "approach her?")
        print("1. Yes")
        print("2. No")
        approachChoice = input()
        if approachChoice == "2":
            print(player.playerName,
                  "recalls the shapeshifting nature of the Zaraleggian race, and decides against approaching her.")
            print("But....")
            print(player.playerName,
                  "feels their stomach grumble. The aroma of her cooking reminds them of home, and they drift towards"
                  "the old woman anyways.")
        print(player.playerName, "approaches the old woman warily, seating themselves across her. She doesn't seem to"
                                 "acknowledge them.")
        print_slow("After a beat, she stops stirring her pot and speaks.\n")
        print_slow("Old Woman: Many a traveler have set foot exactly where you have gone.\n")
        print_slow("Old Woman: And every single one of them never achieve the ending they seek.\n")
        print_slow("Old Woman: Perhaps if I were younger, I'd have done the same. But these bones would've never survived.\n")
        print_slow(
            "Old Woman: Your battles may have been tough so far, but they will be nothing like what is behind that door.\n")
        print_slow("Old Woman: It may not be much, but I can offer you this.\n")
        print_slow("The old woman hands", player.playerName, "a wooden bowl of soup.\n")
        print_slow("Old Woman: Use it well. And hope that our paths never cross again.\n")
        print("The old woman turns her attention back to her pot. She doesn't seem to have anything else to say.\n")
        print(player.playerName, "saves the soup for later.")
        print("'Grandma's Soup' added to Bag!")
        soup = Food(100, "Grandma's Soup")
        inventory.append(soup)

        print(player.playerName,
              "stands up and looks around. In front of them towers an intimidating door. Perhaps there is still"
              "something to discover before passing through.")
        print("What will", player.playerName, "do?")
        print("1. Enter through the door")
        print("2. Explore further")
        finalChoice = input()
        if finalChoice == "2":
            print(player.playerName, "moves around the corners of the room.")
            print(player.playerName, "finds a bag of Airplane Peanuts!")
            peanuts = Food(20, "AirplanePeanuts")
            inventory.append(peanuts)
            print(player.playerName, "finds a Twinkie on the ground!")
            twinkie = Food(15, "Twinkie")
            inventory.append(twinkie)
            print("The items have been added to Bag.")

        print(player.playerName, "knows they cannot delay the inevitable any longer.")
        print(player.playerName, "feels the anxiety weighing on them.")
        print(player.playerName, "knows this will be the hardest thing they've faced yet.")
        print(player.playerName, "opens the door and enters the Throne Room.")
        final_boss(player, inventory)


#main game
def main():
    prologue()
    print()


    inputName = input("What would be the player name?")
    player = Player(inputName, 100, 10, 10)
    print(f"Player name:{player.playerName}\nPlayer health:{player.playerHealth}\n"
          f"Player Attack:{player.playerAttack}\nPlayer defense:{player.playerDefense}\n")
    print(f"The jail cell door lay ajar,{player.playerName} walks out the jail cell door\n")
    #choices
    print(f"{player.playerName} is faced with choices \n"
        "1. Go to next room\n"
        "2. Observe the room\n")

    player_choice = input(f"What will {player.playerName} do? pick 1 or 2: ")

    if player_choice == "1":
        room_1(player)
    elif player_choice == "2":
        print(f"{player.playerName} observes the room. To {player.playerName}'s left is a small window, through which a slither of\n"
             f"moonlight shines. To {player.playerName}'s left is a toilet and sink, which looks very similar to earthly bathrooms,\n"
             f"makes {player.playerName} miss his home. In the corner,to the right, lays a pile of corpses. The smell coming from\n"
             f"the corpses makes {player.playerName} want to get out of here faster.\n")
        player_choice= input(f"Will {player.playerName} go to next room?\n"
                             f"1. Yes or 2. No\n"
                             f"Pick 1 or 2: ")
        if player_choice == "1":
            room_1(player)
        elif player_choice == "2":
            print(f"{player.playerName} holds their nose as the stench of dead bodies fills the room.")
            player_choice = input("Press 1 to go to next room: ")
            if player_choice == "1":
                room_1(player)


    else:
        print("Please enter a valid selection")


main()
























 
















