from math import sin, tan, log, radians,pi
import webbrowser

# definice proměnných

R = 6371.11         # poloměr země [km]
c = 10              # vzdálenost mezi souřadnicemi [°]

rovnobezky = []
poledniky = []


#  z = Výběr zobrazení, neplatný vstup ošetřen pomocí vnořené funkce While

while True:
    z = input("Na výběr z několika válcových tečných zobrazení: \n\nL pro Lambertovo zobrazení \nA pro Marinovo zobrazení \nB pro Braunovo zobrazení \nM pro Mercatorovo zobrazení\n\nZvolte požadované zobrazení: ")
    if z == "L" or z == "A" or z == "B" or z == "M":
        break
    else:
       print(f"pro znak \"{z}\" není definováno žádné zobrazení\n") # f-string. Díky kudrnatým závorkám a lomítkům vytiskne parametr z v uvozovkách.


# m = výběr měřítka, požadovaný vstup integer. While True funkce ošetřuje nechtěný vstup string.

while True:
    m = (input("Zvolte požadované měřítko: "))
    if m.isdigit():
        m = int(m)
        print(f'Zvolil(a) jste měřítko 1:{m}') # kudrnaté závorky z důvodu, aby nebyla mezera za dvojtečkou.
        break
    else:
        print(f"\"{m}\" není číslo (integer), zadejte prosím pouze celočíslenou hodnotu:")


# Volba vlastního poloměru země.
# Výsledný poloměr vždy převeden na jednotky cm.
# ValueError ošetřuje nesprávný vstup string

while True:
    polomer = input("Chcete zvolit vlastní poloměr země? A/N: ")
    if polomer == "A":
        jednotky = (input("V jakých jednotkách chcete zadat poloměr země?\n[km], [m] anebo [cm], [?] pro pomoc s převody: "))
        if jednotky == "km":
            while True:
                try:
                    R = float(input("Zadejte požadovaný poloměr země v km: "))
                except ValueError:
                    print("Zadaný znak není číslo, zadejte prosím pouze číselnou hodnotu poloměru země v km: ")
                    continue
                else:
                    R = abs((R*100000)) # abs ošetřuje vstup záporného měřítka
                    break
            break
        elif jednotky == "m":
            while True:
                try:
                    R = float(input("Zadejte požadovaný poloměr země v m: "))
                except ValueError:
                    print("Zadaný znak není číslo, zadejte prosím pouze číselnou hodnotu poloměru země v m: ")
                else:
                    R = abs(R*100)
                    break
            break
        elif jednotky == "cm":
            while True:
                try:
                    R = float(input("Zadejte požadovaný poloměr země v cm: "))
                except ValueError:
                    print("Zadaný znak není číslo, zadejte prosím pouze číselnou hodnotu poloměru země v cm: ")
                else:
                    R = abs(R)
                    break
            break
        elif jednotky == "?":
            print("Potřebujete odkaz na převod jednotek? https://www.jednotky.cz/")

            # Otevření odkazu v Google Chrome
            url = "https://www.jednotky.cz/"
            chrome_path_windows = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path_windows).open(url)
            chrome_path_linux = '/usr/bin/google-chrome %s'
            webbrowser.get(chrome_path_linux).open(url)
            chrome_path_MacOS = 'open -a /Applications/Google\ Chrome.app %s'
            webbrowser.get(chrome_path_MacOS).open(url)
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
# Ve vzorcích se dosazují radiány - nutný převod ze stupňů na radiány.
# V závěru každé funkce výstup přepočten pomocí zadaného měřítka, následně každá hodnota vložena do vytvořeného seznamu
# Funkcí IF ošetřeno je-li hodnota vzdáleností > 100 cm vypíše "-"



def lambert(R):
    for v in range(-180, 180+1, c):      # funkce range (start, stop, step), hodnota +1 z důvodu, aby byla započtena v range i hodnota 180
        x = float(R*(radians(v)))
        x_vypocet_meritka = round(x / m, 1) # funkce round (číslo, počet destinných míst)
        if abs(x_vypocet_meritka) > 100:
            x_vypocet_meritka = "-"
        poledniky.append(x_vypocet_meritka)

    for u in range(-90, 90+1, c):
        y = R*sin(radians(u))
        y_vypocet_meritka = round(y / m, 1) 
        if abs(y_vypocet_meritka) > 100:
            y_vypocet_meritka = "-"
        rovnobezky.append(y_vypocet_meritka)

def marin(R):
    for v in range(-180, 180+1, c):
        x = float(R*(radians(v)))
        x_vypocet_meritka = round(x / m, 1)
        if abs(x_vypocet_meritka) > 100:
            x_vypocet_meritka = "-"
        poledniky.append(x_vypocet_meritka)

    for u in range(-90, 90+1, c):
        y = R*(radians(u))
        y_vypocet_meritka = round(y / m, 1)
        if abs(y_vypocet_meritka) > 100:
            y_vypocet_meritka = "-"
        rovnobezky.append(y_vypocet_meritka)

def braun(R):
    for v in range(-180, 180+1, c):
        x = R*(radians(v))
        x_vypocet_meritka = round(x / m, 1)
        if abs(x_vypocet_meritka) > 100:
            x_vypocet_meritka = "-"
        poledniky.append(x_vypocet_meritka)
    for u in range(-90, 90+1, c):
        y = 2*R*tan(radians(u)/2)
        y_vypocet_meritka = round(y / m, 1)
        if abs(y_vypocet_meritka) > 100:
            y_vypocet_meritka = "-"
        rovnobezky.append(y_vypocet_meritka)

def mercator(R):
    for v in range(-180, 180+1, c):
        x = R*(radians(v))
        x_vypocet_meritka = round(x / m, 1)
        if abs(x_vypocet_meritka) > 100:
            x_vypocet_meritka = "-"
        poledniky.append(x_vypocet_meritka)
    for u in range(-89, 88+1, c):
        y = R*log(tan(radians(u)/2+(pi/4))) # goniometrická funkce "cotg" není dostupná, použito tan + pi/4.
        y_vypocet_meritka = round (y / m, 1)
        if abs(y_vypocet_meritka) > 100:
            y_vypocet_meritka = "-"
        rovnobezky.append(y_vypocet_meritka)


# Aplikace funkcí a vytisknutí seznamu vzdáleností rovnoběžek a poledníků
print(f'\nZvolil(a) jste měřítko 1:{m}')
print("Zvolil(a) jste poloměr země:", round(R*0.00001, 2), "km")

while z == "L":
    lambert(R)
    print("Lambertovo zobrazení:\n""Rovnoběžky:", rovnobezky, "\nPoledníky:", poledniky)
    exit()
if z == "A":
    marin(R)
    print("Marinovo zobrazení:\n""Rovnoběžky:", rovnobezky, "\nPoledníky:", poledniky)
    exit()
elif z == "B":
    braun(R)
    print("Braunovo zobrazení:\n""Rovnoběžky:", rovnobezky, "\nPoledníky:", poledniky)
    exit()
elif z == "M":
    mercator(R)
    print("Mercatorovo zobrazení:\n""Rovnoběžky:", rovnobezky, "\nPoledníky:", poledniky)
    exit()
else:
    exit()
