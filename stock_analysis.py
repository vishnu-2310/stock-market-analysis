import pandas as pd

# Load dataset
data = pd.read_csv("stock_data.csv")

# Show first 5 rows
print(data.head())

# Basic info
print(data.info())

# Summary statistics
print(data.describe())

# Average closing price
print("Average Close Price:", data["Close"].mean())
