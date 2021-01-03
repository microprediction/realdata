# realdata

Tired of using fake data for testing time series? This returns medium length (~1-2000) univariate time series from real world instrumented processes. The data is live so this never gets stale. 

## Install

    pip install realdata
    
### Usage 

    from realdata import get_values
    values = get_values()
    
### Too bare bones for you? 

See [other ways](https://www.microprediction.org/features.html) to grab the data directly, or see this short [tutorial](https://www.microprediction.com/python-3) on retrieving historical data using the microprediction package.  
