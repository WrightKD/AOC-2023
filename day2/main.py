data = open('input.txt')
games_converted = []


def validate_color_count(color, game_sets, allowed_count):
    found = 0

    for game_set in game_sets:
        if color in game_set:

            if game_set[color] > allowed_count:
                print(color, game_set[color] )
                return False 

            # found += game_set[color]
            # if found > allowed_count:
            #     print(color, found)
            #     return False
                
    return True


for line in data:
    line = line.rstrip()
    game = line.split(': ')
    game_sets = game[1].split('; ')

    games_converted_sets = []

    for game_set in game_sets:
        rs = {}
        for r in game_set.split(', '):
            rx = r.split(' ')
            rs[rx[1]] = int(rx[0])

        games_converted_sets.append(rs)

    log_game = {game[0] : games_converted_sets, 'game_value' : int(game[0].split(' ')[1])}
    games_converted.append(log_game)


correct_game_count = 0

for game in games_converted:
    game_key = f"Game {game['game_value']}"

    total_red = sum([x['red'] if 'red' in x else 0 for x in game[game_key]])
    total_green = sum([x['green'] if 'green' in x else 0 for x in game[game_key]])
    total_blue = sum([x['blue'] if 'blue' in x else 0 for x in game[game_key]])

    game['total_red'] = total_red
    game['total_green'] = total_green
    game['total_blue'] = total_blue

    any_invaild_red = [x['red'] <= 12 if 'red' in x else True for x in game[game_key]]
    any_invaild_green = [x['green'] <= 13 if 'green' in x else True for x in game[game_key]]
    any_invaild_blue = [x['blue'] <= 14 if 'blue' in x else True for x in game[game_key]]

    game['invaild_red'] = not all(any_invaild_red)
    game['invaild_green'] = not all(any_invaild_green)
    game['invaild_blue'] = not all(any_invaild_blue)

    max_red = max([x['red'] if 'red' in x else 0 for x in game[game_key]])
    max_green = max([x['green'] if 'green' in x else 0 for x in game[game_key]])
    max_blue = max([x['blue'] if 'blue' in x else 0 for x in game[game_key]])

    game['max_red'] = max_red
    game['max_green'] = max_green
    game['max_blue'] = max_blue

    game['power'] = max_blue * max_green * max_red

    # if game['invaild_red'] or game['invaild_green'] or game['invaild_blue']:
    #     pass
    # else:
    #     correct_game_count+=game['game_value']
    #     print(game, correct_game_count)

    correct_game_count+=game['power'] 
    print(game, correct_game_count)   
         