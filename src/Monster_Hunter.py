# Created on 1/22/17.

import random

monsterList = ["Vaporscream","Stoneghoul","Tombbug","Mistspawn","Agitated Horror","Arid Beast","Stormcloud Venom Hawk","Iron-Scaled Predator Phoenix","Grim Berserker Rhino","Giant Bone Tiger","Spectralwraith","Spitepaw","Ebon Flame Sheep","Brineclaw"]

def deathStatement():
    print("You died\nYour level was: " + str(lvlCounter) + "\nYour overall score was " + str(overallXPCounter))

def buyOrNot(nameOfItem, attackBonus, defenseBonus, xpGainBonus, cost):
    print("You have " + str(playersGold) + " Gold.")
    wantToBuy = input("Would you like to buy the " + nameOfItem + "? It will grant you:\nAttack: " + attackBonus + "\nDefense: " + defenseBonus + "\nWill increase your XP gain by: " + xpGainBonus + "\n\nThis item costs " + str(cost) + "\n\n(to answer, just say \"yes\". If you do not wish to buy this item, you may say anything else)\n(to exit, simply enter \"exit\"\n")
    if wantToBuy == "yes":
        global playersGold
        if playersGold < cost:
            print("You do not have enough gold to buy this item!")
            return False
        print("Congratulations! You are now equipped with the " + nameOfItem + "!")
        playersGold -= cost
        return True
    elif wantToBuy == "exit":
        return "exit"
    else:
        return False

while True:
    wannaPlay = input("\nWould you like to play a game of Monster Hunter?\n")
    while wannaPlay not in ["yes", "no"]:
        print("You did not say \"yes\" or \"no\"\n")
    if wannaPlay == "yes":
        lvlCounter = 0
        xpCounter = 0
        overallXPCounter = 0
        playersGold = 0
        scarySword = False
        scaryUltraSword = False
        scaryUltraSuperSword = False
        scaryUltraSuperRareSword = False
        scaryUltraSuperRareQuantumSword = False
        scaryUltraSuperRareQuantumImmortalSword = False
        scaryUltraSuperRareQuantumImmortalDeathlySword = False
        scaryUltraSuperRareQuantumImmortalDeathlySwordOfDoom = False

        scaryArmour = False
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
If you choose to flee, you will lose some xp
In the beginning, it will be very easy and you will receive bonuses, but it will become harder as you level up

Good Luck!\n\n""")

        while True:
            monsterNameNum = random.randint(0, 13)
            monsterLvlNum = random.randint(-5, 4)
            monsterLvl = lvlCounter + monsterLvlNum
            requiredXP = lvlCounter * 500 + lvlCounter * lvlCounter * lvlCounter
            monsterXPRan = random.randint(-100, 200)
            monsterXP = monsterLvl * 200 + monsterXPRan
            monsterHPRan = random.randint(-10, 10)
            monsterAttackRan = random.randint(-10, 10)
            playerHPRan = random.randint(-10, 10)
            playerAttackRan = random.randint(-10, 15)
            monsterHP = monsterLvl * (5 + (lvlCounter / 10)) + monsterHPRan
            monsterAttack = monsterLvl * (2 + (lvlCounter / 10)) + monsterHPRan
            playerHP = lvlCounter * 5 + playerHPRan
            playerAttack = lvlCounter * 2 + playerAttackRan
            if monsterXP < 0:
                monsterXP -= monsterXP * 2
            if scarySword == True:
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
            if scaryArmour == True:
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
            fightOrFlee = input("A wild " + monsterList[monsterNameNum] + " of level " + str(
                monsterLvl) + " has appeared. Will you fight or flee?\n")
            while True:
                if fightOrFlee not in ["fight", "flee", "shop"]:
                    fightOrFlee = input(
                        "You did not say \"fight\" or \"flee\" or \"shop\". You must say \"fight\" or \"flee\" or \"shop\"\n")
                else:
                    break
            if fightOrFlee == "fight":
                print("You have chosen to fight")
                if playerAttack <= 0:
                    playerAttack = 6
                while True:
                    monsterHP = monsterHP - playerAttack
                    if monsterHP <= 0:
                        if monsterLvl < 0:
                            monsterLvl = -monsterLvl
                        print("You killed the monster!")
                        playersGold += monsterLvl
                        death = False
                        if monsterLvl > lvlCounter:
                            print(
                                "Because you killed a monster that was a higher level than yourself, your xp gain tripled!")
                            monsterXP *= 3
                        xpCounter += monsterXP
                        overallXPCounter += monsterXP
                        print("You have gained " + str(monsterXP) + "XP\nYou now have " + str(
                            xpCounter) + " XP!\nYou have gained " + str(monsterLvl) + " Gold!\nYou now have " + str(
                            playersGold) + " Gold!")
                        if xpCounter >= requiredXP:
                            xpCounter = 0
                            lvlCounter += 1
                            print("You have gotten to a new level! You are now on level " + str(lvlCounter) + "!")
                        break
                    playerHP = playerHP - monsterAttack
                    if playerHP < 0:
                        death = True
                        break
            elif fightOrFlee == "flee":
                xpCounter -= lvlCounter * 100
                print("You have fled. you lost " + str(-(lvlCounter * 100)) + " XP\nYou now have " + str(
                    xpCounter) + " XP.")
                death = False
            elif fightOrFlee == "shop":
                xpCounter -= lvlCounter * 150
                print("You lost " + str(lvlCounter * 150) + " XP")
                while True:
                    buy = buyOrNot("Scary Sword", "5", "0", "0", 20)
                    if buy == True:
                        scarySword = True
                    elif buy == "exit":
                        break
                    buy = buyOrNot("Scary Ultra Sword", "10", "0", "0", 30)
                    if buy == True:
                        scaryUltraSword = True
                    elif buy == "exit":
                        break
                    buy = buyOrNot("Scary Ultra Super Sword", "20", "0", "0", 40)
                    if buy == True:
                        scaryUltraSuperSword = True
                    elif buy == "exit":
                        break
                    buy = buyOrNot("Scary Ultra Super Rare Sword", "30", "0", "0", 60)
                    if buy == True:
                        scaryUltraSuperRareSword = True
                    elif buy == "exit":
                        break
                    buy = buyOrNot("Scary Ultra Super Rare Quantum Sword", "40", "0", "0", 80)
                    if buy == True:
                        scaryUltraSuperRareQuantumSword = True
                    elif buy == "exit":
                        break
                    buy = buyOrNot("Scary Ultra Super Rare Quantum Immortal Sword", "50", "0", "500", 120)
                    if buy == True:
                        scaryUltraSuperRareQuantumImmortalSword = True
                    elif buy == "exit":
                        break
                    buy = buyOrNot("Scary Ultra Super Rare Quantum Immortal Deathly Sword", "60", "0", "1000", 180)
                    if buy == True:
                        scaryUltraSuperRareQuantumImmortalDeathlySword = True
                    elif buy == "exit":
                        break
                    buy = buyOrNot("Scary Ultra Super Rare Quantum Immortal Deathly Sword of Doom", "100", "0", "2500",
                                   260)
                    if buy == True:
                        scaryUltraSuperRareQuantumImmortalDeathlySwordOfDoom = True
                    elif buy == "exit":
                        break
                    buy = buyOrNot("Scary Armour", "0", "5", "0", 10)
                    if buy == True:
                        scaryArmour = True
                    elif buy == "exit":
                        break
                    buy = buyOrNot("Scary Ultra Armour", "0", "10", "0", 20)
                    if buy == True:
                        scaryUltraArmour = True
                    elif buy == "exit":
                        break
                    buy = buyOrNot("Scary Ultra Super Armour", "0", "20", "0", 30)
                    if buy == True:
                        scaryUltraSuperArmour = True
                    elif buy == "exit":
                        break
                    buy = buyOrNot("Scary Ultra Super Rare Armour", "0", "30", "0", 40)
                    if buy == True:
                        scaryUltraSuperRareArmour = True
                    elif buy == "exit":
                        break
                    buy = buyOrNot("Scary Ultra Super Rare Quantum Armour", "0", "40", "0", 50)
                    if buy == True:
                        scaryUltraSuperRareQuantumArmour = True
                    elif buy == "exit":
                        break
                    buy = buyOrNot("Scary Ultra Super Rare Quantum Immortal Armour", "0", "50", "500", 80)
                    if buy == True:
                        scaryUltraSuperRareQuantumImmortalArmour = True
                    elif buy == "exit":
                        break
                    buy = buyOrNot("Scary Ultra Super Rare Quantum Immortal Deathly Armour", "0", "60", "1000", 120)
                    if buy == True:
                        scaryUltraSuperRareQuantumDeathlyArmour = True
                    elif buy == "exit":
                        break
                    buy = buyOrNot("Scary Ultra Super Rare Quantum Immortal Deathly Armour of Doom", "0", "100", "2500",
                                   260)
                    if buy == True:
                        scaryUltraSuperRareQuantumImmortalDeathlyArmourOfDoom = True
                    elif buy == "exit":
                        break
                    print("I hope your shopping went well!")
            else:
                print("You have chosen not to shop")
                death = False
            if death == True:
                deathStatement()
                break
            print("\nYou continue on your journey")
    else:
        print("Okay then. Goodbye.")
        break
