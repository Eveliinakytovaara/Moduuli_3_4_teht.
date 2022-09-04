# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa,
# onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi, jos se on
# jaollinen neljällä. Sadalla jaolliset vuodet ovat
# karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.


Vuosiluku = int(input("Anna vuosiluku "))
luku_1 = 4
luku_2 = 400

jakojaannos = Vuosiluku % luku_1 or Vuosiluku % luku_2
if jakojaannos == 0:
    print(Vuosiluku, "on karkausvuosi")

else:
    print("Vuosiluku ei ole karkausvuosi")





