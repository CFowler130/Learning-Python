cheeses = ['Chedder', 'Edam', 'Gouda']
numbers = [42, 123]
empty = []
print(cheeses, numbers, empty)

['Chedder', 'Edam', 'Gouda']
for cheese in cheeses:
    print(cheese)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)

# List operations
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
c

# List slices
t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3]

t[:4]

t[3:]

# List methods
# Append method

t = ['a', 'b', 'c']
t.append('d')
t

# Extend method
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
t1

# Sort method
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
t


# To add up all the numbers in a list, you can use a loop like this:


def add_all(t):
    total = 0
    for x in t:
        total += x
    return total


print(add_all(t))

# Built in function (sum) that does it for you

tsum = sum(t)
tsum


# List filter functions


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


capitalize_all(t)


def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
        return res


only_upper(t)

# Deleting elements
# .pop
t = ['a', 'b', 'c']
x = t.pop(1)
t

# del
t = ['a', 'b', 'c']
del t[1]
t

# .remove
t = ['a', 'b', 'c']
t.remove('b')
t

# del with slice index
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
t

# If statement example
if 'f' in t:
    t.remove('f')
else:
    print('not in list')


# Lists and strings
s = 'spam'
t = list(s)
t

# split method
s = 'pining for the fjords'
t = s.split()
t

# delimiter example
s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
t

# join method
t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
s = delimiter.join(t)
s

