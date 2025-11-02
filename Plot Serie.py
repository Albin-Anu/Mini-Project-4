# Import necessary libraries
import yfinance as yf
import matplotlib.pyplot as plt

# Get stock data for a specific company (example: TCS)
ticker = 'TCS.NS'  # use .NS for NSE stocks, .BO for BSE
data = yf.download(ticker, start='2024-01-01', end='2025-01-01')

# Display first few rows
print(data.head())

# Plot the Closing Price
plt.figure(figsize=(10, 5))
plt.plot(data['Close'], label=f'{ticker} Closing Price', color='blue')
plt.title(f'{ticker} Stock Price (2024)')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)
plt.show()
