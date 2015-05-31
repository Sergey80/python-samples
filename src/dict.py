# dict (no order, keys _must be_ immutable and unique, values may be mutable)
# #dict #update #copy #in #values #items #del

print("----dicts")

d = {'alice': "222", 'bob': "333"}   # {}

print(d['bob'])  # 333

# iterating over the dictionary

# for
for k in d:
    print(k)  # alice, bob


for v in d.values():    # by value
    print(v)

for key in d:   # by key
    print("{key} => {value}".format(key=key, value=d[key]))  # keys and values

for key, value in d.items():  # by items
    print("{key} => {value}".format(key=key, value=value))

names_and_ages = [('alice', 25), ('Bob', 28), ('James', 32)]
d = dict(names_and_ages)  # converts array of tuples into dictionary

print(d["Bob"])  # 28

dCopy = d.copy()  # copy
dCopy2 = dict(d)  # by dict() constructor

print(dCopy)

d2 = dict(one=1, two=2, three=3)
print("d2:" + str(d2))

d2.update(d)  # extend one dictionary by another
print("d2 updated:" + str(d2))

yesNo = "one" in d2
print(yesNo)            # True

del d2["Bob"]           # Bob item is removed from the dictionary
print(d2)


# pretty printing
from pprint import pprint as pp
pp(d2)

print(type(d2))  # <class 'dict'>


