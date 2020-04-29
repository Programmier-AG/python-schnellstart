einkaufsliste = ["Äpfel", "Birnen"]

while True:
    print("----- HAUPTMENÜ -----")
    print("Was möchtest du machen?")
    print(": hinzufügen")
    print(": entfernen")
    print(": auflisten")

    aktion = input(": ")

    if aktion == "hinzufügen":
        print(einkaufsliste)
        item = input("Was soll hinzugefügt werden?")
        einkaufsliste.append(item)
        print(einkaufsliste)
    elif aktion == "entfernen":
        print(einkaufsliste)
        item = input("Was soll entfernt werden? ")
        einkaufsliste.remove(item)
        print(einkaufsliste)
    elif aktion == "auflisten":
        print(einkaufsliste)