class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.birds = []
        self.fish = []

    def add_animals(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'bird':
            self.birds.append(name)
        elif species == 'fish':
            self.fish.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            return print(f"Mammal in {self.name}: {', '.join(self.mammals)}\n"
                         f"Total animals: {Zoo.__animals}")
        elif species == 'fish':
            return print(f"Fishes in {self.name}: {', '.join(self.fish)}\n"
                         f"Total animals: {Zoo.__animals}")
        elif species == 'bird':
            return print(f"Birds in {self.name}: {', '.join(self.birds)}\n"
                         f"Total animals: {Zoo.__animals}")


zoo = Zoo(input())
for i in range(int(input())):
    animal_info = input().split(' ')
    zoo.add_animals(animal_info[0], animal_info[1])

animal_kind = input()
zoo.get_info(animal_kind)

