from realdata import get_random_historical_data
from realdata import get_values

def test_live():
    values = get_values()
    
def test_historical():
    df = get_random_historical_data(n_obs=5000)
