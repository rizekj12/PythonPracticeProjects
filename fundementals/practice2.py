# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontalPosition = int(position[0]) - 1 
verticalPosition = int(position[1]) - 1


selected_row = map[verticalPosition]
selected_row[horizontalPosition] = "X"

# chosenRow = f"row{position[0]}"
# chosenColumn = int(position[1]) - 1

# print(chosenRow[position[1]])

# if chosenRow == 'row1':
#     row1[chosenColumn] = "x"
# elif chosenRow == 'row2':
#     row2[chosenColumn] = "x"
# elif chosenRow == 'row3':
#     row3[chosenColumn] = "x"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")