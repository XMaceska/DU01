from math import sin, tan
import sys


# definice proměnných

R = 6371.11

a = input("Na výběr z několika zobrazení: \n\nL pro Lambertovo zobrazení \nA pro Marinovo zobrazení \nB pro Braunovo zobrazení \nM pro Mercatorovo zobrazení\n\nZvolte požadované zobrazení:")

sirka = int(input("vlozte zeměpisnou šířku:"))
#delka = int(input("vlozte zeměpisnou délku:"))

while a == "L":
    print("vzdálenost je:", 2*R*sin(sirka/2))
if a == "A":
    print("x je:", R*delka,"\n","y je", R*sirka)
