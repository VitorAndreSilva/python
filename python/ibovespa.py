import yfinance as yf
ibovespa = yf.download('^BVSP', start = '2020-01-01')
ibovespa.Close.plot();