# See README

from microprediction import MicroReader
import random


DEFAULT_STREAMS = ['electricity-lbmp-nyiso-west.json','electricity-load-nyiso-nyc.json']


def random_name():
    """ Choose a random name of a stream """
    mr = MicroReader()
    NAMES = mr.get_stream_names()
    return random.choice(NAMES)


def get_values(name:str=None)->[float]:
    """ Get a real world time series """
    mr = MicroReader()
    if name is None:
        name = random.choice(DEFAULT_STREAMS)
    lagged = mr.get_lagged_values(name=name)
    values = list(reversed(lagged))
    return values


if __name__=='__main__':
    values = get_values()
    print(len(values))