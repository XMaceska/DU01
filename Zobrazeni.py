from math import sin, tan, log, radians,pi

# definice proměnných

R = 6371.11         # poloměr země [km]
c = 10              # vzdálenost mezi souřadnicemi [°]

rovnobezky = []
poledniky = []


#  z = Výběr zobrazení, neplatný vstup ošetřen pomocí vnořené funkce While

z = input("Na výběr z několika válcových tečných zobrazení: \n\nL pro Lambertovo zobrazení \nA pro Marinovo zobrazení \nB pro Braunovo zobrazení \nM pro Mercatorovo zobrazení\n\nZvolte požadované zobrazení: ")
while z != "L" and z != "A" and z != "B" and z != "M":
    print("pro znak",z, "není definováno žádné zobrazení\n")
    druhy_pokus = input("Na výběr pouze z uvedených válcových tečných zobrazení: \n\nL pro Lambertovo zobrazení \nA pro Marinovo zobrazení \nB pro Braunovo zobrazení \nM pro Mercatorovo zobrazení\n\nZvolte požadované zobrazení: ")
    while druhy_pokus == "L" and druhy_pokus == "A" and druhy_pokus == "B" and druhy_pokus == "M":
        break
    if druhy_pokus != "L" and druhy_pokus != "A" and druhy_pokus != "B" and druhy_pokus != "M":
        print("pro znak",druhy_pokus,"také není definováno žádné zobrazení")
        druhy_pokus = z
        continue
    break


# m = výběr měřítka, Požadovaný vstup integer. While True funkce oštřuje nechtěný vstup string.

while True:
    m = (input("Zvolte požadované měřítko: "))
    if m.isdigit():
        m = int(m)
        print(f'Zvolil(a) jste měřítko 1:{m}') # kudrnaté závorky z důvodu, aby nebyla mezera za dvojtečkou.
        break
    else:
        print({m},"není číslo (integer), zadejte prosím pouze celočíslenou hodnotu:")


# Volba vlastního poloměru země.
# Pomocí vnořených příkazů IF umožněna volba jednotek při vstupu.
# Výsledný poloměr vždy převeden na jednotky cm.

while True:
    polomer = input("Chcete zvolit vlastní poloměr země? A/N: ")
    if polomer == "A":
        jednotky = (input("V jakých jednotkách chcete zadat poloměr země?\n[km], [m] anebo [cm], [?] pro pomoc s převody: "))
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
            print("Zadejte prosím pouze znak(y) uvedené v hranatých závorkách")
            continue
    if polomer == "N":
        R = R*100000
        break
    else:
        print("Zadal jste nesprávný vstup. Zadejte prosím pouze A pro ANO a N pro NE ")


# definice jednolivých funkcí za pomocí dostupných vzorců
# v = poledniky, u = rovnobezky
# Ve Vzorcích se dosazují radiány - nutný převod ze stupnů na radiány.
# V závěru každé funkce výstup přepočten pomocí zadaného měřítka, následně každá hodnota vložena do vytvořeného seznamu
# Funkcí IF ošetřeno je-li hodnota vzdáleností > 100 cm vypíše "-"



def lambert(R):
    for v in range(-180, 180, c):      # funkce range (start, stop, step)
        x = float(R*(radians(v)))
        x_vypocet_meritka = round(x / m, 1)
        if abs(x_vypocet_meritka) > 100:
            x_vypocet_meritka = "-"
        poledniky.append(x_vypocet_meritka)

    for u in range(-90, 90, c):
        y = R*sin(radians(u))
        y_vypocet_meritka = round(y / m, 1)
        if abs(y_vypocet_meritka) > 100:
            y_vypocet_meritka = "-"
        rovnobezky.append(y_vypocet_meritka)

def marin(R):
    for v in range(-180, 180, c):
        x = float(R*(radians(v)))
        x_vypocet_meritka = round(x / m, 1)
        if abs(x_vypocet_meritka) > 100:
            x_vypocet_meritka = "-"
        poledniky.append(x_vypocet_meritka)

    for u in range(-90, 90, c):
        y = R*(radians(u))
        y_vypocet_meritka = round(y / m, 1)
        if abs(y_vypocet_meritka) > 100:
            y_vypocet_meritka = "-"
        rovnobezky.append(y_vypocet_meritka)

def braun(R):
    for v in range(-180, 180, c):
        x = R*(radians(v))
        x_vypocet_meritka = round(x / m, 1)
        if abs(x_vypocet_meritka) > 100:
            x_vypocet_meritka = "-"
        poledniky.append(x_vypocet_meritka)
    for u in range(-90, 90, c):
        y = 2*R*tan(radians(u)/2)
        y_vypocet_meritka = round(y / m, 1)
        if abs(y_vypocet_meritka) > 100:
            y_vypocet_meritka = "-"
        rovnobezky.append(y_vypocet_meritka)

def mercator(R):
    for v in range(-180, 180, c):
        x = R*(radians(v))
        x_vypocet_meritka = round(x / m, 1)
        if abs(x_vypocet_meritka) > 100:
            x_vypocet_meritka = "-"
        poledniky.append(x_vypocet_meritka)
    for u in range(-89, 89, c):
        y = R*log(tan(radians(u)/2+(pi/4))) # goniometrická funkce "cotg" není dostupná, použito tan + pi/4.
        y_vypocet_meritka = round (y / m, 1)
        if abs(y_vypocet_meritka) > 100:
            y_vypocet_meritka = "-"
        rovnobezky.append(y_vypocet_meritka)


# Aplikace funkcí a vytisknutí seznamu vzdáleností rovnoběžek a poledníků

while z == "L":
    lambert(R)
    print("Lambertovo zobrazení:\n""Rovnoběžky:", rovnobezky, "\nPoledníky:", poledniky)
    input("Konec") # díky tomuto příkazu se okno cmd po ukončení nezavře
if z == "A":
    marin(R)
    print("Marinovo zobrazení:\n""Rovnoběžky:", rovnobezky, "\nPoledníky:", poledniky)
    input("Konec")
if z == "B":
    braun(R)
    print("Braunovo zobrazení:\n""Rovnoběžky:", rovnobezky, "\nPoledníky:", poledniky)
    input("Konec")
if z == "M":
    mercator(R)
    print("Mercatorovo zobrazení:\n""Rovnoběžky:", rovnobezky, "\nPoledníky:", poledniky)
    input("Konec")

