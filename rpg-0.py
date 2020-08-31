"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Hero:  ## Step 1: define Hero class.
    hero_health = 0
    hero_power = 0
    def __init__(self): ## Assign hero_health/hero_power to objects.
        self.hero_health = Hero.hero_health
        self.hero_power = Hero.hero_power

    def attack(self, enemy):
        goblin_health -= hero_power
        print("You do %d damage to the goblin." % hero_power)

    def alive(self, goblin_health):    
        if goblin_health <= 0:
            print("The goblin is dead.")

    def print_status(self):
        print("You have %d health and %d power." % (hero_health, hero_power))






class Goblin: ## Step 1: define Goblin class.
    def __init__(self):  ## Assign goblin_health/goblin_power to objects.
        self.health = 0
        self.power = 0

    def attack(self, enemy):
        hero_health -= goblin_power
        print("The goblin does %d damage to you." % goblin_power)

    def alive(self, hero_health):    
        if hero_health <= 0:
            print("You are dead.")

    def print_status(self):
        print("The goblin has %d health and %d power." % (goblin_health, goblin_power))


    


def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

    

    while goblin.alive(hero_health) and hero.alive(goblin_health):
        
        
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)

        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin_health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
main()
