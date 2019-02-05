# 1. What is the output of the following program?
# a. You pass
# b. You pass
# c. Blank

average = float(input("Input your average: "))
if average > 60:
    print("You pass.")
if average < 60:
    print("You fail.")

# 2. Rewrite the program above so that it explicitly handles the case where the average is 60.

average = float(input("Input your average: "))
if average >= 60:
    print("You pass.")
if average < 60:
    print("You fail.")

# 3. Rewrite the program above using an if-else statement.

average = float(input("Input your average: "))
if average >= 60:
    print("You pass.")
else:
    print("You Fail.")

# 4. Write a resort activity advisory program that asks the user to enter the current temperature and the program
# recommends an activity. Use the following guide for your program:

temperature = float(input("Input your temperature: "))
if temperature >= 80:
    print('Go swimming.')
if 79 >= temperature >= 70:
    print('Play tennis.')
if 69 >= temperature >= 50:
    print('Go hiking.')
if temperature < 50:
    print('Sit by the fire.')

temp = int(input("Enter the current temperature: "))
if temp > 80:
    print("Go swimming")
elif temp >= 70:
    print("Play tennis.")
elif temp >= 50:
    print("Go hiking.")
else:
    print("Sit by the fire.")

# 5

bill1 = int(input("First month water bill: "))
bill2 = int(input("Second month water bill: "))
bill3 = int(input("Third month water bill: "))

average = (bill1 + bill2 + bill3) / 3

if average > 75:
    print("You are using an excessive amount of water.")
elif average > 50:
    print("You are using more than a normal amount of water.")
elif average >= 25:
    print("You are using a normal amount of water.")
else:
    print("You don't use very much water.")


# Write a function that takes 3 water bills and prints a statement
def water_bill(b1, b2, b3):
    average = (b1 + b2 + b3) / 3
    if average > 75:
        print("You are using an excessive amount of water.")
    elif average > 50:
        print("You are using more than a normal amount of water.")
    elif average >= 25:
        print("You are using a normal amount of water.")
    else:
        print("You don't use very much water.")


bill1 = int(input("First month water bill: "))
bill2 = int(input("Second month water bill: "))
bill3 = int(input("Third month water bill: "))

water_bill(bill1, bill2, bill3)
