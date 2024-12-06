'''
Napišite program koji omogućuje korisniku da pretvori temperaturu iz Celzija u Fahrenheite ili iz Fahrenheita u Celzije. Program treba prvo pitati korisnika što želi (opcije: "C u F" ili "F u C"). Na temelju izbora, tražite unos temperature i ispišite rezultat. Koristite if za provjeru odabira.
Formula za pretvaranje iz C u F: F = C * 9/5 + 32
Formula za pretvaranje iz F u C: C = (F - 32) * 5/9


'''

temperatura = float(input("Unesite temperatru: "))

print("1 - Pretvori stupnje C u F")
print("2 - Pretvori stupnje F u C")

odabir = int(input("Unesite odabir: "))

if odabir == 1:
    t = temperatura * 9/5 + 32
    print(str(temperatura) + " stupnjeva C je " + str(t) + " stupnjeva F")
elif odabir == 2:
    t = (temperatura - 32) * 9/5
    print(str(temperatura) + " stupnjeva F je " + str(t) + " stupnjeva C")
else:
    print("pogresan odabir")
