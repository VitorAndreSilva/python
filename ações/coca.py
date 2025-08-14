import yfinance as yf
coca = yf.download('KO', start = '2024-08-06')
coca.Close.plot();