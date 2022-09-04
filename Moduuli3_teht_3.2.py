# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C)
# ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
# Tehtävässä on käytettävä if/elif/else-toistorakennetta.

# LUX on parvekkeellinen hytti yläkannella.
# A on ikkunallinen hytti autokannen yläpuolella.
# B on ikkunaton hytti autokannen yläpuolella.
# C on ikkunaton hytti autokannen alapuolella.
# Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

Hyttiluokka_1 = "LUX"
Hyttiluokka_2 = "A"
Hyttiluokka_3 = "B"
Hyttiluokka_4 = "C"
Hyttiluokka = input("kerro hyttiluokkasi ")

if Hyttiluokka_1 == Hyttiluokka:
    print("LUX on parvekkeellinen hytti yläkannella")
elif Hyttiluokka_2 == Hyttiluokka:
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif Hyttiluokka_3 == Hyttiluokka:
    print("B on ikkunaton hytti autokannen yläpuolella")
elif Hyttiluokka_4 == Hyttiluokka:
    print("C on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")



