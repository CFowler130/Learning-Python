# A sequence of data separated by commas, yet not a list. You cannot change the elements of a tuple. Its immutable.

t = 'a','b','c','d','e'
t1 = (1,2,3,4,5)
t2 = 'a',
type(t2)
type(t1)
type(t)

print(t[0])

# you can do slices
t[1:3]

# If you're doing one element then you have to put the comma there
t3 = ('a',)
type(t3)

# You can also create a tuple using the function tuple
w = tuple('hello')
type(w)

# While you can't change them in place...
t = ('A',) + t[1:]
t

# Tuples can be tested for equality
(0,1,2) < (0,3,4)
(0,1,2000) < (0,3,4)

# In computing a lot of times we have to swap values. Say I want to swap those values so that A gets 1 and B gets 2.
a = 2
b = 1
temp = a
a = b
b = temp
print(a, b)

# Swapping using tuples
a = 2
b = 1
a, b = b, a
print(a, b)

# Division function used on tuples
t = divmod(7, 3)
t

# Star modifier takes the tuple and divides it into two
divmod(*t)

max(1)
sum(1, 2)
