class Pet:

    def __init__(self, name, weight, species):
        self.name = name
        self.weight = weight
        self.species = species
        self.alive = True
        self.offspring = []
        print(f'{self.name} successfully initiated.')
    
    def __repr__(self):
        if self.offspring:
            return f'Meet {self.name}. A {self.species} that weighs {self.weight} kg. {self.name} is alive: {self.alive} and has {len(self.offspring)} children, named {", ".join(self.offspring)}'
        else:
            return f'Meet {self.name}. A {self.species} that weighs {self.weight} kg. {self.name} is alive: {self.alive}'

    def birth(self, baby_name):
        self.offspring.append(baby_name)
        print(f'Congratulations to {self.name} on the birth of a new baby {self.species} named {baby_name}!')

class Dog(Pet):
    def __init__(self, name, weight, howls):
        Pet.__init__(self, name, weight, 'dog')
        self.howls = howls

    def __repr__(self):
        return super().__repr__() + f". Does {self.name} howl? " + str(self.howls)

billy = Pet('Billy', 22, 'goat')
rover = Pet('Rover', 13, 'dog')
rover.birth('Spot')
rover.birth('Samantha')

chewy = Dog('Chewie', 15, True)
chewy.birth('Chewbacca Jr')

print(billy)
print(rover)
print(chewy)

print(chewy.offspring)
billy.alive = False
print(billy)