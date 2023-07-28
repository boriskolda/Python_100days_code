# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

pocet = len(names)

nahodne_cislo = random.randint(0, pocet-1)
jmeno = names[nahodne_cislo]

print(f"{jmeno} is going to buy the meal today!")





