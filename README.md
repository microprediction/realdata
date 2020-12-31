# realdata
Simple real time series data

## Usage:

Not used. Instead:

    from microprediction import MicroReader
    import random
    mr = MicroReader()
    NAMES = mr.get_stream_names()
    name = random.choice(NAMES)
    lagged = mr.get_lagged_values(name=name)
    chronological = list(reversed(lagged))
