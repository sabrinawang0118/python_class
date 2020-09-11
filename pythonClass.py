#define parent class Animal, containing a few methods hello(), sleep() and run()
class Animal:
    def __init__(self, name, age):
        self.age=age
        self.name=name
    
    def hello(self):
        print("Hello! my name is "+ self.name+ ", age is "+self.age)
        
    def sleep(self):
        print(self.name , "is sleeping")
    
    def run(self):
        print(self.name, "is running")
        
#example: an instance of parent class Animal inheritating all properties 
class any_animal(Animal):
    pass
 
 
#define class dog, child of Animal, inheriting sleep() and run() from parent class, and overwritting hello() with a new same-named method
class dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def hello(self):
        print("Hello! my name is "+ self.name+ ", age is "+ self.age+ ", and my breed is "+self.breed)
     
 
#example of object of animal using parent methods from Animal class
random_animal=Animal("Lucy", "10")
random_animal.sleep()
random_animal.run()
random_animal.hello()
 
print("---------------------------------------- divider------------------------------------------------------")

#example of object of dog(child of Animal) accessing parent methods sleep() and run(), and its own method hello() overwriting the Animal hello()
fido= dog("Fido", "4", "labrador")
fido.hello()
fido.sleep() 
