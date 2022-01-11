from realdata import get_live, get_historical, live, historical

def test_live():
    values = get_live()
    values = live()
    
def test_historical():
    df = get_historical(n_obs=5000)
    df = historical()
