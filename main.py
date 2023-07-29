import json


def get_money(wave, players, farms):
    wave_bonus = (180 + (50 * wave)) // players  # Fallen
    # wave_bonus = (180 + (100 * wave)) // players #Normal
    farms = [level[i][1] for i in farms]
    farm_bonus = sum(farms)
    all_bonus = wave_bonus + farm_bonus
    return all_bonus


player = 2
max_wave = 13
max_level = 5
max_farm = 8

level = {0: [250, 50], 1: [200, 100], 2: [550, 250], 3: [1000, 500], 4: [2500, 750], 5: [5000, 1500]}
highest = {"player": player, "difficulty": "Fallen", "money": 0, "wave": 0, "level": 0, "graph": None}


for current_wave in range(max_wave+1):
    for current_level in range(max_level):
        for current_farm in range(max_farm):
            money = 600
            farm = []
            graph = {i: {"first_money": 0, "money": 0, "spend": 0, "farm": []} for i in range(current_wave+1)}
            for w in range(current_wave+1):
                if w != 0:
                    money += get_money(w, player, farm)
                graph[w]["first_money"] = money

                if len(farm) < current_farm+1:  # place
                    for i in range((current_farm+1) - len(farm)):
                        if money >= 250:
                            farm.append(0)
                            money -= 250
                            graph[w]["spend"] -= 250

                else:  # upgrade
                    for j in range(current_farm+1):
                        for i in range(current_level+1):
                            if i in farm and money >= level[i][0]:
                                farm[farm.index(i)] += 1
                                money -= level[i+1][0]
                                graph[w]["spend"] -= level[i+1][0]
                graph[w]["money"] = money
                graph[w]["farm"] = farm.copy()

            if highest["money"] < money:
                highest["money"] = money
                highest["wave"] = current_wave
                highest["level"] = current_level+1
                highest["graph"] = graph


with open("data/farm.json", "w") as f:
    json.dump(highest, f, indent=4)
