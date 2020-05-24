from dotenv import load_dotenv
load_dotenv()

import os
SECRET_KEY = os.getenv("SECRET_KEY") 
KEY_ID = os.getenv("KEY_ID")
BASE_URL = os.getenv("BASE_URL")

import alpaca_trade_api as tradeapi


api = tradeapi.REST(key_id=KEY_ID, secret_key=SECRET_KEY, base_url=BASE_URL, api_version='v2')


api.submit_order(
                symbol='AAPL',
                qty=5,
                side='sell',
                type='market',
                time_in_force='gtc'
)
