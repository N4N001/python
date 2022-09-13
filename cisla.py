cisla=[12,75,150,180,145,525]
cisla5=0
cisla149=0
for num in cisla:
    if num>150:
        continue
    if num %5==0:
        print(num)
print("")
input("Stiskni klávesu ENTER pro ukončení programu")