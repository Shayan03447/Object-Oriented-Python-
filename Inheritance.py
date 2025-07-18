class Animal:
    def __init__(self, name):
        self.name=name
    def speak(self):
        print(f"{self.name} makes a sound")
#Drived class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

animal=Animal("Genraic animal")
animal.speak()
        
dog=Dog("buddy")
dog.speak()
        