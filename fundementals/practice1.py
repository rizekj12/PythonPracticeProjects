
import random
import practiceModule

# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇

# numStr = str(two_digit_number)

# numOne = int(numStr[0])

# numTwo = int(numStr[1])

# sum = numOne + numTwo
# print(sum)


# ## simple conditionals
# number = int(input("what is your height in cm?"))

# if number % 2 == 0:
#     print("This is an even number.")
# else :
#     print("This is an odd number.")

# ##rollercoster ride 

# print("welcome to the rollercoaster")
# height = int(input("what is your height in cm?"))

# if height >= 120:
#   print("you can ride the rollercoaster!")
#   age = int(input("What is your age?"))
#   if age < 12:
#     print("Child tickets are $5.")
#     bill = 5
#   elif age <= 18:
#     print("Youth tickets are $7") 
#     bill = 7
#   elif age > 18: 
#     print("Adult tickets are $12")
#     bill = 12
#   elif age >= 45 and age <= 55:
#     bill = 0
#     print("midlife crisis tickets are $0")
#   photos = input("Would you like a photo taken? Type Y for yes and N for no.")
#   if photos == "Y" or photos == "y":
#     bill += 3
#     print(f"Your bill is ${bill}")
#   else:
#     print(f"Your bill is ${bill}")
# else:
#   print("Sorry, you have to grow taller before you can ride")

# random_int = random.randint(1,10)

# random_float = random.random() * 5

random_int = random.randint(0,1)

if random_int == 1:
    print("Heads")
else:
    print("Tails")

items = ["can","shovel","spoon","notebook"]


# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_num = random.randint(0, len(names) - 1)

print(names[random_num])


# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇


chosenRow = f"row{position[0]}"
chosenColumn = int(position[1]) - 1

# print(chosenRow[position[1]])

if chosenRow == 'row1':
    row1[chosenColumn] = "x"
elif chosenRow == 'row2':
    row2[chosenColumn] = "x"
elif chosenRow == 'row3':
    row3[chosenColumn] = "x"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")



