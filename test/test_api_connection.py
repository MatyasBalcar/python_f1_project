"""
File for testing api's connections
"""
import fastf1


def test_connection():
    """
    Tests connection to the fastf1 api
    :return:
    nothing
    :print:
    { test_driver [object] }
    """

    session = fastf1.get_session(2019, 'Monza', 'Q')
    #gets the session from 2019 at Monza-Qualifying
    session.load(telemetry=False, laps=False,weather=False)
    test_driver = session.get_driver("VER")
    print(test_driver)


if __name__ == '__main__':
    test_connection()