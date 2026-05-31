
def hello():
   print("hi milan")


def greet(fx):
    def mfx():
      print("Good morning ")
      fx()
      print("Thanks for using ")
    return mfx 

greet(hello)()