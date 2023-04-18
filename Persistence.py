# Import all necessary libraries
import os
from pathlib import Path
import pandas as pd
import hvplot.pandas
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from sqlalchemy import create_engine
import datetime
from dateutil.relativedelta import relativedelta


# Import data from API/csv into Pandas DataFrame

load_dotenv("alpaca.env")

# Set Alpaca API key and secret
alpaca_api_key=os.getenv('APCA_API_KEY_ID')
alpaca_secret_key=os.getenv('APCA_API_SECRET_KEY')
alpaca_endpoint=os.getenv('APCA_API_BASE_URL')

# Create the Alpaca API object
alpaca = tradeapi.REST()


def load_stock_data(date, tickers):

    # connect to database
    engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/ditiae")

    # Format current and previous date as ISO format

    date_fmt = date.strftime('%Y-%m-%d')
    today = pd.Timestamp(date_fmt, tz='America/New_York').isoformat()

    # Set start date of five years back from today.
    # Sample results may vary from the solution based on the time frame chosen
    five_yrs_ago = date - relativedelta(years=5)
    five_yrs_ago = five_yrs_ago.strftime('%Y-%m-%d')
    start_date = pd.Timestamp(five_yrs_ago, tz='America/New_York').isoformat()

    # Set the tickers


    # Set timeframe to "1Day" for Alpaca API
    timeframe = "1Day"

    # Get current closing prices for SPY and AGG
    # The current day may be a day when the markets are closed (weekend, holiday, etc.)
    # So, if the retrieved portfolio is empty, let's try the previous day.
    stocks_df = alpaca.get_bars(tickers, timeframe, start=start_date, end=today).df

    while stocks_df.empty:
        date -= relativedelta(days=1)
        date_fmt = date.strftime('%Y-%m-%d')
        today = pd.Timestamp(date_fmt, tz='America/New_York').isoformat()
        stocks_df = alpaca.get_bars(tickers, timeframe, start=start_date, end=today).df

    stocks_df['asset_class'] = 'stock'
    return stocks_df
    