"""
File for getting live data from the fast-f1 api.
"""

import fastf1


def get_and_load_session(year, gp, ident):
    """
    :param year:
    :param gp:
    :param ident:
    :return: session [object]
    also loads the session
    """

    session = fastf1.get_session(year, gp, ident)
    session.load()
    return session


def get_drivers_list(session):
    """
    :param session:
    :return: drivers [list[ident]]
    """
    drivers = session.drivers
    drivers = [session.get_driver(driver)["Abbreviation"] for driver in drivers]
    return drivers


def get_driver(session, ident):
    """
    :param: session
    :return: driver [object]
    """
    return session.get_driver(ident)


def get_laps(session, ident, only_accurate=False):
    """
    :param session: The session object containing lap data
    :param ident: The driver identifier to pick laps for
    :param only_accurate: If True, only return laps where IsAccurate is True
    :return: laps [DataFrame]
    """
    laps = session.laps.pick_driver(ident)

    if only_accurate:
        laps = laps[laps["IsAccurate"] == True]

    return laps


def get_maximum_speed(laps_for_driver):
    minimum = 0
    for idx, row in laps_for_driver.iterrows():
        if row["SpeedST"] > minimum:
            minimum = row["SpeedST"]

    return minimum


def get_maximum_speeds(session):
    """
    :param session:
    :return: dict [ident:speed]
    """
    speeds = {

    }
    drivers = get_drivers_list(session)

    for driver in drivers:
        speeds[driver] = get_maximum_speed(get_laps(session, driver))
    return speeds


if __name__ == '__main__':
    print("This file should be imported, not ran separately")
