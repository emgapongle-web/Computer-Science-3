#Create a class for the RPG Hero
class RPGHero:
    def __init__(self, name, health):
        self.name = name #The name of the hero
        self.health = health #The health of the hero

    def stats(self):
        return f"Hero Name: {self.name}, Health: {self.health}"

    def take_damage(self, damage):
        self.health = self.health - damage

RPGHero1 = RPGHero("Arthur", 100)
RPGHero2 = RPGHero("Morgana", 100)

RPGHero1.take_damage(10) #Damage that RPGHero1 takes

print(RPGHero1.stats()) #Prints the stats of RPGHero1 after taking damage
print(RPGHero2.stats()) #Prints the stats of RPGHero2