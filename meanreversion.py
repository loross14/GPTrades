import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the data
# df = pd.read_csv('stock_prices.csv')
df = pd.read_csv('tesla_stock_prices.csv', index_col='Date', parse_dates=True)

# calculate the rolling mean and standard deviation
rolling_mean = df['Price'].rolling(window=20).mean()
rolling_std = df['Price'].rolling(window=20).std()

# calculate the upper and lower bands
upper_band = rolling_mean + 2 * rolling_std
lower_band = rolling_mean - 2 * rolling_std

# plot the data and the bands
plt.plot(df['Price'], label='stock price')
plt.plot(rolling_mean, label='rolling mean')
plt.plot(upper_band)
plt.plot(lower_band)
# Add axis labels
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.show()

# create a new column for the position
df['Position'] = np.nan

# determine the position based on whether the price is above or below the bands
for i in range(len(df)):
    if df['Price'][i] > upper_band[i]:
        df['Position'][i] = -1
    elif df['Price'][i] < lower_band[i]:
        df['Position'][i] = 1

# forward fill the position column to simulate holding the position
df['Position'].fillna(method='ffill', inplace=True)

# calculate the daily returns
df['Returns'] = df['Price'].pct_change()

# calculate the strategy returns
df['Strategy Returns'] = df['Returns'] * df['Position'].shift(1)

# calculate the cumulative returns
df['Cumulative Returns'] = (1 + df['Strategy Returns']).cumprod()

# plot the cumulative returns
plt.plot(df['Cumulative Returns'], label='Cumulative returns')
# Add axis labels
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
# Add a legend
plt.legend()
plt.show()
