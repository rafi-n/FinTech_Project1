# import all necessary libraries
import requests
from ft_logger import * 
import pandas as pd

class PolygonIO:
    def __init__(self, api_key, tickers, start_date, end_date):
        self.api_key = api_key
        self.tickers = tickers
        # All dates should be of the form: YYYY-MM-DD
        self.start_date = start_date
        self.end_date = end_date
        
    def get_splits(self):
        log.info('Getting stock split info')
        responses = [requests.get(f"https://api.polygon.io/v3/reference/splits?ticker={ticker}&execution_date.gte={self.start_date}&execution_date.lte={self.end_date}&apiKey={self.api_key}").json() for ticker in self.tickers]
        # responses.remove([])
        # responses = [responses[i] for i in range(0, len(responses)) if responses[i]
        # get the stocks splits for each execution date
        splits = [[{'time':responses[t]['results'][i]['execution_date'], 'split_factor':responses[t]['results'][i]['split_to'] / responses[t]['results'][i]['split_from'], 'ticker':responses[t]['results'][i]['ticker']} for i in range(0, len(responses[t]['results']))] for t in range(0, len(self.tickers))]
        while [] in splits:
            splits.remove([])
        return splits
