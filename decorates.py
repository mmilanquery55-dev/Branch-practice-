
def hello():
   print("hi milan")


def greet(fx):
    def mfx():
      print("Good morning ")
      fx()
      print("Thanks for using ")
    return mfx 

greet(hello)()

class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name} and {self.age}")

s1=Student("Milan",20)
s1.info()



   