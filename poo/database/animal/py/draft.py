class :
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0
    

    def __str__(self):
        return f"{self.species}:{self.age}:{self.sound}"

    def ageBy(self, increment: int):
        if self.age => 4:
            print(f"warning: {self.species} foi pras cucuias")
            return
        
        self.age += increment


        if self.age >= 4:
            self.age = 4
            print(f"warning: {self.species} morreu")



    def makeSound(self):
        if self.age == 0:
            return "---"
        elif self.age >= 4:
            return "RIP"
        else:
            return self.sound