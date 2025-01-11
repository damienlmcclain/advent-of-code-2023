import math
from typing import Dict, List

from aoc2023.utils import parse_input


def create_cube_dict(input_data: List[str]) -> Dict[int, Dict[str, int]]:
    """
    Returns the given str parsed into a dict of game number to a dict of the maximum number of cubes of each
    color were revealed in a game.

    Parameters
    ----------
    input_data
        A list of str where each str is the draw information for each game.

    Returns
    -------
    The input data broken down into a dict of
        {game number: {color name: number drawn of that color}}
    """
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


def determine_possible_games(max_of_each_color: Dict[str, int],
                             sum_or_product: str,
                             day: int = None,
                             year: int = None,
                             session_cookie: str = None,
                             filename: str = None) -> int or str:
    """
    Takes in a str via various inputs and determines how many games are
    possible given the maximum number of colors per draw.

    Parameters
    ----------
    max_of_each_color
        The maximum number of each color that can be drawn in a single draw.
    sum_or_product
        Whether to add or multiply the passing games.
    day
        The day to pull data for.
    year
        The year to pull data for.
    session_cookie
        The AOC session cookie for pulling data.
    filename
        If input, the name of the file to parse instead of pulling data using
        the day/year.

    Returns
    -------
    A str if there is an error with the inputs or
        an int of the sum of the number of each passing games if sum_or_product
        is set to sum or
        an int of the product of the maximum number of color cubes
        for each game

    """

    massaged_inputs = parse_input(day=day,
                                  year=year,
                                  session_cookie=session_cookie,
                                  filename=filename)
    color_dict = create_cube_dict(input_data=massaged_inputs)

    games_total = 0
    for game_num, color_info in color_dict.items():
        if sum_or_product == 'sum':
            game_passes = True
            for color, max_in_game in color_info.items():
                if max_in_game > max_of_each_color[color]:
                    # if any are greater than the max, the game is impossible
                    game_passes = False
                    break
            if game_passes:
                games_total += game_num
        elif sum_or_product == 'product':
            games_total += math.prod(color_info.values())

    return games_total
