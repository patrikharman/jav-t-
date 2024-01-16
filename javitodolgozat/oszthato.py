import random

print("2. feladat:")
def masodik():
    Lista = []
    for szam in range(0,50,1):
        vszam = random.randrange(1,100)
        Lista.append(vszam)
        print(vszam,end=",")
    return Lista

def kiir(Lista):
    for index in range(0, len(Lista)-1,1):
        print(f"{Lista}")

def ottel_oszthato():
    Lista = []
    for szam in range(0, 50, 1):
        vszam = random.randrange(1, 100)
        if vszam %5 == 0:
            print(f"Öttel osztható számok:{vszam}")


