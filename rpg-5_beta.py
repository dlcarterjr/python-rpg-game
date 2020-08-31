"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if self.health <= 0:
            print("%s is dead." % self.name)

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 5
        self.armor = 0
        self.evade = 0
        self.grenade = False

    def attack(self, enemy):
        if not self.alive():
            return
        if self.grenade:  ## Checks for holy handgrenade.
            throw_grenade = input("Do you wish to use your Holy Handgrenade ? (Y/N)")
            if throw_grenade.lower() == 'y':
                enemy.health = 0
                self.grenade = False
                return
        print("\n%s attacks %s" % (self.name, enemy.name))
        double_damage = random.random() < .2  ## Generate random number to see if hero does double-damage (< 20%) - STEP 1
        if double_damage:  
            enemy.receive_damage(self.power * 2)
        else:
            enemy.receive_damage(self.power)
            time.sleep(1.5)

    def receive_damage(self, points):
        if self.evade != 0:  ## Checks to see if any evade points.
            evade_attack = (((self.evade + 2) * 2.5) * .01) > random.random()  ## Evade attack probability starts at 10% and increases 5% points per 2 points increase (50% max).
            if evade_attack:
                print(f'{self.name} evades the {enemy.name}\'s attack.')  
        else:  ## If no evade points
            self.health -= points - self.armor
            print("%s received %d damage." % (self.name, points))
            if self.health <= 0:
                print("%s is dead." % self.name)

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to %d!" % self.health)
        time.sleep(1)

    def buy(self, item):
        if item.cost > self.coins:
            print("You don't have enough to buy that item.") ## Check if hero has enough coins to buy item.
            return
        self.coins -= item.cost
        item.apply(hero)

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.bounty = 5

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.bounty = 6

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("%s swaps power with %s during attack" % (self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):  ## STEP 2
    def __init__(self):
        self.name = 'medic'
        self.health = 10
        self.power = 5
        self.bounty = 2

    def receive_damage(self, points):
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        recuperate = random.random() < .2  ## See if medic will self-recuperate STEP 2:
        if recuperate:
            self.health += 2  ## recuperate
            print(f"{self.name} has self-recuperated 2 health points.")
        if self.health <= 0:
            print("%s is dead." % self.name)

class Shadow(Character):  ## STEP 3
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 5
        self.bounty = 3

    def receive_damage(self, points):
        not_deflect = random.random() < .1   ## See if deflects damage.
        if not_deflect:                     
            self.health -= points  ## If less than 10%, apply damage.
            print("%s received %d damage." % (self.name, points))
            if self.health <= 0:
                print("%s is dead." % self.name)
        else:
            print(f'{self.name} deflected the damage.')

class Zombie(Character):  ## STEP 4
    def __init__(self):
        self.name = 'zombie'
        self.health = 10
        self.power = 5
        self.bounty = 2

    def alive(self):  ## Zombie can't die.
        return True  ## Health will always be alive.

    def receive_damage(self, points):  ## Adjust damage method so Zombie health can go below 0 and be alive.
        self.health -= points
        print("%s received %d damage." % (self.name, points))
        if self.health <= 0:
            print("%ss can't die!!" % self.name)

class Ogre(Character):  ## STEP 5, New Character
    def __init__(self):
        self.name = 'ogre'
        self.health = 20
        self.power = 5
        self.bounty = 15

    def attack(self, enemy):
        if not self.alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        double_damage = random.random() < .6 ## 60% of double damage.
        if double_damage:  ## If statement for chance of double damage.
            enemy.receive_damage(self.power * 2)  ## If true, double damage.
        else:
            enemy.receive_damage(self.power)
            time.sleep(1.5)

class Thief(Character):  ## STEP 5, New Character
    def __init__(self):
        self.name = 'theif'
        self.health = 10
        self.power = 2
        self.coins = 0
        self.bounty = 2

    def attack(self, enemy):  ## Each time he attacks, he also steals 2 coins.
        if not self.alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        enemy.receive_damage(self.power)
        enemy.coins -= 2  ## steals coins
        time.sleep(1.5)

class Battle(object):
    def do_battle(self, hero, enemy):
        print("\n=====================")
        print("Hero faces the %s" % enemy.name)
        print("=====================")
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight %s" % enemy.name)
            print("2. do nothing")
            print("3. flee")
            print("> ",)
            user_input = int(input())
            if user_input == 1:
                hero.attack(enemy)
            elif user_input == 2:
                pass
            elif user_input == 3:  ## Change to actual flee option w/o ending the game.
                print("Run away! Run away!")
                return True
                #exit(0)
            else:
                print("Invalid input %r" % user_input)
                continue
            enemy.attack(hero)
        if hero.alive():
            print(f"\n**** YOU DEFEATED THE {(enemy.name).upper()}!! ****\n")
            print(f"You collect a bounty of {enemy.bounty} coins.")
            hero.coins += enemy.bounty
            return True
        else:
            #print("YOU LOSE!")
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("%s's health increased to %d." % (character.name, character.health))

class SuperTonic(object):  ## Added SuperTonic to store.
    cost = 15
    name = 'super tonic'
    def apply(self, character):
        character.health += 10
        print("%s's health increased to %d." % (character.name, character.health))

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("%s's power increased to %d." % (hero.name, hero.power))

class Armor(object):  ## Added armor to store. See line 53 for adjustment to damage.
    cost = 15
    name = 'armor'
    def apply(self, hero):
        hero.armor += 2  ## Increases armor attribute by 2.
        print(f'{hero.name}\'s armor is increase to {hero.armor}.')

class Broad_Sword(object):  ## Added broad sword to store.
    cost = 15
    name = 'broad sword'
    def apply(self, hero):
        hero.power += 3 ## Increases power (hit damage) by 1 point%.
        print(f'{hero.name}\'s power is increase to {hero.power}.')

class Evade(object):  ## Added evade to store. See line 55 for evade success calculation.
    cost = 15
    name = 'evade'
    def apply(self, hero):
        if hero.evade >= 38:  ## Check if evade ability is maxed out.
            print('You have already maxed out you evade ability.')
            return
        hero.evade += 2  ## Increases evade attribute by 2.
        print(f'{hero.name}\'s evade ability is increase to {hero.evade}.')

class Holy_hand_grenade(object):
    cost = 15
    name = 'holy hand grenade'
    def apply(self, hero):
        hero.grenade = True
        print("%s now has a holy hangrenade." % (hero.name))

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, SuperTonic, Sword, Armor, Evade, Broad_Sword, Holy_hand_grenade]
    def do_shopping(self, hero):
        while True:
            print("\n=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have %d coins." % hero.coins)
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("%d. buy %s (%d)" % (i + 1, item.name, item.cost))
            print("10. leave")
            user_input = int(input("> "))
            if user_input == 10:
                break
            else:
                ItemToBuy = Store.items[user_input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()  
enemies = [Wizard(), Goblin(), Medic(), Shadow(), Zombie(), Ogre()]  
battle_engine = Battle()
shopping_engine = Store()
for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print("\nYOU LOSE!\n")
        exit(0)
    shopping_engine.do_shopping(hero)

print("\nYOU WIN!\n")






###________________________________
            # TO-DO LIST
###________________________________
## Make it possible to select character for battle.
## Randomize the enemies during battle (make Ogre rare).
## Randomize damage.
## Add store to initial options list, stop it from automatically popping up after battle.
## Make program loop until hero dies. Now it just loops through enemy list.
## Format screen with some white space.