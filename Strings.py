fruit = banana
print(fruit[0])

fruit[1]

letter = fruit[2]
letter

i = 1
fruit[i]

# len = length in python
length = len(fruit)
length

last = len(fruit)-1
fruit[last]

# looping through a string
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

fruit = 'banana'
for letter in fruit:
    print(letter)

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes
    print(letter + suffix)

# string slices
s = 'Monty Python'
s[0:5]

s[1:5]

s[2:5]

s[:4]

# strings are immutable
greeting = 'Hello, world!'
# you can't change the value, must create new string that is a variation on the original
new_greeting = 'J' + greeting[1:]
new_greeting

# searching
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

fruit = 'banana'
print(find(fruit, 'a'))

# counting loop
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

# string methods
word = 'banana'
new_word = word.upper()
new_word

word = 'banana'
index = word.find('a')
index

# The in Operator
'a' in 'banana'

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both('apples', 'oranges')

# string comparison
if word == 'banana':
    print('same')
else:
    print('different')

