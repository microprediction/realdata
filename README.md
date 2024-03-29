# realdata

A mini-package providing an alternative to:

     import np
     x = np.cumsum(np.random.randn(1000))

if you need time-series data in under ten seconds. 

## Install

    pip install realdata
    
### Univariate live data (around 1000 points) 

    from realdata import live
    values = live()
    
### Multivariate historical data (around 30,000 points for 20 variables)

    from realdata import historical
    df = historical()
    
    
There are pseudonyms get_live and get_historicall for backward compat. 
# Alternatives

See [other ways](https://www.microprediction.org/features.html) to grab the live data directly, or see this short [tutorial](https://www.microprediction.com/python-3) on retrieving historical data using the microprediction package.  

The historical data is from [precisedata](https://github.com/microprediction/precisedata). 

### What's the data?

All sorts of things: traffic, electricity, emoji usage, hospital wait times, altitude of UFOs, security wait times at airports, changes in crypto-currencies, ... you get the idea. 

![](https://i.imgur.com/LmrmLQF.png)

Streams are live so the next time you get data, it will be different. 

### Can I add to the collection?

Yes see the [tutorial](https://www.microprediction.com/python-4) on making a new stream of data. 
