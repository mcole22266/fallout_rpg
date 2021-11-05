class Origin:

    def __init__(self):
        self.name = None
        self.description = None
        self.trait = {
            'name': None,
            'description': None
        }
        self.character = None

    def attach(self, character):
        self.character = character


class VaultDweller(Origin):

    def __init__(self):
        self.name = 'Vault Dweller'
        self.description = ''
        self.trait = {
            'name': 'Vault Kid',
            'description': 'Your healthier start to life at the hands of trained doctors and sophisticated auto-docs means you reduce the difficulty of all END tests to resist the effects of disease. In addition, your carefully-planned upbringing means you have one additional tag skill of your choice.'
        }

    def attach(self, character):
        self.character = character


origin_list = [
    VaultDweller()
]
