# Thomas de Bart pizzaCalculator

# zet standaart vaste prijzen
prijsSmall = 5.45
prijsMedium = 7.50
prijsLarge = 9.23

print("Welkom bij de pizza calculator")

# vraag voor hoeveel heid pizza's van verschillende maten
hoeveelheidSmall = input("Hoeveel small pizza's wil je?: ")
hoeveelheidMedium = input("Hoeveel medium pizza's wil je?: ")
hoeveelheidLarge = input("Hoeveel large pizza's wil je?: ")

# zeg hoeveel er is gekozen en hoeveel het kost
print("Je hebt gekozen voor {} small pizza's, {} medium pizza's en {} large pizza's".format(hoeveelheidSmall, hoeveelheidMedium, hoeveelheidLarge))
totaalprijs = float(hoeveelheidSmall)*prijsSmall+float(hoeveelheidMedium)*prijsMedium+float(hoeveelheidLarge)*prijsLarge
print("In totaal kost dat je: {} euro".format(totaalprijs))