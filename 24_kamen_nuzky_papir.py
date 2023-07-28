import random

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

volba = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if volba == "0":
    print(rock)
elif volba == "1":
    print(paper)
elif volba == "2":
    print(scissors)
else:
    print("Wrong choice")

print("\n\nComputer chose")

pocitac_volba = str(random.randint(0, 2))

if pocitac_volba == "0":
    print(rock)
elif pocitac_volba == "1":
    print(paper)
elif pocitac_volba == "2":
    print(scissors)

if volba == pocitac_volba:
    print("It is a draw")
elif volba == "0" and pocitac_volba == "1":
    print("You lose")
elif volba == "0" and pocitac_volba == "2":
    print("You win")
elif volba == "1" and pocitac_volba == "0":
    print("You win")    
elif volba == "1" and pocitac_volba == "2":
    print("You lose")    
elif volba == "2" and pocitac_volba == "0":
    print("You lose")    
elif volba == "2" and pocitac_volba == "1":
    print("You win")    




