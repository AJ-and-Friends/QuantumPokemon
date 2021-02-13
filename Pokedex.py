import numpy as np
import random

pokemon = {'bulbasaur': ['grass', 'poison'], 'ivysaur': ['grass', 'poison'], 'venusaur': ['grass', 'poison'], 'charmander': ['fire'], 'charmeleon': ['fire'], 'charizard': ['fire', 'flying'], 'squirtle': ['water'], 'wartortle': ['water'], 'blastoise': ['water'], 'caterpie': ['bug'], 'metapod': ['bug'], 'butterfree': ['bug', 'flying'], 'weedle': ['bug', 'poison'], 'kakuna': ['bug', 'poison'], 'beedrill': ['bug', 'poison'], 'pidgey': ['normal', 'flying'], 'pidgeotto': ['normal', 'flying'], 'pidgeot': ['normal', 'flying'], 'rattata': ['normal'], 'raticate': ['normal'], 'spearow': ['normal', 'flying'], 'fearow': ['normal', 'flying'], 'ekans': ['poison'], 'arbok': ['poison'], 'pikachu': ['electric'], 'raichu': ['electric'], 'sandshrew': ['ground'], 'sandslash': ['ground'], 'nidoran-f': ['poison'], 'nidorina': ['poison'], 'nidoqueen': ['poison', 'ground'], 'nidoran-m': ['poison'], 'nidorino': ['poison'], 'nidoking': ['poison', 'ground'], 'clefairy': ['fairy'], 'clefable': ['fairy'], 'vulpix': ['fire'], 'ninetales': ['fire'], 'jigglypuff': ['normal', 'fairy'], 'wigglytuff': ['normal', 'fairy'], 'zubat': ['poison', 'flying'], 'golbat': ['poison', 'flying'], 'oddish': ['grass', 'poison'], 'gloom': ['grass', 'poison'], 'vileplume': ['grass', 'poison'], 'paras': ['bug', 'grass'], 'parasect': ['bug', 'grass'], 'venonat': ['bug', 'poison'], 'venomoth': ['bug', 'poison'], 'diglett': ['ground'], 'dugtrio': ['ground'], 'meowth': ['normal'], 'persian': ['normal'], 'psyduck': ['water'], 'golduck': ['water'], 'mankey': ['fighting'], 'primeape': ['fighting'], 'growlithe': ['fire'], 'arcanine': ['fire'], 'poliwag': ['water'], 'poliwhirl': ['water'], 'poliwrath': ['water', 'fighting'], 'abra': ['psychic'], 'kadabra': ['psychic'], 'alakazam': ['psychic'], 'machop': ['fighting'], 'machoke': ['fighting'], 'machamp': ['fighting'], 'bellsprout': ['grass', 'poison'], 'weepinbell': ['grass', 'poison'], 'victreebel': ['grass', 'poison'], 'tentacool': ['water', 'poison'], 'tentacruel': ['water', 'poison'], 'geodude': ['rock', 'ground'], 'graveler': ['rock', 'ground'], 'golem': ['rock', 'ground'], 'ponyta': ['fire'], 'rapidash': ['fire'], 'slowpoke': ['water', 'psychic'], 'slowbro': ['water', 'psychic'], 'magnemite': ['electric', 'steel'], 'magneton': ['electric', 'steel'], 'farfetchd': ['normal', 'flying'], 'doduo': ['normal', 'flying'], 'dodrio': ['normal', 'flying'], 'seel': ['water'], 'dewgong': ['water', 'ice'], 'grimer': ['poison'], 'muk': ['poison'], 'shellder': ['water'], 'cloyster': ['water', 'ice'], 'gastly': ['ghost', 'poison'], 'haunter': ['ghost', 'poison'], 'gengar': ['ghost', 'poison'], 'onix': ['rock', 'ground'], 'drowzee': ['psychic'], 'hypno': ['psychic'], 'krabby': ['water'], 'kingler': ['water'], 'voltorb': ['electric'], 'electrode': ['electric'], 'exeggcute': ['grass', 'psychic'], 'exeggutor': ['grass', 'psychic'], 'cubone': ['ground'], 'marowak': ['ground'], 'hitmonlee': ['fighting'], 'hitmonchan': ['fighting'], 'lickitung': ['normal'], 'koffing': ['poison'], 'weezing': ['poison'], 'rhyhorn': ['ground', 'rock'], 'rhydon': ['ground', 'rock'], 'chansey': ['normal'], 'tangela': ['grass'], 'kangaskhan': ['normal'], 'horsea': ['water'], 'seadra': ['water'], 'goldeen': ['water'], 'seaking': ['water'], 'staryu': ['water'], 'starmie': ['water', 'psychic'], 'mr-mime': ['psychic', 'fairy'], 'scyther': ['bug', 'flying'], 'jynx': ['ice', 'psychic'], 'electabuzz': ['electric'], 'magmar': ['fire'], 'pinsir': ['bug'], 'tauros': ['normal'], 'magikarp': ['water'], 'gyarados': ['water', 'flying'], 'lapras': ['water', 'ice'], 'ditto': ['normal'], 'eevee': ['normal'], 'vaporeon': ['water'], 'jolteon': ['electric'], 'flareon': ['fire'], 'porygon': ['normal'], 'omanyte': ['rock', 'water'], 'omastar': ['rock', 'water'], 'kabuto': ['rock', 'water'], 'kabutops': ['rock', 'water'], 'aerodactyl': ['rock', 'flying'], 'snorlax': ['normal'], 'articuno': ['ice', 'flying'], 'zapdos': ['electric', 'flying'], 'moltres': ['fire', 'flying'], 'dratini': ['dragon'], 'dragonair': ['dragon'], 'dragonite': ['dragon', 'flying'], 'mewtwo': ['psychic'], 'mew': ['psychic']}

types = [       # Index
    "normal",   # 0
    "fire",     # 1
    "water",    # 2
    "electric", # 3
    "grass",    # 4
    "ice",      # 5
    "fighting", # 6
    "poison",   # 7
    "ground",   # 8
    "flying",   # 9
    "psychic",  # 10
    "bug",      # 11
    "rock",     # 12
    "ghost",    # 13
    "dragon"    # 14
]

typeEffectiveness = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1],
    [1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5,],
    [1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5],
    [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5],
    [1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5],
    [1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2],
    [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1],
    [1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1],
    [1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1],
    [1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1],
    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1],
    [1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1],
    [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
] 

moveWeightValues = {
    "normal":   10,
    "fire":     0.17,
    "water":    1.79,
    "electric": 3.85,
    "grass":    0.6,
    "ice":      7.78,
    "fighting": 0.01,
    "poison":   0,
    "ground":   4.62,
    "flying":   1.03,
    "psychic":  5.69,
    "bug":      0.12,
    "rock":     1.06,
    "ghost":    0,
    "dragon":   0
}

def getPokemon():
    return pokemon

def getType(name):
    return pokemon[name]

def getTypeList():
    return types

# def getTypeList(id): # return the row index in typeEffectiveness 
#     return types.index(id)

def getAtt(type):
    return typeEffectiveness[types.index(type)]

def getDef(type):
    return np.rot90(np.fliplr(typeEffectiveness))[types.index(type)]

import numpy as np
def dmgMult(typeAtt,typeDef):
    multi = 1
    typeAttInd = types.index(typeAtt)
    for x in typeDef:
        multi*=getDef(x)[typeAttInd]
    return multi

def score(typeAtt, typeDef):
    multi = dmgMult(typeAtt, typeDef)
    if multi == 4:
        return 2
    if multi == 2:
        return 1
    if multi == 1:
        return 0
    if multi == 0.5:
        return -1
    if multi == 0.25:
        return -2
    if multi == 0:
        return -3

# def teamBuilder(p1, p2, p3, p4, p5, p6):
    
def randomTeam():
    ranTeam = []
    for i in range(6):
        cur = random.choice(list(pokemon))
        if cur in ranTeam:
            i -=1
        else:
            ranTeam.append(cur)
    return ranTeam    

