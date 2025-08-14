import yfinance as yf
xfix = yf.download('XFIX', start = '2023-07-01')
xfix.Close.plot();