for cislo in range(1,101):
    if cislo % 3 == 0 and cislo % 5 == 0:
        print("FizzBuzz")
    elif cislo % 3 == 0:
        print("Fizz")
    elif cislo % 5 == 0:
        print("Buzz")
    else:
        print(cislo)


