"""
Kérjünk be két egész számot, szám1 és szám2
Hasonlítsuk össze a két számto, és irassuk ki, hogy a "szám1 kisebb mint szám2" ,
vagy "a szám2 kisebb mint szám1" ,
vagy "a szám1 egyenlő szám2-vel".
"""

szam1 = int(input("Kérem, adjon meg egy egész számot (szám1): "))
szam2 = int(input("Kérem, adjon meg még egy egész számot (szám2): "))
"""
if szam1 < szam2:
    print(f"{szam1} kisebb mint {szam2}")
if szam1 > szam2:
    print(f"{szam2} kisebb mint {szam1}")
if szam1 == szam2:
    print(f"{szam1} egyenlő {szam2}-vel")
"""

if szam1 < szam2:
    print(f"{szam1} kisebb mint {szam2}")
elif szam1 > szam2:
    print(f"{szam2} kisebb mint {szam1}")
else:
    print(f"{szam1} egyenlő {szam2}-vel")
