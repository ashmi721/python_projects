import yfinance as yf

STK = input("Enter stock symbol (e.g., AAPL for Apple Inc.): ")
Share = yf.Ticker(STK)
info = Share.info

# Check if 'regularMarketPrice' key exists
if 'regularMarketPrice' in info:
    market_price = info['regularMarketPrice']
    print(f"Market Price of {STK}: {market_price}")
else:
    print(f"Market Price information for {STK} not available.")
