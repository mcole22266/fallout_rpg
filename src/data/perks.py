# perks.py
# Michael Cole <mcole042891.prof.dev@gmail.com>
#
# List of all perks in the game
# ---------------------------------------------

from models.Perk import Perk

perksList = [
    Perk(
        name='Action Boy/Girl',
        numRanks=1,
        requirements=[],
        description="When you spend AP to take an additional major action, you do not suffer the increased skill test difficulty during your second action."
    ),
    Perk(
        name='Adamantium Skeleton',
        numRanks=3,
        requirements=['END 7', 'Level 1+'],
        description="When you suffer damage, the amount of damage needed to inflict a critical hit on you increases by your rank in this perk. For example, if you have one rank in this perk, you suffer a critical hit from 6 or more damage, rather than 5 or more. Each time you take this perk, the level requirement increases by 3."
    ),
    Perk(
        name='Andrenaline Rush',
        numRanks=1,
        requirements=['STR 7'],
        description="When your health is below its maximum value, you count your STR score as 10 for all purposes when attempting a STR-based skill test or melee attack"
    ),
    Perk(
        name='Animal Friend',
        numRanks=2,
        requirements=['CHA 6', 'Level 1+'],
        description="At rank 1, whenever a creature NPC with the Mammal, Lizard, or Insect keyword would attack you, roll 1 Combat Die: on any result other than an Effect, the creature chooses not to attack you, although it may still attack another character it can target. At rank 2, you can attempt a CHA + Survival test with a difficulty of 2 as a major action. If you succeed, the animal treats you as friendly and will attack anyone who attacks you. Mighty and Legendary animals are unaffected by this perk. Each time you take this perk, the level requirement increases by 5."
    ),
    Perk(
        name='Aquaboy/Aquagirl',
        numRanks=2,
        requirements=['END 5, Level 1+'],
        description="Water is your ally. At rank 1, you no longer take radiation damage from swimming in irradiated water, and you can hold your breath for twice as long as normal. At rank 2, enemies add +2 to the difficulty to tests to detect you while you are submerged underwater. Each time you take this perk, the level requirement increases by 3."
    ),
    Perk(
        name='Armorer',
        numRanks=4,
        requirements=['STR 5, INT6'],
        description="You can modify armor with armor mods. Each rank in this perk unlocks an additional rank of mods: rank 1 unlocks rank 1 mods, rank 2 unlocks rank 2 mods, etc. Each time you take this perk, the level requirement increases by 4."
    ),
    Perk(
        name='Awareness',
        numRanks=1,
        requirements=['PER 7'],
        description="When you take the Aim minor action at a target within Close range, you spot their weaknesses and can attack more efficiently. The next attack you make against that target gains the Piercing 1 damage effect, or improves the rating of any existing Piercing X damage effect by 1."
    ),
    Perk(
        name='Barbarian',
        numRanks=1,
        requirements=['STR 6'],
        description="Your physical Damage Resistance increases on all hit locations based on your STR. You do not gain this benefit while wearing Power Armor. STR 7-8: +1 physical DR. STR 9-10: +2 physical DR. STR 11+: +3 physical DR"
    ),
    Perk(
        name='Basher',
        numRanks=1,
        requirements=['STR 6'],
        description="When you make a melee attack by bashing with your gun, your attack gains the Vicious damage effect."
    ),
    Perk(
        name='Better Criticals',
        numRanks=1,
        requirements=['LCK 9'],
        description="When you inflict one or more points of damage to an enemy, you may spend 1 Luck Point to automatically inflict a critical hit, causing an injury."
    ),
    Perk(
        name='Big Leagues',
        numRanks=1,
        requirements=['STR 8'],
        description="When you make a melee attack with a two-handed melee weapon, the weapon gains the Vicious damage effect."
    ),
    Perk(
        name='Black Widow/Lady Killer',
        numRanks=1,
        requirements=['CHA 6'],
        description="The Black Widow Perk affects men and masculine characters, while the Lady Killer perk affects women and feminine characters -- they are otherwise identical. When you attempt a CHA-based skill test to influence a character of the chosen gender, you may re-roll 1d20. In addition, your attacks inflict +1 Combat Dice additional damage against characters of the chosen gender."
    ),
    Perk(
        name='Blacksmith',
        numRanks=3,
        requirements=['STR 6, Level 2+'],
        description="You can modify melee weapons with weapon mods. Each rank in this perk unlocks an additional rank of melee weapon mods: rank 1 unlocks rank 1 mods, rank 2 unlocks rank 2 mods, and rank 3 unlocks rank 3 mods. Each time you take this perk, the level requirement increases by 4."
    ),
    Perk(
        name='Blitz',
        numRanks=2,
        requirements=['AGI 9, Level 1+'],
        description="When you move into reach of an opponent and make a melee attack against them in one turn, you may re-roll one d20 on your attack. At rank 2, you also inflict +1 Combat Dice damage with that attack. Each time you take this perk, the level requirement increases by 3."
    ),
    Perk(
        name='Bloody Mess',
        numRanks=1,
        requirements=['LCK 6'],
        description="When you inflict a critical hit, roll 1 Combat Dice; if you roll an Effect, you inflict one additional injury to a random location."
    ),
    Perk(
        name='Can Do!',
        numRanks=1,
        requirements=['LCK 5'],
        description="When you are scavenging a location that contains food, you gain 1 additional random food item, without spending AP."
    ),
    Perk(
        name='Cap Collector',
        numRanks=1,
        requirements=['CHA 5'],
        description="When you buy or sell items, you may increase or decrease the price of the goods being traded by 10%."
    ),
]
