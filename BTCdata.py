import yfinance as yf
import pandas as pd

# Define the ticker symbol
ticker = "BTC-USD"

# Set the start and end date for the historical data
start_date = "2015-01-01"
end_date = "2022-03-27"

# Get the data from yfinance
data = yf.download(ticker, start=start_date, end=end_date)

# Save the data as a CSV file
data.to_csv("bitcoin_prices.csv")
