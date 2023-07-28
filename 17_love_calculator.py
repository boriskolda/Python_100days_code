# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()
name = name1_lower + name2_lower

cislo1 = name.count("t") + name.count("r") + name.count("u") + name.count("e")
cislo2 = name.count("l") + name.count("o") + name.count("v") + name.count("e")

hodnota = int(str(cislo1) + str(cislo2))

if hodnota < 10 or hodnota > 90:
   print(f"Your score is **{hodnota}**, you go together like coke and mentos.")

elif hodnota >= 40 and hodnota <=50: 
    print(f"Your score is **{hodnota}**, you are alright together.")

else:
    print(f"Your score is **{hodnota}**.")

