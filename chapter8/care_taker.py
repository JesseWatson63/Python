# Critter Cartaker
# A virtual pet to care for

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, bordem = 0):
        self.name = name
        self.hunger = hunger
        self.bordem = bordem

    def __pass_time(self):
        self.hunger += 1
        self.bordem += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.bordem

        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 15:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m="furstrated"
        else:
            m = "mad"
        return m
            
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food = 4):
        print("Brupppp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("WHEEEEEE!")
        self.bordem -= fun
        if self.bordem < 0:
            self.bordem = 0
        self.__pass_time()

def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print \
        ("""
        Critter Caretaker
        
        0 - Quit 
        1 - Listen to you Critter 
        2 - Feed your Critter 
        3 - PLay with your Critter 
        """)

        choice = input("Choice: ")
        print()

        # exit 
        if choice == "0":
            print("Good Bye")

        # listen to your Critter
        elif choice == "1":
            crit.talk()

        # feed you Critter
        elif choice == "2":
            crit.eat()

        # play with you Critter
        elif choice == "3":
            crit.play()

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice")

main()
("\n\nPRess the enter key to exit.")