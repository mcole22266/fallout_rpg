# Gun.py
# Michael Cole <mcole042891.prof.dev@gmail.com>
#
# Gun Model
# -----------------------------------------------

class Gun:

    def __init__(self, name, ammoType, weaponType, dr, effects, dt, fr, range, qualities, weight, cost, rarity, description):
        self.name = name
        self.ammoType = ammoType
        self.weaponType = weaponType
        self.dr = dr
        self.effects = effects
        self.dt = dt
        self.fr = fr
        self.range = range
        self.qualities = qualities
        self.weight = weight
        self.cost = cost
        self.rarity = rarity
        self.description = description
