# Local - lives in a function

data = 1   # Global scope

def fun1():
    data = 2       # Local

def fun2():
    global data  # marks as global to refer to top-level 'data'
    data = 2

fun1()
print(data)
fun2()
print(data)

# Enclosing

# Global

# Built-in
