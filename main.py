# Class for the functionality of a peg
class Unit:
    def __init__(self, name, cost, attack, health, star_level=0):
        self.name = name
        self.cost = cost
        self.attack = attack
        self.orig_health = health
        self.health = health
        self.star_level = star_level

    def print_stats(self):
        print(self.name, "| Cost:", self.cost, "| Health:", self.orig_health, "| Attack:", self.attack)

    def upgrade_star(self):
        self.star_level+=1
        self.orig_health *= 2
        self.health *= 2
        self.cost *= 2


    def is_alive(self):
        if self.health > 0:
            return True

    def take_damage(self, amount):
        self.health -= amount

    def reset(self):
        self.health = self.orig_health

def main():
    print("Hello World")

if __name__ == "__main__":
    main()