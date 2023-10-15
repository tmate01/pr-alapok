import random
gondolt_szam = random.randint(1, 5)
bekert_szam = int(input("Kérem, adjon meg egy számot 1 és 5 között: "))
if bekert_szam == gondolt_szam:
    print("Gratulálok, találtad el a számot!")
elif bekert_szam < gondolt_szam:
    print("A gondolt szám nagyobb, mint a megadott szám.")
else:
    print("A gondolt szám kisebb, mint a megadott szám.")
