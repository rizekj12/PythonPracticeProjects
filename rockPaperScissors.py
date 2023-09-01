

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random 

#first attempt

# randomNum = random.randint(1,3)

# if randomNum == 1:
#   computerChoice = rock
# elif randomNum == 2:
#   computerChoice = paper
# elif randomNum == 3:
#   computerChoice = scissors
  
# yourChoice = input("Welcome to Rock, Paper, Scissors. What do you pick?\n").lower()


# print(f"Computer choice:\n{computerChoice}")

# if yourChoice == 'paper' and computerChoice == rock:
#   print(f"Your choice:\n {paper}")
#   print("You win!")
# elif yourChoice == 'paper' and computerChoice == scissors:
#   print(f"Your choice:\n {paper}")
#   print("You lose!")
# elif yourChoice == 'paper' and computerChoice == paper:
#   print(f"Your choice:\n {paper}")
#   print("tie")
# elif yourChoice == 'rock' and computerChoice == scissors:
#   print(f"Your choice:\n {rock}")
#   print("You win!")
# elif yourChoice == 'rock' and computerChoice == paper:
#   print(f"Your choice:\n {rock}")
#   print('You lose!')
# elif yourChoice == 'rock' and computerChoice == rock:
#   print(f"Your choice:\n {rock}")
#   print('tie')
# elif yourChoice == 'scissors' and computerChoice == paper:
#   print(f"Your choice:\n {scissors}")
#   print('You win!')
# elif yourChoice == 'scissors' and computerChoice == rock: 
#   print(f"Your choice:\n {scissors}")
#   print('You lose!')
# elif yourChoice == 'scissors' and computerChoice == scissors:
#   print(f"Your choice:\n {scissors}")
#   print('tie')
# else:
#   print('invalid entry, please type rock, paper, or scissors')

  #second attempt refactored with a list 

options = [rock, paper, scissors]

randomNum = random.randint(0,2)

computerChoice = options[randomNum]

yourChoice = input("Welcome to Rock, Paper, Scissors. What do you pick?\n").lower()

print(f'computer choice:\n {computerChoice}')

if yourChoice == 'paper' and computerChoice == rock:
  print(f"Your choice:\n {paper}")
  print("You win!")
elif yourChoice == 'paper' and computerChoice == scissors:
  print(f"Your choice:\n {paper}")
  print("You lose!")
elif yourChoice == 'paper' and computerChoice == paper:
  print(f"Your choice:\n {paper}")
  print("tie")
elif yourChoice == 'rock' and computerChoice == scissors:
  print(f"Your choice:\n {rock}")
  print("You win!")
elif yourChoice == 'rock' and computerChoice == paper:
  print(f"Your choice:\n {rock}")
  print('You lose!')
elif yourChoice == 'rock' and computerChoice == rock:
  print(f"Your choice:\n {rock}")
  print('tie')
elif yourChoice == 'scissors' and computerChoice == paper:
  print(f"Your choice:\n {scissors}")
  print('You win!')
elif yourChoice == 'scissors' and computerChoice == rock: 
  print(f"Your choice:\n {scissors}")
  print('You lose!')
elif yourChoice == 'scissors' and computerChoice == scissors:
  print(f"Your choice:\n {scissors}")
  print('tie')
else:
  print('invalid entry, please type rock, paper, or scissors')


