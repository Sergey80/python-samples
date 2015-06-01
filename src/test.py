print("hello")

l = len([1, 2, 3])

print(l)

# for loop - braces are not needed
for i in range(5):
    x = i * 10
    print(x)

# never mix tab and spaces

print("1")

import math

print(math.sin(0))  # we can use dot ...

n = 5
k = 3
result = math.factorial(n) / (math.factorial(k))

print("result:" + str(result))  # str - to string

print(0x10)  # to hex

print(float(1))  # 1.0

# None, True, False
bool(0)   # False
bool(42)  # True
bool(0.2)  # True
bool([])    # False
bool([1, 2, 3])  # True
bool("")  # False
bool("False")  # True

# flow

if 1 < 2:
    print("it is indeed")

if False:
    print("never")
else:  #  elif
    print("Always")

times = 0
while times < 3:
    times += 1
    print(times)

count = 0
while True:
    count += 1
    if count == 3:
        break

print("count:" + str(count))




