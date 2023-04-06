import pandas as pd
import requests

# Set API endpoint and parameters
url = 'https://www.alphavantage.co/query'
params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': 'MSFT',
    'outputsize': 'full',
    'apikey': '<your-api-key>'
}

# Send API request
response = requests.get(url, params=params)

# Convert response to Pandas dataframe
data = response.json()['Time Series (Daily)']
df = pd.DataFrame.from_dict(data, orient='index')
df.index = pd.to_datetime(df.index)
df = df.astype(float)

# Print dataframe
print(df)
