# Klasse / Objekt erstellen, das definiert,
# welche Attribute und Methoden
# ein Mensch(-Objekt in diesem Programm) hat.
class Mensch:
    # Jede Klasse hat eine Konstruktor-Funktion,
    # die immer ausgeführt wird, wenn eine Instanz erstellt wird.
    def __init__(self):
        print("Yay, ich lebe!")

# Instanz des Objekts erstellen
mensch = Mensch()

class Mensch2:
    def __init__(self):
        # Der Klasse Attribute geben,
        # welche in der ganzen Klasse und außerhalb verfügbar sind.
        self.name = "Herbert"
        self.alter = 42
        self.haarfarbe = "braun"
        self.augefarbe = "grün"

mensch2 = Mensch2()
print(mensch2.name + " ist " + str(mensch2.alter) + " Jahre alt.")

class Mensch3:
    # Die Attribute als Parameter der __init__ Funktion dynamisch einlesen
    def __init__(self, name, alter, haarfarbe, augenfarbe):
        self.name = name
        self.alter = alter
        self.haarfarbe = haarfarbe
        self.augefarbe = augenfarbe

mensch3 = Mensch3("Herbert", 44, "braun", "grün")
print(mensch3.name + " ist " + str(mensch3.alter) + " Jahre alt.")

class Mensch4:
    def __init__(self, name, alter, haarfarbe, augenfarbe):
        self.name = name
        self.alter = alter
        self.haarfarbe = haarfarbe
        self.augefarbe = augenfarbe
    
    # Dem Objekt (in diesem Fall ein Mensch) Methoden geben,
    # die das Programm ausführen kann, um es(/ihn) etwas machen zu lassen.
    def sprechen(self, text):
        print(self.name + " sagt: " + text)
    
    def lachen(self):
        print(self.name + " lacht...")
    
    def vorstellen(self):
        print("Hallo, ich bin " + self.name + "!")
        print("Ich bin " + str(self.alter) + " Jahre alt.")
        print("Meine Haare sind " + self.haarfarbe + " und meine Augen sind " + self.augefarbe + ".")


# Instanz erstellen und Methoden ausführen
mensch4 = Mensch4("Maria", 39, "blau", "braun")
mensch4.lachen()
mensch4.sprechen("Ich bin einer toller Text.")
mensch4.vorstellen()
# Mensch4.vorstellen() z. B. würde nicht gehen,
# da er keine individuelle Instanz ist.

# Mehrere Instanzen der eigenen Klasse erstellen
karl = Mensch4("Karl", 22, "blond", "braun")
rosa = Mensch4("Rosa", 34, "braun", "blau")
friedrich = Mensch4("Friedrich", 64, "grau", "braun")

# Attribute einzelner Klassen ausgeben
print(friedrich.alter, karl.alter)

# Methode einer bestimmten Instanz aufrufen
rosa.vorstellen()