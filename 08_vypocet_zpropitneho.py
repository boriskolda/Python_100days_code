print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

vysledek = (bill + (bill / 100 * tip)) / people

vysledek_zaokr = round(vysledek,2)

print(f"Each person should pay: ${vysledek_zaokr}")