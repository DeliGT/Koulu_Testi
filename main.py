from tuotelista import Tuotelista

varasto = Tuotelista()

while(True):
    valinta = int(input("1. Lisää tuote \n2. Poista tuote \n3. Tulosta tuotteet \n4. Muokkaa tuotetta \n5. Hae tuotetta \n0. Lopeta \n"))
    if( valinta == 0):
        break
    if( valinta == 1): 
        nimi = input("Anna tuotteen nimi:")
        hinta = float(input("Anna tuotteen hinta:"))
        maara = int(input("Anna tuotteen määrä:"))
        varasto.lisaaTuote(nimi,hinta,maara)
    if( valinta == 2):
        nimi = input("Anna poistettavan tuotteen nimi:")
        varasto.poistaTuote(nimi)
    if( valinta == 3):
        print(varasto.tulostaTuotteet())
    if( valinta == 4):
        vanhanimi = input("Anna tuotteen nykyinen nimi:")
        nimi = input("Anna tuotteen uusi nimi:")
        hinta = float(input("Anna tuotteen uusi hinta:"))
        maara = int(input("Anna tuotteen uusi määrä:"))
        varasto.muokkaaTuote(vanhanimi,nimi,hinta,maara)
    if( valinta == 5):
        haku = input("Anna haettavan tuotteen nimi:")
        print(varasto.haeTuote(haku))
print("Ohjelma loppui")