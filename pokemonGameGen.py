import random
import requests
import json

gen = int(input("Generation: "))

def pickfromGen(gen):
    genParams = []
    offsets = {
        1: [0, 151],
        2: [151, 99], 
        3: [251, 134],
        4: [386, 106], 
        5: [493, 155],
        6: [649, 72],
        7: [722, 86],
        8: [809, 95]
    }
    for genNumber, params in offsets.items():
        if gen == genNumber:
            for param in params:
                genParams.append(param)
    return genParams

baseUrl = 'https://pokeapi.co/api/v2/pokemon'
parameters = {'offset': pickfromGen(gen)[0], 'limit': pickfromGen(gen)[1]}

response = requests.get(baseUrl, params=parameters)
jsonContent = response.content
content = json.loads(jsonContent)
pokemonList = content["results"]

pokemonNames = []
pokemonNumbers = []

count = 0
for i in pokemonList:
    pokemonInfo = pokemonList[count]
    pokemonName = pokemonInfo["name"]
    pokemonNames.append(pokemonName)
    pokemonNumbers.append(count)
    count += 1

randomNumber = random.choice(pokemonNumbers)
randomPokemon = pokemonNames[randomNumber-1]

pokemonUrl = baseUrl + '/' + randomPokemon
response = requests.get(pokemonUrl)
jsonContent = response.content
content = json.loads(jsonContent)

print("")
print("Guess the Pokemon!")
print("")

def statFinder (category, categories):
    itemsList = content[categories]
    count = 0
    for i in itemsList:
        itemsInfo = itemsList[count]
        item = itemsInfo[category]
        itemName = item["name"]
        print(itemName)
        count += 1

#abilities
print("Abilities: ")

category = 'ability'
categories = 'abilities'
statFinder(category, categories)

print("")

#type
print("Type: ")

category = 'type'
categories = 'types'
statFinder(category, categories)

print("")

#guess
guessCount = 1
print("")
guess = str(input("Guess "+str(guessCount)+": "))
guess = guess.lower()
print("")

attempts = 5

while attempts > 0:
    if guess == randomPokemon:
        print("That is correct!")
        break
    else:
        attempts -= 1
        guessCount += 1
        if attempts == 0:
            print("youre a loser. the correct answer was "+randomPokemon)
            break
        else:
            print("That is so so wrong! You have " + str(attempts) + " attempts left.")
            print("")
            guess = str(input("Guess "+str(guessCount)+": "))