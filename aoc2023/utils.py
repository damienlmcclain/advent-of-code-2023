import aocd
import os
from typing import List


def parse_input(day: int = None,
                year: int = None,
                session_cookie: str = None,
                filename: str = None) -> List[str] or str:
    """
    Intakes a str of game information and returns it as a list of strs.

    Parameters
    ----------
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
    A list of each line in the pulled data or file as a str.
    """

    if filename:
        with open(filename, encoding='utf-8') as file:
            input_data = file.read().split('\n')
    elif day and year and session_cookie:
        os.environ['AOC_SESSION'] = session_cookie
        data = aocd.get_data(day=day, year=year)
        input_data = data.split('\n')
    else:
        return 'Please enter a valid combination of inputs: either a ' \
               'filename to pull from locally or a day, year, and ' \
               'session_cookie.'
    return input_data
