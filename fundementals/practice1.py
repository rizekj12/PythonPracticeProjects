# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

numStr = str(two_digit_number)

numOne = int(numStr[0])

numTwo = int(numStr[1])

sum = numOne + numTwo
print(sum)


## simple conditionals
number = int(input("what is your height in cm?"))

if number % 2 == 0:
    print("This is an even number.")
else :
    print("This is an odd number.")

##rollercoster ride 

print("welcome to the rollercoaster")
height = int(input("what is your height in cm?"))

if height >= 120:
  print("you can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("please pay $7")  
  else:
    print("Please pay $12")
else:
  print("Sorry, you have to grow taller before you can ride")