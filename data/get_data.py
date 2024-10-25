"""
File for getting live data from the fastf1 api.
"""

import fastf1

def get_session(year,gp,ident):
    """
    :param year:
    :param gp:
    :param ident:
    :return: session [object]
    also loads the session
    """

    session = fastf1.get_session(year,gp,ident)
    session.load()
    return session

if __name__ == '__main__':
    print("This file should be imported, not ran separately")