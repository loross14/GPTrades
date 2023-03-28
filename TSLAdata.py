import yfinance as yf
import pandas as pd

# set the stock ticker and date range
ticker = "TSLA"
start_date = "2015-01-01"
end_date = "2022-03-25"

# fetch the stock price data from Yahoo Finance
data = yf.download(ticker, start=start_date, end=end_date)

# save the data to a CSV file
data.to_csv("tesla_stock_prices.csv")
