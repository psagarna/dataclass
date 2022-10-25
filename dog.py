class Dog:

    def __init__(self, name, age):
        self.name= name
        self.age= age
        self.color="azul"

    def __init__(self, name, age,color):
        self.name= name
        self.age= age
        self.color= color

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} is now rolling over")

    def getDetails(self):
        return f"{self.name} tiene {self.age} años y color {self.color}"


myDog= Dog("Willi","30")
myDog.sit()
print(myDog.getDetails())
myDog.age=50
print(myDog.getDetails())

class Caniche(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)


caniche=Caniche("susi","12")
print(caniche.getDetails())

