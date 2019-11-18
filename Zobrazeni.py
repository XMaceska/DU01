from math import sin, tan
import sys


# definice proměnných

R = 6371.11         # poloměr země [km]
c = 10              # vzdálenost mezi souřadnicemi [°]

Rovnobezky = []
Poledniky = []

a = input("Na výběr z několika válcových tečných zobrazení: \n\nL pro Lambertovo zobrazení \nA pro Marinovo zobrazení \nB pro Braunovo zobrazení \nM pro Mercatorovo zobrazení\n\nZvolte požadované zobrazení:")
b = int(input("Zvolte požadované měřítko:",))

def lambert(R):

    for v in range(-180,180,c):      # funkce range (start, stop, step)
        x = R*v
        Rovnobezky.append(x)
    for u in range(-90, 90, c):
        y = R*u
        Poledniky.append(y)



def marin(R):
    return "rofl"
def braun(R):
    print("ok")
def mercator(R):
    print("not ok")

if a == "L":
    lambert(R)
    print("Lambertovo zobrazení:\n""Rovnoběžky:", Rovnobezky,"\nPoledníky:", Poledniky)

elif a == "A":
    print("Marinovo zobrazení:\n""Rovnoběžky:", Rovnobezky,"\n","Poledníky:", Poledniky)

else:
    print("pro písmeno",a, "není definované žádné zobrazení")
    exit()



