from math import sin, tan
import sys


# definice proměnných

R = 6371.11

a = input("Na výběr z několika zobrazení: \n\nL pro Lambertovo zobrazení \nA pro Marinovo zobrazení \nB pro Braunovo zobrazení \nM pro Mercatorovo zobrazení\n\nZvolte požadované zobrazení:")

b = int(input("Zvolte požadované měřítko:",))

def lambert(R):
    for v in range (-180,180):
        x = 10


def marin(R):
    return "rofl"
def braun(R):
    print("ok")
def mercator(R):
    print("not ok")

if a == "L":
    print("Lambertovo zobrazení:", lambert(R))
elif a == "A":
    print(marin(R))



