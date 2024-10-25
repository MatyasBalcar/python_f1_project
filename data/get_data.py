"""
File for getting live data from the fast-f1 api.
"""

import fastf1


def get_and_load_session(year,gp,ident):
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


def get_drivers_list(session):
    """
    :param session:
    :return: drivers [list[ident]]
    """
    drivers = session.drivers
    return drivers


def get_driver(session, ident):
    """
    :param: session
    :return: driver [object]
    """
    return session.get_driver(ident)


def get_results(session):
    """
    :param session:
    :return: results [object]
    """
    return session.results


if __name__ == '__main__':
    print("This file should be imported, not ran separately")