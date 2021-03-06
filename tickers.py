# Provide a list of all tickers currently listed on our target indexes 

import quandl

target_indexes = ['NYSE', 'NASDAQ','SPY','DJI']

tickers = quandl.get_table('SHARADAR/TICKERS', qopts={"columns":['ticker', 'exchange']}, api_key='INSERT_API_KEY_HERE', paginate=True)

tickers = tickers.loc[tickers['exchange'].isin(target_indexes)]

tickers
