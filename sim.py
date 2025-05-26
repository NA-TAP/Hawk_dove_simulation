def reproduce(h, d, type):
    if type = hawk:
        h += 1
    if type = dove:
        d += 1
    return (h, d)

def calc_food_values(foodvalue, fightloss, foodgotten):
    return foodvalue * foodgotten - fightloss

def calc_chance_of_survival_and_reproduction(foodgottenvalue, reproductionneed, survivalneed):
    if foodgottenvalue >= reproductionneed:
        reproduce = True
        survive = True
    elif foodgottenvalue >= survivalneed:
        reproduce = False
        survive = True
    else:
        reproduce = False
        survive = False
    return (reproduce, survive)

def simstep(foodamt, foodvalue, h, d, fightloss):
    pass
