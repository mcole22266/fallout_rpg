# dice.py
# Michael Cole <mcole042891.prof.dev@gmail.com>
#
# Helper functions related to dice-rolling
# ---------------------------------------------

from random import randint


def rollDice(numSides=20, numDice=1, modifier=0):
    '''
    Simulate rolling dice.

    Params:
        numSides (int): Number of sides on the dice
        numDice (int): Number of dice to roll
        modifier (int): Number to add to the sum of
            all rolled dice.

    Returns:
        Total sum of all dice results with the modifier added
    '''
    total = 0

    # For each dice, add the result to the total
    for _ in range(numDice):
        total += randint(1, numSides)
    
    # Return with the modifier added
    return total + modifier


def skillTest(
    targetNumber, difficulty, dicePool=2,
    tagSkillNum=0, complicationsNum=20
):
    '''
    Perform a standard 2d20 system Skill Test

    Params:
        targetNumber (int): The number each d20 must roll equal
            or under to generate one success
        difficulty (int): The number of successes required to pass
            the test
        dicePool (int): The number of dice being rolled
        tagSkillNum (int): If the test is being performed on a tagged
            skill, all rolls under this number are critical successes
        complicationsNum (int): Allows modification of what roll constitutes
            a complication

    Returns:
        Dictionary mapping with attributes of the test
    '''
    skillTestResults = {
        # Parameters
        'targetNumber': targetNumber,
        'difficulty': difficulty,
        'dicePool': dicePool,
        'tagSkillNum': tagSkillNum,
        'complicationsNum': complicationsNum,

        'results': [],
        'successes': 0,
        'complications': 0,
        'passedTest': False
    }

    # Roll all dice
    skillTestResults['results'] = [rollDice(20) for _ in range(dicePool)]

    # Determine number of successes
    for dieRoll in skillTestResults['results']:
        # Check for critical successes
        #   CASE 1: Rolled 1 results in critical success
        if dieRoll == 1:
            skillTestResults['successes'] += 2
        #   CASE 2: Rolled 20 results in complication
        elif dieRoll == complicationsNum:
            skillTestResults['complications'] += 1
        #   CASE 3: Rolled under tagSkillNum results in critical success
        elif dieRoll <= tagSkillNum:
            skillTestResults['successes'] += 2
        #   CASE 4: Rolled equal or under targetNumber results in 1 success
        elif dieRoll <= targetNumber:
            skillTestResults['successes'] += 1
        #   CASE 5: Rolled above targetNumber results in nothing
        else:
            pass

    # Determine if pass the skill test
    if skillTestResults['successes'] >= difficulty:
        skillTestResults['passedTest'] = True

    # Return results
    return skillTestResults
