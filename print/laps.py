"""
Module for printing information in formated w ay
"""
import pandas as pd

def print_laps(laps):
    """
    :param laps:
    :return: nothing
    """
    for idx, row in laps.iterrows():
        lap_time = pd.to_timedelta(row['LapTime'])

        minutes = lap_time.components.minutes
        seconds = lap_time.components.seconds
        milliseconds = lap_time.components.milliseconds

        print(f"Lap {idx + 1}: Time = {minutes:02}:{seconds:02}.{milliseconds:03}, Driver = {row['Driver']}")

