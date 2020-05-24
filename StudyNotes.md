# Setup 

Shoutout to Sebastian and the awesome guide posted on [medium](https://medium.com/analytics-vidhya/the-alpaca-api-explained-for-people-who-want-to-get-started-trading-7e57f0af7a) covering this topic!

Without further adieu let's jump into the project! 


# Alpaca API Explained for People Who Want to get Started Trading 

Alpaca Trade API allows users to buy and sell shares in real time, have access to unlimited paper trading, see how algorithms are performing, all from a Python program. Zero commissions!! 

In the simplest form buying a stock looks something like: 

```python 
api.submit_order(
    symbol='AAPL', 
    qty=5, 
    side='buy',
    type='market',
    time_in_force='gtc
)
```

Let's see how we get to this point. 

## Terminology 

Let's define a couple of simple terms 
- Share: Single unit issued by a company as a representation of ownership 
- Stock: Collection of shares 
- Paper Trading: Simulated trading which allows investors to practice buying and selling securities without real money 
- Live Trading: Trading with real money, allowing for profits and losses 
- Algorithm: Set of rules regarding when to buy, sell or hold shares 
- Symbol: Identifier used for a stock (ex. AAPL)

## Setup 

After creating an account we will be using the Alpaca Trade API -- install this using pip/pip3

```
pip3 install alpaca-trade-api  
```


Another thing to be aware of make sure that `python3` and `pip3` are being used so that we have access to all of Python3's capabilities. 


Now we can go ahead and start making trades by calling the Alpaca Trade API: 
```python
api = tradeapi.REST(key_id=KEY_ID, secret_key=SECRET_KEY, base_url=BASE_URL, api_version='v2')


api.submit_order(
                symbol='AAPL',
                qty=5,
                side='sell',
                type='market',
                time_in_force='gtc'
)
```

