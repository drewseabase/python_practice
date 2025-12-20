p1 = input("Rock, Paper or Scissors? ").lower()
p2 = input("Rock, Paper or Scissors? ").lower()


if p1 == p2:
    print("Draw!")
elif p1 == 'rock' and p2 == 'scissors':
    print("Player 1 won!")
elif p1 == 'paper' and p2 == 'rock':
    print("Player 1 won!")
elif p1 == 'scissors' and p2 == 'paper':
    print("Player 1 won!")
elif p2 == 'rock' and p1 == 'scissors':
    print("Player 2 won!")
elif p2 == 'paper' and p1 == 'rock':
    print("Player 2 won!")
elif p2 == 'scissors' and p1 == 'paper':
    print("Player 2 won!")

