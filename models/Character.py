# Character.py
# Michael Cole <mcole042891.prof.dev@gmail.com>
#
# Character Model
# -----------------------------------------------

class Character:

    def __init__(self, name, lvl=1):
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

    def setDerivedStatistics(self):
        self.carry_weight = 150 + (self.strength * 10)
        self.initiative = self.perception + self.agility
        self.defense = 2 if self.agility >= 9 else 1
        self.damage_resistance = 0
        self.hp_max = self.endurance + self.luck
