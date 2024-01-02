from art import *
import game_data
import random
print(logo)



correct_answers = 0
correct_answer = True
compareA = game_data.data[random.randint(0, len(game_data.data)-1)]
compareB = game_data.data[random.randint(0, len(game_data.data)-1)]
while correct_answer:
  

  print(f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}")

  print(vs)

  print(f"Compare B: {compareB['name']}, a {compareB['description']}, from {compareB['country']}")

  choice = input("Who has more followers? 'A' or 'B'? \n").lower()

  if choice == "a":
    if compareA['follower_count'] > compareB['follower_count']:
      correct_answers += 1
      print(f"You are correct! {compareA['name']} has more followers than {compareB['name']}.")
      print(f'You have {correct_answers} correct answers so far.')
      compareA = compareA
      compareB = game_data.data[random.randint(0, len(game_data.data)-1)]
    else:
      print(f"Sorry, {compareA['name']} does not have more followers than {compareB['name']}.")
      correct_answer = False
      break

  elif choice == "b":
    if compareA['follower_count'] < compareB['follower_count']:
      correct_answers += 1
      print(f"You are correct! {compareB['name']} has more followers than {compareA['name']}.")
      print(f'You have {correct_answers} correct answers so far.')
      
      compareB = compareB
      compareA = game_data.data[random.randint(0, len(game_data.data)-1)]
    else:
      print(f"Sorry, {compareB['name']} does not have more followers than {compareA['name']}.")
      correct_answer = False