# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen
# ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko
# hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

gender = input("sukupuolesi (nainen/mies)? ")
hg_value = int(input("hemoglobiinisi (g/l)? "))

if gender == "nainen":
    # tetsataan naisen ohjearvoja vastaan
    if hg_value < 117:
        print("Hemoglobiiniarvo on alhainen ")
    elif hg_value <= 175:
        print("Hemoglobiiniarvo on normaali ")
    else:
        print("Hemoglobiiniarvo on korkea ")
elif gender == "mies":
    #testataan miehen ohjearvoja vastaan
    if hg_value < 134:
        print("Hemoglobiiniarvo on alhainen")
    elif hg_value <=195:
        print("Hemoglobiiniarvo on normaali")
    else:
        print("Hemoglobiiniarvo on korkea")

else:
    print("ei kumpikaan")
    #TODO: tulosta virheilmoitus(?)
