# Funktionen in Python

"""
    Struktur von Funktionen:

    def name(parameter1, parameter2):
        etwas_machen()
        # 'return' kehrt zum Prozess vor der Funktion zurück.
        return

"""


# 1. Eine Funktion definieren
# Ziel: Eine Funktion, die einen Nutzer begrüßen kann.
def sage_hallo(vorname):
    print("Hallo, ", vorname, "!")

# Ziel der nächsten Funktion: Eine Funktion, die zwei Zahlen addieren kann.
def addieren(zahl1, zahl2):
    print("Addiere Zahlen...")
    # Ergebnis zurückgeben
    return zahl1 + zahl2

# Funktion ausführen und Nutzer "Max" begrüßen.
sage_hallo("Max")

# Funktion erneut ausführen, aber einen anderen Nutzer begrüßen.
sage_hallo("Tom")

# Zwei Zahlen miteinander addieren.
ergebnis = addieren(1, 5)
print(ergebnis)