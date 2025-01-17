zbroj = 0
br_elemenata = 0
while True:
    broj = int(input("unesite neki broj: "))
    if broj < 0:
        print("kraj")
        break
    zbroj += broj
    br_elemenata += 1

a_sredina = zbroj/br_elemenata

print("Aritmeticka sredina brojeva je:", a_sredina)
