import random
import requests
import json

baseUrl = 'https://pokeapi.co/api/v2/pokemon'
pickerParameters = {'offset': '0', 'limit': '1025'}

response = requests.get(baseUrl, params=pickerParameters)
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

#generation
print("Generation: ")
if randomNumber <= 151:
    print("1")
elif randomNumber <= 251:
    print("2")
elif randomNumber <= 386:
    print("3")
elif randomNumber <= 493:
    print("4")
elif randomNumber <= 649:
    print("5")
elif randomNumber <= 722:
    print("6")
elif randomNumber <= 809:
    print("7")
elif randomNumber <= 905:
    print("8")
else:
    print("9")

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
