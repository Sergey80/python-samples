s = set([1, 2, 3, 3])  # list to set
print(s)  # {1, 2, 3}

s.add(4)  # {1, 2, 3, 4}
print(s)

s.remove(1)
print(s)  # {2, 3, 4}

s1 = {1, 2, 3}   # notice: we use {} not [] to define Set
s2 = {1, 4, 3}

# union
print(s1.union(s2))  # {1, 2, 3, 4}
print(s1.issubset(s2))  # False
print(s1.issubset(s2))  # False
print({1, 4}.issubset(s2))  # True

print(len(s1))  # 3
