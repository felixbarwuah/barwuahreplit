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
# my code below

your_choice = input("What do you choose? Type 1 for rock, 2 for paper or 3 for scissor?\n")

if your_choice == "1".lower():
        print("you choose rock:" + rock)
if your_choice == "2".lower():
        print("you choose paper:" + paper)
if your_choice == "3".lower():
        print("you choose scissors:" + scissors)
else:
         print("You dumb!")



import random
computer_number = random.randint(1,3)

if computer_number == 1:
        print("The computer chooses rock:" + rock)
if computer_number == 2:
        print("The computer chooses paper:" + paper)
if computer_number == 3:
        print("The computer chooses scissors:" + scissors)

# stone beats scissors ; paper beats stone ; scissor beats paper

if your_choice == "1":
        if computer_number == 1:
                print("It's a draw. Try again!")
        if computer_number == 2:
                print("You won. Congratulations!")
        if computer_number == 3:
                print("The computer won. Sorry mate!")

if your_choice == "2":
        if computer_number == 1:
                print("You won. Congratulations!")
        if computer_number == 2:
                print("It's a draw. Try again!")
        if computer_number == 3:
                print("The computer won. Sorry mate!")

if your_choice == "3":
        if computer_number == 1:
                print("The computer won. Sorry mate!")
        if computer_number == 2:
                print("You won. Congratulations!")
        if computer_number == 3:
                print("It's a draw. Try again!")

else:
        print("You lost!")

print("\n Thanks for the playing the ultimative rock-paper-scissor Game at BarwuahGames69.")

# I had to distinguish between the two different data types. 
# If_your_choice is a str and computer_number is an int.
# Therefore I had to put "" around the str and not around the int.