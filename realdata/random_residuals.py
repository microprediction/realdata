import time
import random
import pandas as pd

SKATER_RESIDUAL_URL = 'https://raw.githubusercontent.com/microprediction/precisedata/main/skaterresiduals/skater_residuals_0.csv'

n_data = 450

def get_random_data(n_obs:int):
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

