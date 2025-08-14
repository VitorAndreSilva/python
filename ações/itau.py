import yfinance as yf
itau = yf.download('ITUB4.SA', start = '2024-08-06')
itau.Close.plot();