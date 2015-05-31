# iterable protocol
# iter(iterable)

# iterator protocol
# item = next(iterator)

iterable = ["one", "two", "three"]
iterator = iter(iterable)
next(iterator)  # one
next(iterator)  # two
next(iterator)  # tree
# next(iterator)  # StopIteration


# --- zip
print(list(zip([1, 2, 3], ["a", "b", "c"])))  # [(1, 'a'), (2, 'b'), (3, 'c')]
