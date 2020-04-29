zutaten = ["Milch", "Zucker", "Mehl"]

# Für jede Zutat in dem Array Zutaten wird der Code ausgeführt.
# 'zutat' ist hierbei das entsprechende Element aus dem Array, das betrachtet wird.
for zutat in zutaten:
    # Wir geben die Zutat aus, um die es jetzt geht.
    print(zutat)
    # Wir können z. B. an jeden String in dem Array eine Zutat anhängen.
    print(zutat+" ist toll.")
    # Wir können die Zutat aus dem Array entfernen.
    zutaten.remove(zutat)

# Wird ausgeführt, sobald die Schleife zuende ist.
print(zutaten)