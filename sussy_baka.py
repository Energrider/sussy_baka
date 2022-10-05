while True:
 import random

 turns = ['Rock', 'Paper', 'Scissors']
 human_turn = input("Rock, Paper or Scissors? Type 'Stop' to stop the game! ")
 computer_turn = random.choice(turns)
 human_turns = []
 computer_turns = []
 if human_turn == 'Stop':
  break
 elif human_turn == computer_turn:
     print('Draw! Both Lose!')
 elif human_turn == 'Rock' and computer_turn == 'Scissors':
     print('You Win! (Rock beats Scisssors!)')

 elif human_turn == 'Paper' and computer_turn == 'Rock':
     print('You Win! (Paper beats Rock!)')

 elif human_turn == 'Scissors' and computer_turn == 'Paper':
     print('You Win! (Scissors beats Paper!)')
 else:
     print('You Lose!')

