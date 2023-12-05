import pdb
import json

with open ("data.txt","r") as my_file:
    lines = my_file.readlines()

    all_games = dict()
    game_id_sum = 0
    

    for line in lines:
        skip_game = False
        game_id = line.split(":")[0].split()[1]
        game_sets = line.split(":")[1].strip().split(";")

        all_games[game_id] = {}

        set_counter = 0

        for game_set in game_sets:
            for item in game_set.split(","):
                item_count = 0
                amount_of_sets = len(game_set.split(","))

                number = int(item.split()[0])
                color = item.split()[1]

                all_games[game_id][item_count] = dict()                
                all_games[game_id][item_count][color] = number

                if color == "red" and number > 12 or color == "green" and number > 13 or color == "blue" and number > 14:
                    skip_game = True
                    break

                item_count += 1

        if skip_game:            
            continue
        else:
            game_id_sum += int(game_id)

        
print(json.dumps(all_games, indent=4))
print()
print()
print("Sum: ", game_id_sum)



