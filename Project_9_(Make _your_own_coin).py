import random

class Pound :

    def __init__(self,rare=False) :

        self.rare= rare

        if self.rare :
            self.value = 1.25
        else    :
            self.value = 1.00

        self.colour = "Gold"
        self.diameter = 22.5
        self.thickness = 3.15
        self.heads = True

    def __del__(self) :
        print("Coin spent")
        
    def rust(self) :
        self.colour = "Greenish"

    def clean(self) :
        self.colour = "Gold"

    def flip(self) :
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
