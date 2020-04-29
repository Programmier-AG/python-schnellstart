name = input("Dein Name: ")
alter = int(input("Dein Alter: "))

if alter > 29:
    print("Du musst jünger als 30 Jahre sein.")
elif alter < 18:
    print("Du musst mindestens 18 Jahre alt sein.")
else:
    print("--------------------------------------")
    print("Willkommen, "+name)
    print("In einem Jahr bist du: " + str(alter+1))
    print("In 2 Jahren bist du:   " + str(alter+2))
    print("In 3 Jahren bist du:   " + str(alter+3))
    print("--------------------------------------")
