class Animal:
    # Klasse wird initiiert
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        # Klasse Fish erbt von Animal
        # super() bezieht sich auf die zu vererbende Klasse
        super().__init__()

    def breathe(self):
        super().breathe()
        # breathe() der Superklasse wird ausgeführt und dann das print Statement der Fish Klasse ausgeführt.
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()
