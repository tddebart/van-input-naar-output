croissantHoeveelheid = int(input("Hoeveel croissants: "))
croissantPrijs = int(input("Croissant prijs in centen: "))/100
stockbroodHoeveelheid = int(input("Hoeveel stokbroden: "))
stockbroodPrijs = int(input("Stockbrood prijs in centen: "))/100
bonnenHoeveelheid = int(input("Hoeveel kortings bonnen: "))
bonnenKorting = int(input("Korting in centen: "))/100

volledigePrijs = (croissantHoeveelheid*croissantPrijs+stockbroodHoeveelheid*stockbroodPrijs-bonnenHoeveelheid*bonnenKorting)

print("De feestlunch kost je bij de bakker " + str(volledigePrijs) + " euro voor de " + str(croissantHoeveelheid) + " croissantjes en de " + str(stockbroodHoeveelheid) + " stokbroden als de " + str(bonnenHoeveelheid) + " kortingsbonnen nog geldig zijn!")
print(volledigePrijs)

