import math

# count-controlled loop
x = 1
while x <= 10:
    print(x, math.sqrt(x))
    x = x + 1

# sentinel-controlled loop
while True:
    line = input('>')
    if line == 'done':
        break
    print(line)

print('Done')

# for-loop
for i in range(10):
    print(i)

# string is just a list of characters
word = input('Enter a word: ')
for letter in word:
    print(letter)