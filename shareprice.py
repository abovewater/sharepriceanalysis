import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt

#tickers for all the stocks I'm watching
tickers = ['EOS.AX', 'WES.AX', 'BHP.AX']

ask = input("What stock do you want to check? ")

#function to return the stock price for the stocks.
def shareprice(ticker):
    stock = pdr.get_data_yahoo(ticker,
                start=datetime.datetime(2019, 12, 1),
                end=datetime.datetime(2020, 12, 11))
    
    return stock


share = shareprice(ask)

adj_close_px = share['Adj Close']

share['50'] = adj_close_px.rolling(window=50).mean()
share['100'] = adj_close_px.rolling(window=100).mean()
share['150'] = adj_close_px.rolling(window=150).mean()

share[['Adj Close', '50', '100', '150']].plot()

plt.title(ask)
plt.show()

