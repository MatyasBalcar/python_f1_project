"""
Module for printing information in formated w ay
"""

def print_laps(laps):
    """
    :param laps:
    :return: nothing
    """
    # Iterating over the DataFrame and printing each row in a formatted manner
    for idx, row in laps.iterrows():
        print(f"Lap {idx + 1}: Time = {row['LapTime']}, Driver = {row['Driver']}")

