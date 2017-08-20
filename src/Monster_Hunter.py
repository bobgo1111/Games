# Created on 1/22/17.

import random

monsterList = ["Vaporscream","Stoneghoul","Tombbug","Mistspawn","Agitated Horror","Arid Beast","Stormcloud Venom Hawk","Iron-Scaled Predator Phoenix","Grim Berserker Rhino","Giant Bone Tiger","Spectralwraith","Spitepaw","Ebon Flame Sheep","Brineclaw"] # Gives a list of monster names that random.randint will later choose from

def deathStatement(): # If you die, a variable named "death" will become True, and at the end of the turn loop, if "death" == True, it will print the death statement through this function
    print("You died\nYour level was: " + str(lvlCounter) + "\nYour lore level was " + str(loreLevel) + "\nYour overall score was " + str(overallXPCounter) + ".")

def buyOrNot(varNameOfItem, nameOfItem, attackBonus, defenseBonus, xpGainBonus, cost): # Each turn the player can choose to buy stuff from the shop
    if varNameOfItem == True: # If the player has already bought the item, then the function will return None, so the player will not have to remember everything they bought or not
        return None
    else: # If the player has not bought it, if does this
        global playersGold
        print("You have " + str(playersGold) + " Gold.") # Tells the player how much gold they have, so they know if they can buy an item or not
        wantToBuy = input("Would you like to buy the " + nameOfItem + "? It will grant you:\nAttack: " + attackBonus + "\nDefense: " + defenseBonus + "\nWill increase your XP gain by: " + xpGainBonus + "\n\nThis item costs " + str(cost) + " gold." + "\n\n(to answer, just say \"yes\". If you do not wish to buy this item, you may say anything else)\n(to exit, simply enter \"exit\")\n") # asks the player if they want to buy the item and tells them what the item does. Saves player's answer to variable "wantToBuy"
        if wantToBuy == "yes": # If the player wants to buy, it goes into this
            if playersGold < cost: # If the player doesn't have enough gold, this will not allow them to buy the item
                print("You do not have enough gold to buy this item!")
                return False # Returns that the player did not buy the item
            print("Congratulations! You are now equipped with the " + nameOfItem + "!") # If the player does have enough money, this tells them that they successfully purchased the item
            playersGold -= cost # Takes away the amount of gold that the item was bought for
            return True # Returns that the player did indeed buy the item
        elif wantToBuy == "exit": # If the player doesn't wish to view the entire shopping catalogue, they can type "exit" and the function will return that the player wants to exit
            return "exit"
        else:
            return False # If the player types anything other than "yes" or "exit", the function will assume the player did not want to buy the item and will return so

def wandering(): # Each turn, the player has an option to wander. Also, the player is forced to wander after 8 non wandering turns
    global playersFood, playersGold, xpCounter, overallXPCounter, death, playersLore, loreLevel
    playersFood -= 1 # Wandering costs one food
    playersLore += 1 # Wandering increases the player's lore by one
    if playersLore == 10: # Every 10 lore earned makes the player level up in lore
        loreLevel += 1
        print("You got to a new level of lore! Your lore level is now " + str(loreLevel) + "!")
    overallXPCounter += 100 # Player gains 100 to their overall score from learning lore
    xpCounter -= lvlCounter * 150 # Takes away xp from player to counter player wandering instead of fleeing a monster to avoid losing xp

    dirToWander = random.randint(1, 4) # Makes a random direction to wander
    directions = ["North", "South", "East", "West"]
    distToWander = random.randint(5, 30) # Makes a random distance to wander
    getFromWandering = random.randint(1, 30) # Random integer that will determine what the player gets from wandering
    whereYouGo = random.randint(0, 9) # Makes a random biome to end up in
    biomes = ["Ice Spike Plains", "Arid Desert", "Lush Jungle", "Spooky Forest", "Dark Cave", "Meadows of Valinor", "Low Grasslands", "Lush Riverlands", "Chasms of Doom", "Cliffs of Malibar"] # All the biomes
    print("You have chosen to wander " + str(directions[dirToWander - 1]) + " for " + str(distToWander) + " miles. You have arived at the " + biomes[whereYouGo] + ". During your wanderings, you used up 1 food. You now have " + str(playersFood) + " food.") # Tells the player where they went

    if getFromWandering in range(1, 3): # 2/30 chance player finds two food during their wanderings
        playersFood += 2
        print("You found 2 food! You now have " + str(playersFood) + " food!")
    elif getFromWandering in range(3, 9): # 6/30 chance player finds one food
        playersFood += 1
        print("You found 1 food! You now have " + str(playersFood) + " food!")
    elif getFromWandering in range(9, 15): # 6/30 chance player finds one gold
        playersGold += 1
        print("You found 1 gold! You now have " + str(playersGold) + " gold!")
    elif getFromWandering in range(15, 18): # 3/30 chance player finds 10 gold
        playersGold += 10
        print("You found 10 gold! You now have " + str(playersGold) + " gold!")
    elif getFromWandering in range(18, 20): # 2/30 chance player finds 100 XP
        xpCounter += 100
        overallXPCounter += 100
        print("You found 100 XP! You now have " + str(xpCounter) + " XP!")
    else: # 10/30 chance player finds nothing

        print("You found nothing. Better luck next time!")
    print("From your wanderings, you have learned 1 lore. You now have " + str(playersLore) + " Lore.") # Tells player how much lore they have
    attackBonus = random.randint(-2, 3) # calculates the biome's attack bonus
    defenseBonus = random.randint(-4, 6) # calculates the biome's defense bonus
    if attackBonus > 0:
        print("In this new biome, you will gain " + str(attackBonus) + " bonus attack.")
    else:
        print("In this new biome, you will lose " + str(attackBonus) + " attack power.")
    if defenseBonus > 0:
        print("In this new biome, you will gain " + str(defenseBonus) + " bonus defense.")
    else:
        print("In this new biome, you will lose " + str(defenseBonus) + " defense power.")
    death = False # Death is false after wandering.

while True: # Begins all gameplay
    wannaPlay = input("\nWould you like to play a game of Monster Hunter?\n") # Asks if they want to play a game. If they say yes, they play the game, if they say no, the program ends. If they play the game and die, it will loop back here and ask if they want to play a game again
    while wannaPlay not in ["yes", "no"]: # Makes sure the player says "yes" or "no"
        print("You did not say \"yes\" or \"no\"\n")
        wannaPlay = input("\nWould you like to play a game of Monster Hunter?\n")

    if wannaPlay == "yes": # Sets all the variables before the game
        lvlCounter = 0
        xpCounter = 0
        overallXPCounter = 0
        playersGold = 0
        playersFood = 5
        attackBonus = 0
        defenseBonus = 0
        wanderCounter = 0
        playersLore = 0
        loreLevel = 0

        scarySword = False # Starts player with no swords
        scaryUltraSword = False
        scaryUltraSuperSword = False
        scaryUltraSuperRareSword = False
        scaryUltraSuperRareQuantumSword = False
        scaryUltraSuperRareQuantumImmortalSword = False
        scaryUltraSuperRareQuantumImmortalDeathlySword = False
        scaryUltraSuperRareQuantumImmortalDeathlySwordOfDoom = False

        scaryArmour = False # Starts player with no armour
        scaryUltraArmour = False
        scaryUltraSuperArmour = False
        scaryUltraSuperRareArmour = False
        scaryUltraSuperRareQuantumArmour = False
        scaryUltraSuperRareQuantumImmortalArmour = False
        scaryUltraSuperRareQuantumDeathlyArmour = False
        scaryUltraSuperRareQuantumImmortalDeathlyArmourOfDoom = False

        print("""You are on a great journey through miles of unknown, dangerous territory to discover new lands.
On you journey, you will meet many monsters.
Some you can kill, some you might not, so choose wisely who you will fight.
If you choose to fight, know this. Having armour and a weapon will increase the chance of your winning.
You can buy armour and weapons from the store. If at any time you wish to access the store, when you meet a monster, instead of attacking of fleeing, simply type \"shop\"
Visiting the shop also costs xp (more xp than is lost from fleeing monsters)
Also, if you succeed in killing a monster that is a higher level than yourself, your xp gain will triple
If you choose to flee, you will lose some XP
If you do not wish to flee or fight, you have an option to travel. Traveling, or Wandering, costs 1 food and some XP. You begin with 5 food, and you can find more food by wandering.
However, food is rare, so use it wisely and sparingly to make sure that you do not starve.
When you wander, you will learn \"lore\". Lore will automatically be used to help you learn new skills. You can also find XP by wandering.
Another thing that can be helpful about wandering is that certain biomes will give you an attack and HP bonus. However, sometimes the biome may take away attack and HP.
If you stay in a biome too long, you may eridicate all the monsters there, there will be nothing left to slay, and you will be forced to move to new territory.
In the beginning, it will be very easy and you will receive bonuses, but it will become harder as you level up.

Good Luck!\n\n""") # Prints the game instructions/intro

        while True: # Each individual game has turns that begin here and that loop back here after each turn is done.
            wanderCounter += 1
            if wanderCounter > 8: # Makes sure the player cannot stay in one place forever
                print("You have stayed in this area too long. There are no more monsters to kill. You must move to a new area. If you do not have enough food to make the journey, then you die.")
                if playersFood == 0:
                    print("You starved to death.")
                    death = True # If the player has no food but is forced to make the journey, then they die
                else:
                    wanderCounter = 0
                    print("You had enough food. You have journeyed to a new place.")
                    wandering() # The player has enough food then they successfully wander
            else:
                monsterNameNum = random.randint(0, 13) # Random number that sets the monsters random name
                monsterLvlNum = random.randint(-5, 4) # Sets the monster's random level that is close to the player's
                monsterLvl = lvlCounter + monsterLvlNum # Sets the monster's random level that is close to player's
                requiredXP = lvlCounter * 500 + lvlCounter * lvlCounter * lvlCounter # Sets the amount of XP required for the player for the player to get to the next level
                monsterXPRan = random.randint(-100, 200) # Sets a random number that somewhat depends on the monster's level for how much XP the monster will give if killed
                monsterXP = monsterLvl * 200 + monsterXPRan # Sets how much XP the monster will give if killed
                monsterHPRan = random.randint(-10, 10) # Sets a random number that depends somewhat on the monster's level for how much HP the monster will have
                monsterAttackRan = random.randint(-10, 10) # Sets a random number that depends somewhat on the monster's level for how much attack the monster will have
                playerHPRan = random.randint(-10, 10) # Sets a random number that depends somewhat on the player's level for how much HP the player will have
                playerAttackRan = random.randint(-10, 15) # Sets a random number that depends somewhat on the player's level for how much attack the player will have

                monsterHP = monsterLvl * (5 + (lvlCounter / 10)) + monsterHPRan # Sets how much HP the monster has
                monsterAttack = monsterLvl * (2 + (lvlCounter / 10)) + monsterHPRan # Sets how much attack the monster has
                playerHP = lvlCounter * 5 + playerHPRan + (3 * loreLevel) # Sets how much HP the player will have
                playerAttack = lvlCounter * 2 + playerAttackRan + (5 * loreLevel) # Sets how much attack the player will have

                if monsterXP < 0: # If the monster's XP is negative, it makes it positive for the player
                    monsterXP -= monsterXP * 2
                if scarySword == True: # If a sword is owned, the player's attack is increased
                    playerAttack += 5
                if scaryUltraSword == True:
                    playerAttack += 5
                if scaryUltraSuperSword == True:
                    playerAttack += 10
                if scaryUltraSuperRareSword == True:
                    playerAttack += 10
                if scaryUltraSuperRareQuantumSword == True:
                    playerAttack += 10
                if scaryUltraSuperRareQuantumImmortalSword == True:
                    playerAttack += 10
                    monsterXP += 500
                if scaryUltraSuperRareQuantumImmortalDeathlySword == True:
                    playerAttack += 10
                    monsterXP += 500
                if scaryUltraSuperRareQuantumImmortalDeathlySwordOfDoom == True:
                    playerAttack += 40
                    monsterXP += 1500

                if scaryArmour == True: # If armour is owned, the player's HP is increased
                    playerHP += 5
                if scaryUltraArmour == True:
                    playerHP += 5
                if scaryUltraSuperArmour == True:
                    playerHP += 10
                if scaryUltraSuperRareArmour == True:
                    playerHP += 10
                if scaryUltraSuperRareQuantumArmour == True:
                    playerHP += 10
                if scaryUltraSuperRareQuantumImmortalArmour == True:
                    playerHP += 10
                    monsterXP += 500
                if scaryUltraSuperRareQuantumDeathlyArmour == True:
                    playerHP += 10
                    monsterXP += 500
                if scaryUltraSuperRareQuantumImmortalDeathlyArmourOfDoom == True:
                    playerHP += 40
                    monsterXP += 1500

                playerAttack += attackBonus # Gives the player the attack bonus from the biome
                playerHP += defenseBonus # Gives the player the HP bonus from the biome

                fightOrFlee = input("A wild " + monsterList[monsterNameNum] + " of level " + str(monsterLvl) + " has appeared. Will you fight, flee, shop, or wander?\n") # Tells the player their options when they meet a monster
                while True:
                    if fightOrFlee not in ["fight", "flee", "shop", "wander", "gold", "food", "XP"]: # Makes sure player says one of the options
                        fightOrFlee = input("You did not say \"fight\", \"flee\", \"shop\", or \"wander\". You must say \"fight\", \"flee\", \"shop\", or \"wander\".\n")
                    else:
                        break

                if fightOrFlee == "gold": # Hax
                    howMuch = input("How much?")
                    playersGold += int(howMuch)
                    death = False
                if fightOrFlee == "food": # Hax
                    howMuch = input("How much?")
                    playersFood += int(howMuch)
                    death = False
                if fightOrFlee == "xp": # Hax
                    howMuch = input("How much?")
                    xpCounter += int(howMuch)
                    death = False

                if fightOrFlee == "fight": # If the player chooses to fight, then this happens
                    print("You have chosen to fight.")

                    if playerAttack <= 0:
                        playerAttack = 6 # Makes sure the player has some attack if their attack is negative

                    while True: # Player and monster fight
                        monsterHP = monsterHP - playerAttack # Takes away the player's attack from the monster's HP

                        if monsterHP <= 0: # If the monster is dead
                            if monsterLvl < 0:
                                monsterLvl = -monsterLvl # Makes sure the player still gets gold from negative level monsters
                            print("You killed the monster!")
                            playersGold += monsterLvl # Gives the player their gold
                            if monsterLvl == 0: # Makes sure the player gets gold from a level 0 monster
                                playersGold += 1
                            death = False # If the player kills the monster, the player does not die
                            if monsterLvl > lvlCounter: # If the player kills a monster that was a higher level than them, their XP gain triples
                                print("Because you killed a monster that was a higher level than yourself, your XP gain tripled!")
                                monsterXP *= 3
                            xpCounter += monsterXP # Player gains XP from killing monster
                            overallXPCounter += monsterXP # Player's overall score increases
                            if monsterLvl == 0: # Tells player they killed the monster
                                print("You have gained " + str(monsterXP) + "XP\nYou now have " + str(xpCounter) + " XP!\nYou have gained 1 Gold!\nYou now have " + str(playersGold) + " Gold!")
                            else:
                                print("You have gained " + str(monsterXP) + "XP\nYou now have " + str(xpCounter) + " XP!\nYou have gained " + str(monsterLvl) + " Gold!\nYou now have " + str(playersGold) + " Gold!")
                            if xpCounter >= requiredXP: # If the player's XP counter is as big as the required XP to get to the next level, the player advances to the next level
                                xpCounter = 0
                                lvlCounter += 1
                                print("You have gotten to a new level! You are now on level " + str(lvlCounter) + "!")
                                doYouGetFood = random.randint(1, 7) # There is a one in 7 chance that upon killing a monster, the player finds one food
                                if doYouGetFood == 1:
                                    playersFood += 1
                                    print("You found 1 food! You now have " + str(playersFood) + " food!")
                            break

                        playerHP = playerHP - monsterAttack # If the monster is not dead, the the monster's attack is subtracted from the player's HP

                        if playerHP < 0: # If the player's HP is less than 0, they die
                            death = True # Sets death as True
                            break

                elif fightOrFlee == "flee": # If the player chooses to flee instead of fight, they lose some XP, but live
                    xpCounter -= lvlCounter * 100
                    print("You have fled. you lost " + str(-(lvlCounter * 100)) + " XP\nYou now have " + str(xpCounter) + " XP.")
                    death = False # If the player flees, they live

                elif fightOrFlee == "shop": # The player could also ask to shop
                    xpCounter -= lvlCounter * 150 # Shopping costs XP
                    print("You lost " + str(lvlCounter * 150) + " XP")
                    while True: # Shows the player the entire shopping catalogue. Player may exit at any time
                        buy = buyOrNot(scarySword, "Scary Sword", "5", "0", "0", 20)
                        if buy == True:
                            scarySword = True
                        elif buy == "exit":
                            break
                        buy = buyOrNot(scaryUltraSword, "Scary Ultra Sword", "10", "0", "0", 30)
                        if buy == True:
                            scaryUltraSword = True
                        elif buy == "exit":
                            break
                        buy = buyOrNot(scaryUltraSuperSword, "Scary Ultra Super Sword", "20", "0", "0", 40)
                        if buy == True:
                            scaryUltraSuperSword = True
                        elif buy == "exit":
                            break
                        buy = buyOrNot(scaryUltraSuperRareSword, "Scary Ultra Super Rare Sword", "30", "0", "0", 60)
                        if buy == True:
                            scaryUltraSuperRareSword = True
                        elif buy == "exit":
                            break
                        buy = buyOrNot(scaryUltraSuperRareQuantumSword, "Scary Ultra Super Rare Quantum Sword", "40", "0", "0", 80)
                        if buy == True:
                            scaryUltraSuperRareQuantumSword = True
                        elif buy == "exit":
                            break
                        buy = buyOrNot(scaryUltraSuperRareQuantumImmortalSword, "Scary Ultra Super Rare Quantum Immortal Sword", "50", "0", "500", 120)
                        if buy == True:
                            scaryUltraSuperRareQuantumImmortalSword = True
                        elif buy == "exit":
                            break
                        buy = buyOrNot(scaryUltraSuperRareQuantumImmortalDeathlySword, "Scary Ultra Super Rare Quantum Immortal Deathly Sword", "60", "0", "1000", 180)
                        if buy == True:
                            scaryUltraSuperRareQuantumImmortalDeathlySword = True
                        elif buy == "exit":
                            break
                        buy = buyOrNot(scaryUltraSuperRareQuantumImmortalDeathlySwordOfDoom, "Scary Ultra Super Rare Quantum Immortal Deathly Sword of Doom", "100", "0", "2500",260)
                        if buy == True:
                            scaryUltraSuperRareQuantumImmortalDeathlySwordOfDoom = True
                        elif buy == "exit":
                            break
                        buy = buyOrNot(scaryArmour, "Scary Armour", "0", "5", "0", 10)
                        if buy == True:
                            scaryArmour = True
                        elif buy == "exit":
                            break
                        buy = buyOrNot(scaryUltraArmour, "Scary Ultra Armour", "0", "10", "0", 20)
                        if buy == True:
                            scaryUltraArmour = True
                        elif buy == "exit":
                            break
                        buy = buyOrNot(scaryUltraSuperArmour, "Scary Ultra Super Armour", "0", "20", "0", 30)
                        if buy == True:
                            scaryUltraSuperArmour = True
                        elif buy == "exit":
                            break
                        buy = buyOrNot(scaryUltraSuperRareArmour, "Scary Ultra Super Rare Armour", "0", "30", "0", 40)
                        if buy == True:
                            scaryUltraSuperRareArmour = True
                        elif buy == "exit":
                            break
                        buy = buyOrNot(scaryUltraSuperRareQuantumArmour, "Scary Ultra Super Rare Quantum Armour", "0", "40", "0", 50)
                        if buy == True:
                            scaryUltraSuperRareQuantumArmour = True
                        elif buy == "exit":
                            break
                        buy = buyOrNot(scaryUltraSuperRareQuantumImmortalArmour, "Scary Ultra Super Rare Quantum Immortal Armour", "0", "50", "500", 80)
                        if buy == True:
                            scaryUltraSuperRareQuantumImmortalArmour = True
                        elif buy == "exit":
                            break
                        buy = buyOrNot(scaryUltraSuperRareQuantumDeathlyArmour, "Scary Ultra Super Rare Quantum Immortal Deathly Armour", "0", "60", "1000", 120)
                        if buy == True:
                            scaryUltraSuperRareQuantumDeathlyArmour = True
                        elif buy == "exit":
                            break
                        buy = buyOrNot(scaryUltraSuperRareQuantumImmortalDeathlyArmourOfDoom, "Scary Ultra Super Rare Quantum Immortal Deathly Armour of Doom", "0", "100", "2500",260)
                        if buy == True:
                            scaryUltraSuperRareQuantumImmortalDeathlyArmourOfDoom = True
                        elif buy == "exit":
                            break

                        shopAgain = input("I hope your shopping went well! Would you like to shop again?\n") # Asks if the player would like to shop again
                        if shopAgain not in ["yes", "no"]: # Makes sure the player says "yes" or "no"
                            shopAgain = input("You didn't say yes or no. You must say yes or no.")
                        if shopAgain == "yes":
                            print("Ok.")
                        else:
                            print("I hope your shopping went well!")
                            break
                        death = False

                if fightOrFlee == "wander": # If the player chooses to wander, if they do not have enough food, they can't. If they do, they wander
                    if playersFood < 1:
                        print("You do not have enough food to wander. Maybe you'll find more food next time!")
                    else:
                        wanderCounter = 0
                        wandering()

            if death == True: # At the end of each turn, if death is True, the player dies, the game ends, and the program asks the player if they want to play again
                deathStatement()
                break

            print("\nYou continue on your journey.") # If the player lives, they continue on their journey and the turn starts all over again
    else:
        print("Okay then. Goodbye.") # If the player does not want to play, the program ends
        break
