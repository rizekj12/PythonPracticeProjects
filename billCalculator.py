# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("welcome to the tip calculator")
print("(please only use numbers as inputs, no special characters)")
bill = float(input("what is the total of your bill? \n$"))
tip_percent = input("what percent would you like to tip?\n")
ppl_to_split = input("how many people to split the bill?\n")

tip_as_float = int(tip_percent) / 100

total_bill_after_tip = round(bill * tip_as_float + float(bill), 2)

final_bill_for_each = total_bill_after_tip / float(ppl_to_split)

print(f"Each person should pay: ${final_bill_for_each}")
