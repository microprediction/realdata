# realdata
A really simple way to grab univariate time series data that never gets stale.

## Usage:

Not used. Instead:

    pip install microprediction
    
Then 

    from microprediction import MicroReader
    import random
    mr = MicroReader()
    NAMES = mr.get_stream_names()
    name = random.choice(NAMES)
    lagged = mr.get_lagged_values(name=name)
    chronological = list(reversed(lagged))
