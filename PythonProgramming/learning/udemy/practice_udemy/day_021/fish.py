from animal import Animal


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe_fish(self):
        super().breathe()
        print("doing this underwater")
        
    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim() # from class Fish
nemo.breathe() # from class Animal
print(nemo.num_eyes)
nemo.breathe_fish()