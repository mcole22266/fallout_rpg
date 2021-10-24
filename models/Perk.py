class Perk:

    def __init__(self, name, numRanks, requirements, description):
        self.name = name
        self.numRanks = numRanks
        self.requirements = requirements
        self.description = description

        self.currentRank = 0

    def increaseRanks(self):
        if self.numRanks - self.currentRank >= 1:
            self.currentRank += 1
        else:
            print('[WARNING]: Max number of ranks reached.')
