from math import sin, tan, log1p, 
import sys


# definice proměnných

R = 6371.11         # poloměr země [km]
c = 10              # vzdálenost mezi souřadnicemi [°]

rovnobezky = []
poledniky = []

a = input("Na výběr z několika válcových tečných zobrazení: \n\nL pro Lambertovo zobrazení \nA pro Marinovo zobrazení \nB pro Braunovo zobrazení \nM pro Mercatorovo zobrazení\n\nZvolte požadované zobrazení:")
b = int(input("Zvolte požadované měřítko:",))


# tvorba funkcí ze vzorců pro zobrazení
# v = poledniky, u = rovnobezky

def lambert(R):
    for v in range(-180, 180, c):      # funkce range (start, stop, step)
        x = R*v
        poledniky.append(x)
    for u in range(-90, 90, c):
        y = R*sin(u)
        rovnobezky.append(y)

def marin(R):
    for v in range(-180, 180, c):
        x = R*v
        poledniky.append(x)
    for u in range(-90, 90, c):
        y = R*u
        rovnobezky.append(y)

def braun(R):
    for v in range(-180, 180, c):
        x = R*v
        poledniky.append(x)
    for u in range(-90, 90, c):
        y = 2*R*tan(u/2)
        rovnobezky.append(y)

def mercator(R):
    for v in range(-180, 180, c):
        x = R*v
        poledniky.append(x)
    for u in range(-90, 90, c):
        y = R*log1p()

if a == "L":
    lambert(R)
    print("Lambertovo zobrazení:\n""Rovnoběžky:", rovnobezky, "\nPoledníky:", poledniky)

elif a == "A":
    print("Marinovo zobrazení:\n""Rovnoběžky:", rovnobezky, "\n", "Poledníky:", poledniky)

else:
    print("pro písmeno",a, "není definované žádné zobrazení")
    exit()



