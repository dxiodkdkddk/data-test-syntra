#!/usr/bin/env python3
"""
Mastermind 
==========
- 6 pionkleuren
- Code bestaat uit4 pionnen met elk zijn pionkleur, herhaling pionkleuren toegestaan
- 12 gok pogingen
- returnk:
    'X' = juiste pionkleur / juiste plaats
    'O' = juiste pionkleur / verkeerde plaats
    '_' = verkeerde pionkleur
"""

import random
import webbrowser

def genereer_code(codeLengte=4, aantalVerschillendeKleuren=6):
    #returns lijst van kleuren int [1,1,1,1]    
    
    return [random.randint(1, aantalVerschillendeKleuren) for _ in range(codeLengte)]

def read_poging(codeLengte=4, aantalVerschillendeKleuren=6):
    #returns lijst van kleuren int [1,1,1,1]
    
    while True:
        invoer = input(f"Geef uw code ({codeLengte} cijfers tussen 1 en {aantalVerschillendeKleuren}), \
ex '1111' of 'help' voor uitleg over het spel\n> ").strip()

        if invoer == "help":
            help_mastermind()
            continue

        #lengte moe kloppen
        if len(invoer) != codeLengte:
            print(f"Dju: je moet exact {codeLengte} cijfers ingeven. Probeer opnieuw.")
            continue

        #moeten allemaal cijfers zijn tussen 1 en aantalVerschillendeKleuren
        pogingGeldig = True
        poging = []
        for kleur in invoer:
            if kleur.isdigit():
                waarde = int(kleur)
                if 1 <= waarde <= aantalVerschillendeKleuren:
                    poging.append(waarde)
                else:
                    pogingGeldig = False
                    break
            else:
                pogingGeldig = False
                break
        if not pogingGeldig:
            print(f"Dju: alleeen cijfers 1 t.e.m. {aantalVerschillendeKleuren}. Probeer opnieuw.")
            continue
        return poging
    return None

def bereken_resultaat(code, poging):
    """
    Bereken het aantal X en O.
        - X: juiste kleur + juiste plaats
        - O: juiste kleur + verkeerde plaats
        retourneert (X, O)
    """
    lengte = len(code)

    
    
    aantalX = 0
    positiesGebruikt = [False] * lengte   # markeer welke posities al gebruikt zijn
    positiesX = [False] * lengte # markeer welke posities al als X geteld zijn

    for i in range(lengte):
        if poging[i] == code[i]:#  X (exacte matches op positie)
            aantalX += 1
            positiesGebruikt[i] = True
            positiesX[i] = True

    aantalO = 0
    for i in range(lengte):
        if positiesX[i]:
            continue  # deze was al X
        kleurIn = poging[i]
        # zoek in de code een niet-gebruikte positie met dezelfde kleur
        for j in range(lengte):
            if not positiesGebruikt[j] and code[j] == kleurIn:# O (juiste kleur, verkeerde positie)
                aantalO += 1
                positiesGebruikt[j] = True  # markeer die code-pin als gebruikt
                break  # ga naar volgende poging-pin

    return aantalX, aantalO

def speel_spel():
    LENGTE = 4
    KLEUREN = 6
    MAX_POGINGEN = 12

    geheimeCode = genereer_code(LENGTE, KLEUREN)
    #print("[DEBUG] Geheime code:", geheimeCde)

    for pogingNr in range(1, MAX_POGINGEN + 1):
        print(f"Poging {pogingNr} van {MAX_POGINGEN}")
        poging = read_poging(LENGTE, KLEUREN)
        if poging is None:  # help opgeroepen
            return
        aantalX, aantalO = bereken_resultaat(geheimeCode, poging)
        print(f"zwart: {aantalX} | wit: {aantalO}\n")

        if aantalX == LENGTE:
            print("Proficiat! Ge zijt ne slimmme gij!")
            break
    else:
        print("Uw pogingen zijn op, de code was:", "".join(str(x) for x in geheimeCode))


def help_mastermind():
    url = "https://nl.wikipedia.org/wiki/Mastermind"
    try:
        success = webbrowser.open(url)
        if not success:
            raise Exception("Browser issue")
    except Exception:
        print(f"browser probleem, copy/paste {url} om toch te zien\n")
        return None
    
if __name__ == "__main__":
    speel_spel()

