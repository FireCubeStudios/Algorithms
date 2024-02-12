class Knight:
    def __init__(self, health, strength, index):
        self.health = health
        self.strength = strength
        self.index = index

    # Damage the knight by a specified amount, return true if dead
    def damage(self, amount):
        self.health -= amount
        return True if self.health <= 0 else False

# Recursively battles knights and returns survivor
def recursive_battle(knight1: Knight, knight2: Knight):
    if(knight2.damage(knight1.strength)): return knight1
    return recursive_battle(knight2, knight1)

def battle(knight1: Knight, knight2: Knight):
    while True:
        if knight2.damage(knight1.strength): return knight1
        knight1, knight2 = knight2, knight1

knights: int = int(input())

health1, strength1 = map(int, input().split())
health2, strength2 = map(int, input().split()) if (knights > 1) else (0, 0)
survivor = battle(Knight(health1, strength1, 1), Knight(health2, strength2, 2))

if(knights > 2):
    for i in range(3, knights + 1):
        health, strength = map(int, input().split())
        survivor = battle(survivor, Knight(health, strength, i))

print(survivor.index)