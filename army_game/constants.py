
CIVILIZATIONS = {
    'Chinese': {
        'Arquer': 2,
        'Pikeman': 25,
        'Chivalry': 2,
    },
    'English': {
        'Arquer': 10,
        'Pikeman': 10,
        'Chivalry': 10,
    },
    'Byzantine': {
        'Arquer': 5,
        'Pikeman': 8,
        'Chivalry': 15,
    }
}

BRANCH_POINTS = {
    'Arquer': 5,
    'Pikeman': 10,
    'Chivalry': 20,
}

BRANCH_TO_LEVEL = {
    'Arquer': 1,
    'Pikeman': 2,
    'Chivalry': 3,
}

LEVEL_TO_BRANCH = {
    1: 'Archer',
    2: 'Pikeman',
    3: 'Chivalry',
}

TRAINING_FORCE_POINTS_COST = {
    'Arquer': {'points': 3, 'cost': 10},
    'Pikeman': {'points': 7, 'cost': 20},
    'Chivalry': {'points': 10, 'cost': 30},
}

TRASFORMATION_BRANCH_COST = {
    2: 30,
    3: 40,
}

TOTAL_COINS_FOR_BATTLE_WON = 100
