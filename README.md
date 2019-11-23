# DU01
Program pro výpočet vzdáleností mezi body po aplikaci kartografického zobrazení.

1) Výběr zobrazení:

 - 4 definované válcové tečné zobrazení
 - Pro vstup zadat požadované písmeno

2) Volba meřítka

 - Ve formátu 1:<váš vstup>
 - Pouze celočíselný formát
 - S defaultním poloměrem země nejlépe funguje 1:50000000

3) Volba vlastního poloměru země
 
 - Volba "N" defaulní poloměr: 6371.11km
 - Vlastní vstup v jednotkách km, m anebo cm, dle volby
 - Při zadání záporné hodnoty program bude počítat s hodnout kladnou. 

4) Výsledek
 
- Defaulní nastavení rozmezí mezi poledníky a rovnoběžkami je 10°
- Zobrazí se seznam vzdáleností 18 rovnoběžek a 36 poledníků
- Pokud je vzdálenost větší, než 100cm, zobrazí se '-'
