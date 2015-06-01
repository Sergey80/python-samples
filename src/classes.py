"""Model for aircraft flights"""

class Flight:
    """some doc here"""

    def __init__(self, number):  # initialization method (it is not a constructor). Should not return anything.

        # Invariants:

        # Begins for upper case two letters then 3-4 numbers
        if not number[:2].isalpha():    # 2 first letters are alphabetic
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():    # 2 first letters are uppercase
            raise ValueError("Invalid airline code '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):  # 2 latest is digits, but not too big
            raise ValueError("Invalid route number '{}'".format(number))

        # code

        self._number = number

    def number(self):
        return self._number



#from src.classes import Flight

f = Flight("NN123")
#  f = Flight("NNaaa")  # will fail
#  f = Flight("123")    # will fail with ValueError
#  f = Flight("NN99999")    # will fail with ValueError

print(f.number())

