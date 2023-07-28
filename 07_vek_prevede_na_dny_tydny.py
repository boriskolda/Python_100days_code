age = input("Vlozte svůj věk? ")

dny = 90 * 365 - int(age) * 365
tydny = 90 * 52 - int(age) * 52
mesice = 90 * 12 - int(age) * 12
roky = 90 - int(age)

print(f"You have {dny} days, {tydny} weeks, and {mesice} months left.")