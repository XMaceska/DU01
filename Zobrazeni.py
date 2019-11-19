from math import sin, tan, log, radians, degrees

# definice proměnných

R = 6371.11         # poloměr země [km]
c = 10              # vzdálenost mezi souřadnicemi [°]

rovnobezky = []
poledniky = []

a = input("Na výběr z několika válcových tečných zobrazení: \n\nL pro Lambertovo zobrazení \nA pro Marinovo zobrazení \nB pro Braunovo zobrazení \nM pro Mercatorovo zobrazení\n\nZvolte požadované zobrazení:")
b = int(input("Zvolte požadované měřítko: ",))

polomer = input("Chcete zvolit vlastní poloměr země? A/N: ")

# tohle celkem blbost vlastně, musím napsat, v jakých chcete zadat jednotkách? elif print: odkaz na převod jednotek

while polomer == "A":
    jednotky = (input("V jakých jednotkách chcete zadat poloměr země? [km], [m] anebo [cm], [?] pro pomoc s převody: "))
    if jednotky == "km":
        R = float(input("Zadejte požadovaný poloměr země v km: "))
        R = R*100000
        break
    if jednotky == "m":
        R = float(input("Zadejte požadovaný poloměr země v m: "))
        R = R*100
        break
    if jednotky == "cm":
        R = float(input("Zadejte požadovaný poloměr země v cm: "))
        R = R
        break
    if jednotky == "?":
        print("Potřebujete odkaz na převod jednotek? https://www.jednotky.cz/")
        continue
    else:
        print("Zadejte prosím pouze znak(y) v hranatých závorkách")
        continue
if polomer == "N":
    R = R*100000

# tvorba funkcí ze vzorců pro zobrazení
# v = poledniky, u = rovnobezky

def lambert(R):
    for v in range(-180, 180, c):      # funkce range (start, stop, step)
        x = float(R*(radians(v)))
        x_vypocet_meritka = round(x/b,1)
        poledniky.append(x_vypocet_meritka)

    for u in range(-90, 90, c):
        y = R*sin(radians(u))
        y_vypocet_meritka = round(y/b,1)
        rovnobezky.append(y_vypocet_meritka)

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
        y = 2*R*tan(radians(u)/2)
        rovnobezky.append(y)

def mercator(R):
    for v in range(-180, 180, c):
        x = R*v
        poledniky.append(x)
    for u in range(-90, 91, c):
        y = R*log(1/tan(radians(u)/2))
        rovnobezky.append(y)

if a == "L":
    lambert(R)
    print("Lambertovo zobrazení:\n""Rovnoběžky:", rovnobezky, "\nPoledníky:", poledniky)

elif a == "A":
    marin(R)
    print("Marinovo zobrazení:\n""Rovnoběžky:", rovnobezky, "\n", "Poledníky:", poledniky)

elif a == "B":
    braun(R)
    print("Braunovo zobrazení:\n""Rovnoběžky:", rovnobezky, "\n", "Poledníky:", poledniky)

elif a == "M":
    mercator(R)
    print("Mercatorovo zobrazení:\n""Rovnoběžky:", rovnobezky, "\n", "Poledníky:", poledniky)

else:
    print("pro písmeno",a, "není definované žádné zobrazení")
    exit()



