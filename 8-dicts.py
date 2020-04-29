"""
name = {
    "key": "value"
}
"""

zutaten = {
    "mehl": "300 Gramm",
    "zucker": "100 Gramm",
    "salz": "1 Esslöffel"
}

# Wie viel Mehl brauchen wir?
print("------------------")
print(zutaten["mehl"])
print("------------------")

# Alle "Keys" in einem Array
print(zutaten.keys())
print("------------------")

# Alle "Values" in einem Array
print(zutaten.values())
print("------------------")

# Durchgehen aller Elemente der Dict mit einer for
for zutat in zutaten:
    print("Du brauchst " + zutaten[zutat] + " " + zutat + ".")