# See README

from microprediction import MicroReader
import random


EXAMPLE_STREAMS = ['electricity-lbmp-nyiso-west.json','electricity-load-nyiso-nyc.json']


def random_name():
    """ Choose a random name of a stream """
    mr = MicroReader()
    names = [n for n in mr.get_stream_names() if '~' not in n ]
    return random.choice(names)


def get_values(name:str=None)->[float]:
    """ Get a real world time series """
    mr = MicroReader()
    if name is None:
        name = random_name()
    lagged = mr.get_lagged_values(name=name)
    values = list(reversed(lagged))
    return values


if __name__=='__main__':
    values = get_values()
    print(len(values))
