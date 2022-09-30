class God:
    def __init__(self):
        self.character = "Helping beings, Protecting Dharma"

    def trinity(self):
        trinity_god = input("Enter Name of the God: ").lower()
        if trinity_god == "brahma" or trinity_god == "vishnu" or \
                trinity_god == "shiva":
            print("Yes, Trinity")
        else:
            print("Not Trinity")

    @staticmethod
    def weapons(self):
        self.no_of_weapons = "Unlimited"


class Hanuman(God):
    def __init__(self):
        super().__init__()

    @staticmethod
    def description():
        print("Vaanaram")

    def trinity(self):
        super().trinity()
        print("But Avatar of a Trinity, Shiva")
        # Inherited a method from super class and customized for this class
        # This is called Override


hanuman = Hanuman()
hanuman.description()
print(hanuman.character)  # Inheriting attributes from super class
hanuman.trinity()  # Inheriting Methods from super class
