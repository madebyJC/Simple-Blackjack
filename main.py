import random as r 
from time import sleep
from replit import clear
from art import logo

sleep(0.5)
print(logo)

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  draw_card = r.choice(cards)
  return draw_card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0 

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
    
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif user_score > 21 and computer_score > 21:
    return "Draw"
  elif user_score == 0:
    return "Blackjack! you win"
  elif computer_score == 0:
    return "You lose, the opponent has Blackjack"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. you win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"

def play_game():
  sleep(0.5)
  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for n in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while is_game_over == False:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    sleep(1)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    sleep(1)
    print(f"   Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else: 
      sleep(1)
      user_deal = input("Type 'yes/y' to get another card, type 'no/n' to pass: ").lower()
      if user_deal == "yes" or user_deal == "y":
        user_cards.append(deal_card())
      else: 
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  sleep(0.5)
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  sleep(0.5)
  print(f"   Computer's final hand {computer_cards}, final score: {computer_score}")
  sleep(2)
  print(compare(user_score, computer_score))

sleep(3)
while input("Do you want to play agame of Blackjack? Type 'yes' or 'no': ").lower() == "yes":
  clear()
  play_game()