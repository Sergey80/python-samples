class Person:
    def help(self):
        print("Heeeelp!")

class Duck:
    def help(self):
        print("Quaaaaaack!")

class SomethingElse:
    pass

donald = Duck()
john = Person()
who = SomethingElse()

def in_the_forest(x):
    x.help()

for thing in [donald, john, who]:
    try:
        in_the_forest(thing)
    except AttributeError:
        print('Meeowww!')
