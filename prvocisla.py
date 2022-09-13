lower_value = 1
upper_value = int(input ("Zadejte nejvyšší hodnotu čísla: "))    
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  
input("Stiskni klávesu ENTER pro ukončení programu")