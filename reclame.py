from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    korting_prijs = format(prijs * (1 - korting), ".2f")
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting_prijs} euro."

def inkomsten_totaal(inkomsten, btw):
    week_inkomsten = sum(inkomsten)
    btw_bedrag = week_inkomsten * btw
    return f"Het totaal van alle inkomsten van deze week is {week_inkomsten} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    hoog_laag_lijst = [max(mijn_lijst), min(mijn_lijst)]
    return hoog_laag_lijst

def gemiddelde(mijn_lijst):
    gemiddelde_bedrag = format(sum(mijn_lijst) / len(mijn_lijst), ".2f")
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_bedrag} euro."

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer