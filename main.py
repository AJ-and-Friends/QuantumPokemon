import requests
import json
import import_ipynb
import Pokedex as pd
import sys

pokedex = pd.getPokemon()
typeList = pd.getTypeList()
randomTeam = pd.randomTeam()
randomTeam.sort()


myTeam = pd.teamBuilder()

typeAtt = input('Enter Type:')
for i in myTeam:
    print(i)
    print(pd.score(typeAtt,pokedex[i]))
    
typeAtt = input('Enter Type:')

for i in randomTeam:
    print(i)
    print(pd.score(typeAtt,pokedex[i]))

while True:
    try:
        cur = input("Enter Pokemon Name: ").lower()
        pd.getType(cur)
        break
    except KeyError:
        print("Try Again!")

for i in pd.getType(cur):
    print(cur,'is a:', i,'type pokemon')
    print('=================')
    print('Strengths:')
    x = 0
    for types in typeList:
        print('{:<10s}{:>4.1f}'.format(types, (pd.getAtt(i)[x])))
        x+=1
    x = 0
    print('=================')
    print('Defense:')
    for types in typeList:
        print('{:<10s}{:>4.1f}'.format(types, (pd.getDef(i)[x])))
        x+=1
