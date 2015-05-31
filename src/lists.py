__author__ = 'sstarodu'

# list
aa = [1, 2, 3]
empty = []

aa.append(4)

print(aa)  # [1, 2, 3, 4]

aa.reverse()

print(aa)  # reversed [4, 3, 2, 1]

print(aa[:2])  # [4, 3]
print([1, 2, 3, 4][:-1])  # [1, 2, 3]

print("--slices")
# slices
s = "asdf asddfd df dfd".split()
print(s)  # ['asdf', 'asddfd', 'df', 'dfd']

print(s[-2])  # df

print(s[1:4])  # ['asddfd', 'df', 'dfd']
print(s[2:])  # ['df', 'dfd']

a = [[1, 2], [3, 4]]
b = a[:]
print(a)
print(b)
print(a is b)  # False
print(a == b)  # True

# list multiplication / repetition
c = [1, 2]
d = c * 4
print(d)  # [1, 2, 1, 2, 1, 2, 1, 2]
s = [[-1, +1]] * 2  # [[-1, 1], [-1, 1]]
print(s)

print(c.index(2))  # 2

# remove

c.remove(2)  # before it was: [1, 2]
print(c)  # [1]


#
print([1, 2, 3].extend([4, 5]))  # None

print(sorted([3, 1, 2]))  # [1, 2, 3]

