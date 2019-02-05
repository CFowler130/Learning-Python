# Exercise 9-1
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) >= 20:
        print(word)


# Exercise 9-2
def has_no_e(word):
    if not 'e' in word:
        return True
    return False


fin = open('words.txt')
count = 0
no_es = 0
for line in fin:
    word = line.strip()
    count = count + 1
    if has_no_e(word):
        print(word)
        no_es = no_es + 1
print('The percentage of words with no e is: ', (no_es / count) * 100)


# Exercise 9-3
def avoids(word, forbidden):
    for i in range(0, len(word)):
        if word[i] in forbidden:
            return False
    return True


fin = open('words.txt')
forbidden = input('Enter the forbidden letters: ')
count = 0
for line in fin:
    word = line.strip()
    if avoids(word, forbidden):
        count = count + 1
print(count)
