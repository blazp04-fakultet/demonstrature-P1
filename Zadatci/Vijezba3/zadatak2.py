broj_provjera = int(input("Unesite n: "))

for i in range(broj_provjera):
    if i % 15 == 0:
        print(i, "| FizzBuzz")
    elif i % 5 == 0:
        print(i, "| Buzz")
    elif i % 3 == 0:
        print(i,"| Fizz")
