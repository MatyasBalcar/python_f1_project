"""
File for running the main program.
Author : Matyas Balcar
GitHub : https://github.com/MatyasBalcar'
"""
from data.get_data import *
from print.laps import *

session = get_and_load_session(2024,1,"Q")
laps = get_laps(session, 'VER', True)
print(get_maximum_speeds(session))
