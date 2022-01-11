# See README

from microprediction import MicroReader
import random
import time
import random
import pandas as pd

SKATER_RESIDUAL_URL = 'https://raw.githubusercontent.com/microprediction/precisedata/main/skaterresiduals/skater_residuals_0.csv'
EXAMPLE_STREAMS = ['electricity-lbmp-nyiso-west.json','electricity-load-nyiso-nyc.json']


def random_name():
    """ Choose a random name of a stream """
    mr = MicroReader()
    names = [n for n in mr.get_stream_names() if '~' not in n ]
    return random.choice(names)


def get_live(name:str=None)->[float]:
    """ Get a live univariate real world time series """
    mr = MicroReader()
    if name is None:
        name = random_name()
    lagged = mr.get_lagged_values(name=name)
    values = list(reversed(lagged))
    return values

live = get_live 

n_data = 450

def get_historical(n_obs:int=10000):
    """ Dataframe with up to 30,000 x 20 variable values """
    assert n_obs<=30000, 'Too many requested. Try 30,000 or less.'
    got = False
    while not got:
        the_choice = random.choice(list(range(n_data)))
        the_url = SKATER_RESIDUAL_URL.replace('N', str(the_choice))
        try:
            df = pd.read_csv(the_url)
            del df['Unnamed: 0']
            got = len(df.index) > n_obs + 10
        except:
            got = False
    return df

historical = get_historical
