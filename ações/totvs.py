import yfinance as yf
totvs = yf.download('TOTS3.SA', start = '2024-08-06')
totvs.Close.plot();