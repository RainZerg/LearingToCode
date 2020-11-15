import pickle


class Character:

    def __init__(self, race, damage=10):
        self.race = race
        self.armor = 20
        self.health = 100
        self.damage = damage

    def hit(self, damage):
        puredamage = damage - self.armor
        self.armor -= damage
        if self.armor <= 0:
            self.health -= puredamage
            self.armor = 0

    def is_dead(self):
        return self.health == 0

    def __setstate__(self, state):
        self.race = state.get('race', 'Elf')
        self.damage = state.get('damage', 10)
        self.armor = state.get('armor', 20)
        self.health = state.get('health', 100)


c = Character('Elf')
c.hit(10)
print(c.health)
print(c.armor)

with open(r'game_state.bin', 'w+b') as f:
    pickle.dump(c, f)

c = None
print(c)
with open(r'game_state.bin', 'rb') as f:
    c = pickle.load(f)

print(c.health)
print(c.armor)

print(c.__dict__)
