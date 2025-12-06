#!/usr/bin/env python3

import json # 10. pdf: JSON modul

def adat_irasa():
    film = {
        "cim": "Inception",
        "ev": 2010,
        "szereplok": ["DiCaprio", "Page", "Hardy"]
    }
    
    # 10. pdf: Fájlba írás JSON formátumban
    with open("film.json", "w") as f:
        json.dump(film, f, indent=4) # indent a szép formázáshoz

def adat_olvasasa_es_modositasa():
    try:
        with open("film.json", "r") as f:
            adat = json.load(f) # 10. pdf: JSON betöltése
            
        adat['cim'] += " - Rendezői változat"
        return adat
    except FileNotFoundError:
        return "Nincs meg a fájl!"




def main():
    adat_irasa()
    print(adat_olvasasa_es_modositasa())

##############################################################################

if __name__ == "__main__":
    main()