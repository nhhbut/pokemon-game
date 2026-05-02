class Pokemon:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def __repr__(self):
        return f"Nom : {self.name}, PV restants : {self.health}, Attaque : {self.attack}"

    def take_damages(self, damage_received):
        self.health -= damage_received
        if self.health < 0:
            self.health = 0

    def deal_damages(self, pokemon):
        print(f"{self.name} attaque {pokemon.name}")
        pokemon.take_damages(self.attack)

    def pokemon_alive(self):
        return self.health > 0


def combat(pokemon1, pokemon2):
    tour = 1

    while pokemon1.pokemon_alive() and pokemon2.pokemon_alive():
        print(f"\n--- Tour {tour} ---")

        pokemon1.deal_damages(pokemon2)
        print(pokemon2)

        if not pokemon2.pokemon_alive():
            print(f"{pokemon2.name} a perdu le combat.")
            print(f"{pokemon1.name} a gagné !")
            break

        pokemon2.deal_damages(pokemon1)
        print(pokemon1)

        if not pokemon1.pokemon_alive():
            print(f"{pokemon1.name} a perdu le combat.")
            print(f"{pokemon2.name} a gagné !")
            break

        tour += 1


pikachu = Pokemon("Pikachu", 80, 30)
salameche = Pokemon("Salamèche", 90, 20)

print(pikachu)
print(salameche)

combat(pikachu, salameche)