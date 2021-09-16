zahl = 0

# Auf 'while' folgt eine Bedinung, wie bei 'if' auch.
# Da eine Bedingung erfüllt oder nicht erfüllt sein kann, kann man auch gleich True oder False (Boolean) angeben.
# So ist 'while True:' also eine unendlich lange Schleife.
while True:
    # Erhöht die Zahl um 1.
    zahl += 1
    # Gibt die Zahl aus.
    print(zahl)

# Die oben stehende Schleife muss auskommentiert werden, sonst kommt das Programm nicht weiter.

gutes_wetter = True

# Solange es wahr ist, dass das Wetter gut ist, läuft diese Schleife.
# Sobald guttes_wetter auf 'False' steht, stoppt die Schleife.
while gutes_wetter == True:
    # Erhöht die Zahl um 1.
    zahl += 1
    # Gibt die Zahl aus.
    print(zahl)
    # Wenn die Zahl Größer als 15 wird, wird das Wetter schlecht (guttes_wetter = False)
    if zahl > 15:
        gutes_wetter = False
        print("Das Wetter ist nun schlecht.")
    