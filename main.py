from art import logo, vs
from game_data import data
from replit import clear
import random

chosen = []

def chose():
  global chosen
  
  choice = random.randint(0,len(data) - 1)
  
  while choice in chosen:
    choice = random.randint(0,len(data) -1)
    
  chosen.append(choice)
  
  return choice
  
keep_go = True

choice1 = chose()
choice2 = chose()
score = 0
while keep_go:
  
  print(logo)
  print(f"Current score :{score}\n")
  print(f"Compare A: {data[choice1]['name']},{data[choice1]['follower_count']},{data[choice1]['description']},{data[choice1]['country']}")
  
  print(vs)
  
  print(f"Compare B: {data[choice2]['name']},{data[choice2]['follower_count']},{data[choice2]['description']},{data[choice2]['country']}")

  
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  if data[choice1]["follower_count"] > data[choice2]["follower_count"] and answer == "a":
    choice1 = choice2
    choice2 = chose()
    keep_go = True
    clear()
    score +=1

  elif data[choice2]["follower_count"] > data[choice1]["follower_count"] and answer == "b":
    choice1 = choice2
    choice2 = chose()
    keep_go = True
    clear()
    score +=1
  else:
    keep_go = False
    clear()
    print(F"You LOST! Final Score : {score}")