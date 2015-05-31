def fun1():
    print("hello")


def fun2():
    print("hello2")


def fun3(arg1, arg2="123"):
    print(str(arg1) + " " + str(arg2))

fun1()
fun2()
fun3("value1")
fun3("value1", "value2")
