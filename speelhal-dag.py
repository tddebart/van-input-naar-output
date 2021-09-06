toegangsTicketPrijs = int(input("Prijs toegang in centen: "))/100
aantalPersonen = int(input("Hoeveel personen: "))
lengteVR = int(input("Hoelang VR in minuten: "))
vrPrijs = int(input("Kosten VR in centen per 5 minuten: "))/100

volledigePrijs = aantalPersonen*toegangsTicketPrijs+(lengteVR/5)*vrPrijs*aantalPersonen

print("Dit geweldige dagje-uit met {} mensen in de Speelhal met {} minuten VR kost je maar {} euro".format(aantalPersonen, lengteVR, volledigePrijs))
print(volledigePrijs)
