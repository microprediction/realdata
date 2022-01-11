# realdata


## Install

    pip install realdata
    
### Random live data (around 1000 points) 

    from realdata import get_values
    values = get_values()
    
### Random historical data (around 30,000 points for 20 variables)

    from realdata import get_historical
    df = get_historical()
    
### Too bare bones for you? 

See [other ways](https://www.microprediction.org/features.html) to grab the live data directly, or see this short [tutorial](https://www.microprediction.com/python-3) on retrieving historical data using the microprediction package.  

### What's the data?

All sorts of things: traffic, electricity, emoji usage, hospital wait times, altitude of UFOs, security wait times at airports, changes in crypto-currencies, ... you get the idea. 

![](https://i.imgur.com/LmrmLQF.png)

Streams are live so the next time you get data, it will be different. 

### Can I add to the collection?

Yes see the [tutorial](https://www.microprediction.com/python-4) on making a new stream of data. 
