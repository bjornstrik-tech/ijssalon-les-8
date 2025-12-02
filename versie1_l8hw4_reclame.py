def aanbieding_1(smaak,prijs,korting):# l8hw5 niet helemaal de waarom en hoe van de opdracht maar hopelijk klopt dit
    prijs_na_korting = prijs *(1-korting)
    uitvoer = f"vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak{smaak},van {prijs},euro voor {prijs_na_korting} euro."
    return uitvoer
print(aanbieding_1(smaak ="aarbei",prijs=4,korting=0.1)) # print test van L8hw5


def inkomsten_totaal(inkomsten):#L8hw6 totaal wordt met return gebracht naar inkomsten en uitgeprint
    maandag = 220
    dinsdag = 430
    woensdag = 125
    donderdag = 160
    vrijdag = 205
    zaterdag = 90
    zondag = 345
    totaal = maandag + dinsdag + woensdag + donderdag + vrijdag + zaterdag + zondag
    btw = 0.09#hw8les7L8hw7
    btw = totaal * btw
    return "het totaal van alle inkomsten van deze week = ",totaal, "waarover", btw, " euro btw betaald dient te worden"
print (inkomsten_totaal(0)) # de 0 moet er zijn omdat anders komt er niks uit


def laag_en_hoog(mijn_lijst):#L8hw8 gegeven van inkomsten in dictionary functie geplaatst waarvan de hoogste en laagst verdiende dag terugkome
    totaal_inkomsten = {
    "maandag" :220,
    "dinsdag" :430,
    "woensdag" :125,
    "donderdag": 160,
    "vrijdag" :205,
    "zaterdag" :90,
    "zondag": 345,
    } 
    totaal_inkomsten = "beste verdiende dag =", max(totaal_inkomsten),"slechts verdiende dag =",min(totaal_inkomsten)
    return totaal_inkomsten
print (laag_en_hoog(0))

def  gemiddelde(mijn_lijst):#L8hw9 gegeven van inkomsten in dictionary functie geplaatst waarvan het gemiddelde wordt weer gegeven
    maandag = 220
    dinsdag = 430
    woensdag = 125
    donderdag = 160
    vrijdag = 205
    zaterdag = 90
    zondag = 345
    totaal_inkomsten = maandag + dinsdag + woensdag + donderdag + vrijdag + zaterdag + zondag
    return "de gemiddelde inkomsten deze week zijn = ",totaal_inkomsten / 7#L8hw10
print (gemiddelde(0))
