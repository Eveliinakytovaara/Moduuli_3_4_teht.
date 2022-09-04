# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin
# järveen ilmoittaen samalla käyttäjälle, montako senttiä
# alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuhan_alamittainen_pituus = 37
kuhan_pituus_cm = int(input("anna kuhan pituus "))

if kuhan_pituus_cm <37:
    print("Laske kuha takaisin järveen")
    print(f"Kuhan pituudesta puuttuu {kuhan_alamittainen_pituus - kuhan_pituus_cm} cm ")
elif kuhan_pituus_cm >37:
    print("Voit pitää kuhan")






