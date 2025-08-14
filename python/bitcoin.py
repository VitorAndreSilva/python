import yfinance as yf
bitcoin = yf.download('BTC-USD', start = '2020-01-01')
bitcoin.Close.plot();