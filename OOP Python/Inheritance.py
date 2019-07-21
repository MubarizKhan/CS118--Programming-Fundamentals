class Animal():
    def __init__(self):
        print("Animal created!")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


my_animal = Animal()

print(my_animal.eat())


class Dog(Animal): #Inheritance
    def __init__(self):
        Animal.__init__(self)
        print("Dog created!")

    def who_am_i(self):
        print("I am a dog")

    def eat(self):
        print("I am eating chicken manchurian & spanish margharita")


my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()

#------------------------Polymorphism----------------------------------------------

class toad():
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name + " says Rbit Rbit")
        return self.name 

class cat():
    
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name + " says Meow")
        return self.name 

grabby = toad("grabby")
grabby.speak()

felix = cat("felix")
felix.speak()

for i in [grabby,felix]:
    print (i.speak(), "<__DUffles ")


# -------------------#----------------------------------------------------------

class animalz():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


myani = animalz("gawlin")
# myani.speak() will raise an error


class dougee(animalz):
    def speak(self):
        print (self.name, "I am a dougeeeee")


class pussycat(animalz):
    def speak(self):
        print (self.name, "I am a kitty cat ")


cattie = pussycat("L")
cattie.speak()

pupper = dougee("jh")
pupper.speak()