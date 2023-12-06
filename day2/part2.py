import pdb
import json

with open ("data.txt","r") as my_file:
    lines = my_file.readlines()

    all_games = dict()    
    total_games = 0    

    for line in lines:        
        game_id = line.split(":")[0].split()[1]
        game_sets = line.split(":")[1].strip().split(";")

        all_games[game_id] = {}        
        all_games[game_id]["red"] = 0
        all_games[game_id]["blue"] = 0
        all_games[game_id]["green"] = 0

        for game_set in game_sets:  

            for item in game_set.split(","):
                
                amount_of_sets = len(game_set.split(","))

                number = int(item.split()[0])
                color = item.split()[1]

                if number > all_games[game_id][color]:
                    all_games[game_id][color] = number

             
        game_total = all_games[game_id]["red"] * all_games[game_id]["blue"] * all_games[game_id]["green"]                  
        total_games += game_total         

        
print(json.dumps(all_games, indent=4))
print()
print()
print("Total games sum: ", total_games)



