def parse_input(filename):
    with open(filename, encoding='utf-8') as file:
        input_data = file.read().split('\n')
    parsed_data_dict = {}
    for game_str in input_data:
        # find the game number
        game_idx = int(game_str.split(':')[0].split(' ')[1])
        # figure out the different draws
        draws = game_str.split(':')[1].split(';')
        # remove the leading whitespace
        draws = [draw.lstrip() for draw in draws]
        draw_dict = {'blue': 0, 'red': 0, 'green': 0}
        for draw in draws:
            different_colors = draw.split(',')
            different_colors = [color.lstrip() for color in different_colors]
            for color in different_colors:
                color_name = color.split(' ')[1]
                color_number = int(color.split(' ')[0])
                if draw_dict[color_name] < color_number:
                    draw_dict[color_name] = color_number
        parsed_data_dict[game_idx] = draw_dict
    return parsed_data_dict


def return_possible_games(parsed_inputs, requirements):
    possible_games = []
    for game_idx, max_color_cubes in parsed_inputs.items():
        had_to_break = False
        for color, number in max_color_cubes.items():
            if number > requirements[color]:
                had_to_break = True
                break
        # if it didn't have to break, it must be good
        if had_to_break is False:
            possible_games.append(game_idx)
    return possible_games


def sum_possible_games(possible_games):
    game_sum = 0
    for game in possible_games:
        game_sum += game
    return game_sum


def return_powers(parsed_inputs):
    summed_powers = 0
    for min_color_cubes in parsed_inputs.values():
        summed_powers += min_color_cubes['blue'] * min_color_cubes['red'] * min_color_cubes['green']
    return summed_powers


requirements = {'blue': 14, 'red': 12, 'green': 13}
parsed_input = parse_input('tests/fixtures/day_02_input.txt')
possible_games = return_possible_games(parsed_input, requirements)
game_sum = sum_possible_games(possible_games)
print(f'The answer to day two, part one is {game_sum}')

total_powers = return_powers(parsed_input)
print(f'The answer to day two, part two is {total_powers}')

