__author__ = 'sstarodu'

# str
print(str(1) + "a")

print("first" "second")  # firstsecond

print('''hello,
my dear ''')

path = r'C:\n\r\c\d\path'  # raw string
print(path)  # C:\n\r\c\d\path

print("aa".capitalize())  # Aa
print("aa".upper())  # AA

print(len("123"))  # 3

# join
print(';'.join(["1", "2", "3"]))  # 1;2;3

# partition
print("asdfadfadf".partition("fa")) # ('asd', 'fa', 'dfadf')

# format
print("The age of {0} is {1}".format("Bob", "25"))
print("The age of {name} is {age}".format(age="25", name="Bob"))
