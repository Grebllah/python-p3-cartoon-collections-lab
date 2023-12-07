def roll_call_dwarves(names):
    index = 0
    for name in names:
        order_number = 1 + index
        print(f"{order_number}. {name}")
        index = order_number

def summon_captain_planet(calls):
    captain_planet = [f"{call.title()}" + "!" for call in calls]
    return captain_planet

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) < 5:
            pass
        elif len(call) > 4:
            return True
    return False

def find_the_cheese(snacks):
    ingredients = ["cheddar", "gouda", "camembert"]
    for ingredient in snacks:
        if ingredient in ingredients:
            return ingredient
    return None
