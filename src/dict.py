# dict (no order, keys are immutable, values may be mutable)

print("----dicts")

d = {'alice': "222", 'bob': "333"}

print(d['bob'])  # 333

# for
for k in d:
    print(k)  # alice, bob


for v in d.values():
    print(v)