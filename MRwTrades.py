import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
prices = pd.read_csv("tesla_stock_prices.csv")

def generate_trades(prices, window_size, num_std_dev):
    rolling_mean = prices.rolling(window=window_size).mean()
    rolling_std = prices.rolling(window=window_size).std()
    upper_band = rolling_mean + (rolling_std * num_std_dev)
    lower_band = rolling_mean - (rolling_std * num_std_dev)

    buy_signal = (prices < lower_band).astype(int)
    sell_signal = (prices > upper_band).astype(int)

    # Initialize the list to store the trades
    trades = []

    # Loop over the signals and generate trades
    for i in range(len(prices)):
        if buy_signal[i] == 1:
            # Buy signal
            entry_date = prices.index[i]
            entry_price = prices.iloc[i]
            trades.append((entry_date, entry_price, None))
        elif sell_signal[i] == 1:
            # Sell signal
            exit_date = prices.index[i]
            exit_price = prices.iloc[i]
            if trades:
                # If we have an open position, Price it
                last_trade = trades[-1]
                trades[-1] = (last_trade[0], last_trade[1], exit_date, exit_price)
            else:
                # Otherwise, do nothing
                pass

    return trades

# Generate the trades
trades = generate_trades(prices['Price'], 20, 2)

# Plot the prices and the trades
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(prices.index, prices['Price'], label='Price')
if trades:
    print(len(trades))
for trade in trades:
    entry_date, entry_price, exit_date, exit_price = trade
    if exit_date is None:
        # Open trade
        ax.scatter(entry_date, entry_price, color='green', marker='^', s=100)
    else:
        # Priced trade
        ax.scatter(entry_date, entry_price, color='red', marker='v', s=100)
        ax.plot([entry_date, exit_date], [entry_price, exit_price], color='black', lw=2)
ax.legend()
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title('Tesla Mean Reversion with Trades')
plt.show()
