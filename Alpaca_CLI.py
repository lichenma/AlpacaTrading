from dotenv import load_dotenv
load_dotenv()

import os
SECRET_KEY = os.getenv("SECRET_KEY") 
KEY_ID = os.getenv("KEY_ID")
BASE_URL = os.getenv("BASE_URL")

import alpaca_trade_api as tradeapi


api = tradeapi.REST(key_id=KEY_ID, secret_key=SECRET_KEY, base_url=BASE_URL, api_version='v2')

# Check for ensuring that markets are open before performing functions
if not api.get_clock().is_open:
    print('Market is closed.  Try again later.')
    exit()

# Execution loop for Command Line Tool 
# CLI
print('==================================')
print('Interactive paper-stock trading')
print('==================================')
while True:
    print('---')
    try:
        # This is where we will put our logic
        account = api.get_account()
        print('Your cash: ', account.cash)
        print('Your buying power: ', account.buying_power)

        buy_or_sell = input('[B]uy or [s]ell? ').lower()

        if buy_or_sell == 'b':
            side = 'buy'
        elif buy_or_sell == 's':
            side = 'sell'
        else:
            print('Unrecognized action.  Try again.')
            continue

        ticker = input('Ticker of the stock you would like to buy/sell: ')

        quantity = int(input('Quantity of the stock you would like to buy/sell: '))

        try:
            api.submit_order(
                symbol=ticker,
                qty=quantity,
                side=side,
                type='market',
                time_in_force='gtc'
            )
        except tradeapi.rest.APIError as e: # If the API doesn't recognize the stock ticker...
            print('Error:', e)
            continue

    except KeyboardInterrupt:
        print('\nProgram interrupted by user.  Exiting...')
        exit()