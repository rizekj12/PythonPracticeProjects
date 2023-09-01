
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