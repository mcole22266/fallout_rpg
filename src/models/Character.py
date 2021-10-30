# Character.py
# Michael Cole <mcole042891.prof.dev@gmail.com>
#
# Character Model
# -----------------------------------------------

from src.helpers.persistance import save_object, load_object


class Character:

    def __init__(self, name=None, lvl=1):
        self.name = name
        self.lvl = lvl
        self.origin = None
        self.perks = []
        self.traits = []

        # S.P.E.C.I.A.L. (default=5 as stated in rules)
        self.strength = 5
        self.perception = 5
        self.endurance = 5
        self.charisma = 5
        self.intelligence = 5
        self.agility = 5
        self.luck = 5

        # Skills
        self.athletics = 0
        self.barter = 0
        self.big_guns = 0
        self.energy_weapons = 0
        self.explosives = 0
        self.lockpick = 0
        self.medicine = 0
        self.melee_weapons = 0
        self.pilot = 0
        self.repair = 0
        self.science = 0
        self.small_guns = 0
        self.sneak = 0
        self.speech = 0
        self.survival = 0
        self.throwing = 0
        self.unarmed = 0
        self.tagged_skills = []

        # Derived Statistics
        self.setDerivedStatistics()

        # Persistence
        self.generateSavedCharacterFilename()

    def generateSavedCharacterFilename(self):
        self.saveLocation = f'./src/data/saved_data/characters/{self.name}.pkl'

    def setDerivedStatistics(self):
        self.carry_weight = 150 + (self.strength * 10)
        self.initiative = self.perception + self.agility
        self.defense = 2 if self.agility >= 9 else 1
        self.damage_resistance = 0
        self.hp_max = self.endurance + self.luck

    def saveCharacter(self):

        self.generateSavedCharacterFilename()
        save_object(self, self.saveLocation)
        print(f'Character {self.name} saved successfully')

    def loadCharacter(self, charName=None):
        if not charName:
            charName = self.name
        if not self.name:
            self.name = charName

        self.generateSavedCharacterFilename()
        object = load_object(self.saveLocation)

        # Assign current characters attributes to match the loaded character
        self.name = object.name
        self.lvl = object.lvl
        self.origin = object.origin
        self.perks = object.perks
        self.traits = object.traits

        # S.P.E.C.I.A.L. (default=5 as stated in rules)
        self.strength = object.strength
        self.perception = object.perception
        self.endurance = object.endurance
        self.charisma = object.charisma
        self.intelligence = object.intelligence
        self.agility = object.agility
        self.luck = object.luck

        # Skills
        self.athletics = object.athletics
        self.barter = object.barter
        self.big_guns = object.big_guns
        self.energy_weapons = object.energy_weapons
        self.explosives = object.explosives
        self.lockpick = object.lockpick
        self.medicine = object.medicine
        self.melee_weapons = object.melee_weapons
        self.pilot = object.pilot
        self.repair = object.repair
        self.science = object.science
        self.small_guns = object.small_guns
        self.sneak = object.sneak
        self.speech = object.speech
        self.survival = object.survival
        self.throwing = object.throwing
        self.unarmed = object.unarmed
        self.tagged_skills = object.tagged_skills

        # Derived Statistics
        self.setDerivedStatistics()
