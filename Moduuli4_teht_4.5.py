# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja
# salasanan. Jos jompikumpi tai molemmat ovat väärin, tunnus
# ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot
# ovat oikein tai väärät tiedot on syötetty viisi kertaa. Edellisessä
# tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

Kayttajatunnus = "Python"
Salasana = "rules"


while Kayttajatunnus != "python":
    Kayttajatunnus = input("kerro käyttäjätunnus: ")
    Salasana = input("kerro salasana: ")
    if Kayttajatunnus == "Python":
    if Salasana == "rules":
        print("Tervetuloa")
    else:
        print("Pääsy evätty")
