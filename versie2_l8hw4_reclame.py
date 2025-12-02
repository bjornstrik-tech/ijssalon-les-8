from L8hw1_algemene_functies import mijn_functie_2
def aanbieding_1(smaak,prijs,korting):# l8hw5 niet helemaal de waarom en hoe van de opdracht maar hopelijk klopt dit
    prijs_na_korting = prijs *(1-korting)
    uitvoer = f"vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak{smaak},van {prijs},euro voor {prijs_na_korting} euro."
    return uitvoer
print(aanbieding_1(smaak ="aarbei",prijs=4,korting=0.1)) # print test van L8hw5


def inkomsten_totaal(*inkomsten):#L8hw6
    totaal_inkomsten = sum(inkomsten)
    btw = 0.09
    btw = totaal_inkomsten * btw #L8hw7
    return"het totaal van alle inkomsten van deze week in", totaal_inkomsten,"euro","waarover", btw, "euro btw betaald dient te worden"
print (inkomsten_totaal(220,430,125,160,205,90,345))


def laag_en_hoog(*mijn_lijst):#L8hw8
    hoogst_verdiend_bedrag = max(mijn_lijst)
    laagst_verdiend_bedrag = min(mijn_lijst)
    return"hoogst verdiend bedrag =", hoogst_verdiend_bedrag,"laagst verdiend bedrag =", laagst_verdiend_bedrag
print (laag_en_hoog(220,430,125,160,205,90,345))


def gemiddelde(*mijn_lijst):#L8hw9
    totaal = sum(mijn_lijst)
    lengte = len(mijn_lijst)
    gemiddelde = totaal / lengte
    return"De gemiddelde inkomsten van deze week zijn", gemiddelde,"euro"#L8Hw10
print (gemiddelde(220,430,125,160,205,90,345))

def meervoudig(*invoer_lijst):#L8hw11, uitvoer is niet zoals het hoort wat gaat fout?
    meervoudig = laag_en_hoog(invoer_lijst)
    return meervoudig
print(meervoudig(10,5,3,2,1,2,9))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer= mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer


