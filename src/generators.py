# all generators are iterators
# are lazy evaluated (the next value in the sequence is computed on demand)
# can model infinite sequences
# are composable into pipeline (for natural stream processing)

# generators

def gen123():
    print("!1")
    yield 1
    print("!2")
    yield 2
    print("!3")
    yield 3


g = gen123()

print(g)  # <generator object gen123 at 0x02397698>

a = next(g)
b = next(g)
c = next(g)

print(a)  # 1
print(b)  # 2
print(c)  # 3

for v in gen123():  # can be used in the for loop (as any iterator)
    print(v)


# Stateful generators

def take(count, itrable):
    """Take first count elements"""
    counter = 0
    for item in itrable:
        if counter == count:
            return
        counter += 1
        yield item


items = [2, 4, 6, 8, 10]
for item in take(2, items):
    print(item)  # 2,4

# result = sum(x * x for x in range(1, 100))
# print(result)  # 328350
