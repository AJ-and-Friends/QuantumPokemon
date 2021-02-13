import requests
import import_ipynb
import Pokedex as pd
import sys
from flask import Flask, render_template
import os

pokedex = pd.getPokemon()
typeList = pd.getTypeList()

typeAtt = input('Enter Type:').lower()

print(pd.score(typeAtt, pokedex['gengar']))

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

app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template(
        "index.html"
    )
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)