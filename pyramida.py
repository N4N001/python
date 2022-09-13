rows = int(input("Zadej počet pater pyramidy: "))
for x in range(1, rows + 1):
    for y in range(1, x + 1):
        print(y, end=' ')
    print('')
input("Stiskni klávesu ENTER pro ukončení programu")