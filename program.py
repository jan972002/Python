from ast import Return
import math


a = int(10)
b = int(100)
c = int(200)
d = int(150)


print(str("\n\n\n\n\n\nMożesz wybrać tylko 3000kg produktów z pośród \ngrochu 5zł za opakowanie 10kg\ncukru 200zł za opakowanie 100kg\nkapusty 30zł za opakowanie 200kg\nbambusa 50zł za opakowanie 150kg\n\n\n\n", ))
f = int(input("Wybierz ile opakowań   GROCHU   chcesz?  ") )
g = int(input("Wybierz ile opakowań   CUKRU   chcesz?  "))
i = int(input("Wybierz ile opakowań   KAPUSTY   chcesz?  "))
o = int(input("Wybierz ile opakowań   BAMBUSA   chcesz?  "))


h = int(5)
e = int(200)
m = int(30)
k = int(50)
print("\n\n\n")
print(f*a, "kg grochu ", " w cenie", (f*h))
print(g*b, "kg cukru ", " w cenie", (g*e))
print(i*c, "kg kapusty ", " w cenie", (i*m))
print(o*d, "kg bambusa ", " w cenie", (o*k))

print("\n\n")

fa = (f*a)
gb = (g*b)
ic = (i*c)
od = (o*d)



fh = (f*h)
ge = (g*e)
im = (i*m)
ok = (o*k)


fagbicod = int(fa+gb+ic+od)    #masa
fhgeimok = int(fh+ge+im+ok)    #cena

pro = int(0.9*fhgeimok)


if fhgeimok > 2000 and fagbicod <3000:
    print("Otrzymujesz bonus, -10% wartości zamówienia")
    print(str("do zapłaty po odliczeniu rabatu",pro, "zł!"))
elif fagbicod >0 and fagbicod<3000:
    print("Twoje zamówienie o wartości", fhgeimok, "zł", "i masie",fagbicod,"kg", "zostało przyjęte, opłać je przy kasie!")
else:
    print("Zamówiłeś",fagbicod, "kg produktów w cenie", fhgeimok, "Masa twojego zamóienia przekracza dopuszczalny limit. \nProsimy złożyć zamówienie ponownie.")


print("\n\n")
    #potrzeba dodać pętlę ponownego odtwarzania
