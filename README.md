# realdata

Tired of using fake data for testing time series? This returns medium length (~1-2000) univariate time series from real world instrumented processes. The data is live so this never gets stale. 

## Install

    pip install realdata
    
### Usage 

    from realdata import get_values
    values = get_values()
    
### Too bare bones for you? 

See [other ways](https://www.microprediction.org/features.html) to grab the data directly, or see this short [tutorial](https://www.microprediction.com/python-3) on retrieving historical data using the microprediction package.  

### What's the data?

All sorts of things: traffic, electricity, emoji usage, hospital wait times, altitude of UFOs, security wait times at airports, changes in crypto-currencies, ... you get the idea. 

![](https://i.imgur.com/LmrmLQF.png)

Streams are live so the next time you get data, it will be different. 

### Can I add to the collection?

Yes see the [tutorial](https://www.microprediction.com/python-4) on making a new stream of data. 
