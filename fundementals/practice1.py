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