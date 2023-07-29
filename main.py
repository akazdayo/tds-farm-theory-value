def get_money(wave,players,farms):
    wave_bonus = (180 + (50 * wave)) / players #Fallen
    #wave_bonus = (180 + (100 * wave)) / players #Normal
    farms = [level[i][1] for i in farms]
    farm_bonus = sum(farms)
    all_bonus = wave_bonus + farm_bonus
    #print(all_bonus)
    return all_bonus


level = {0: [250,50],1:[200,100],2:[550,250],3:[1000,500],4:[2500,750],5:[5000,1500]}
player = 1
highest = {"money":0,"wave":0,"level":0,"graph":None}
"""
money = 600
farm = []

max_farm = 8
max_level = 5
max_wave = 13
"""

for max_wave in range(13):
    for max_level in range(5):
        for max_farm in range(8):
            money = 600
            farm = []
            graph = {i:{"money":0,"spend":0,"farm":[]} for i in range(max_wave+1)}
            for w in range(max_wave+1):
                money += get_money(w,player,farm)
                if len(farm) < max_farm+1: #place
                    for i in range((max_farm+1) - len(farm)):
                        if money >= 250:
                            farm.append(0)
                            money -= 250
                            graph[w]["spend"] -= 250
                            
                else: #upgrade
                    for j in range(max_farm+1):
                        for i in range(max_level+1):
                            if i in farm and money >= level[i][0]:
                                farm[farm.index(i)] += 1
                                money -= level[i][0]
                                graph[w]["spend"] -= level[i][0]
                graph[w]["money"] = money
                graph[w]["farm"] = farm
            
            if highest["money"] < money:
                highest["money"] = money
                highest["wave"] = max_wave+1
                highest["level"] = max_level+1
                #highest["graph"] = graph
                #print(max_wave+1,max_level+1 ,max_farm+1,money,farm,graph)
                #highest = {"money":0,"wave":0,"level":0,"graph":None}
                
                    
print(highest)
