import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from csv import reader

#tickers for all the stocks I'm watching. Listed in a CSV file with all the stocks. 
with open('shares.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    tickers = list(csv_reader)

#creates a pdf for saving of the plots. To be used in the future. 
#pp = PdfPages(f'{tickers[i]}.pdf')


#function to return the stock price for the stocks for the date range required. Currently one year.
def shareprice(ticker):
    stock = pdr.get_data_yahoo(ticker,
                start=datetime.datetime(2019, 12, 1),
                end=datetime.datetime(2020, 12, 11))
    
    return stock


#for loop to plot the SMA for 50,100,150
for i in range(len(tickers)):
    share = shareprice(tickers[i])

    adj_close_px = share['Adj Close']

    share['50'] = adj_close_px.rolling(window=50).mean()
    share['100'] = adj_close_px.rolling(window=100).mean()
    share['150'] = adj_close_px.rolling(window=150).mean()

    share[['Adj Close', '50', '100', '150']].plot()

    plt.title(tickers[i])
    plt.xlabel('Date')
    plt.ylabel('Share Price')

    pp = PdfPages(f'{tickers[i]}.pdf')

    plt.savefig(pp, format='pdf')
    plt.clf()
    pp.close()
    

#plt.savefig()
#plt.show()






