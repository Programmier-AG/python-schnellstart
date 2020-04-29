einkaufsliste = ['Äpfel','Äpfel','Ps4']


while True:
    print('-------Hauptmenu----------')
    print('Was tun?')
    print(':Hinzufügen')
    print(': Entfernen')
    print(': Auflisten')

    aktion = input(':')

    if aktion == 'Hinzufügen':
        print(einkaufsliste)
        added = input('Was möchtest du hinzufügen?:')
        einkaufsliste.append(added)
    elif aktion == 'Entfernen':
        print(einkaufsliste)
        item = input('Was soll enfernt werden?:')
        einkaufsliste.remove(item)
        print(einkaufsliste)
    elif aktion == 'Auflisten':
        print(einkaufsliste)