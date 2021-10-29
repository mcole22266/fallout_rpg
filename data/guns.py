# guns.py
# Michael Cole <mcole042891.prof.dev@gmail.com>
#
# List of all guns in the game
# ---------------------------------------------

from models.Gun import Gun

gunList = [
    Gun(
        name='.44 Pistol',
        ammoType='.44 Magnum',
        weaponType='Small Guns',
        effects='Vicious',
        dt='Physical',
        fr=1,
        range='C',
        qualities=['Close Quarters'],
        weight=4,
        cost=99,
        rarity=2,
        description=""
    ),
    Gun(
        name='10mm Pistol',
        ammoType='10mm',
        weaponType='Small Guns',
        effects=None,
        dt='Physical',
        fr=2,
        range='C',
        qualities=['Close Quarters', 'Reliable'],
        weight=4,
        cost=50,
        rarity=1,
        description=""
    ),
]
