from random import randint

def rollDice(numSides=20, numDice=1, modifier=0):
    total = 0
    for _ in range(numDice):
        total += randint(1, numSides)
    
    return total + modifier
