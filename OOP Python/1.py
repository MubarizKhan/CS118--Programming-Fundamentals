class Dog():

    #CLASS OBJECT ATTRIBUTE
    #SAME FOR EVERY OBJECT
    special = "mammal"

    #All arguments must be filled wwhen a new object will be made
    def __init__(self,breed,name,spots): #This is the constructor for the class
        self.breed = breed    #Attributes, we take in the attribute & Assign it using
        self.name = name          #using self.attribute_name = breed
        
        self.spots = spots #Expect true or false

    #METHODS--Operations/Actions-- Functions in a class
    def bark(self):
        print("WOOF!")

#my_sample = Sample()
#print(type(my_sample))

my_dog = Dog(breed = "Rott", name = "DEAN", spots = True)
print(my_dog.breed,"<---")
print(my_dog.name,"<---")
print(my_dog.spots,"<---")

my_dog.bark()


class circle():
    pi = 3.142 #Class object

    def __init__(self,radius):
        self.radius = radius
        self.area = radius * radius * self.pi

    #Method
    def get_circumference(self):
        print (2 * self.pi * self.radius,"<---")
        return 2 * self.pi * self.radius
    
    
my_circle = circle(6)
# my_circle.radius = 6

my_circle.get_circumference()
print (my_circle.area)