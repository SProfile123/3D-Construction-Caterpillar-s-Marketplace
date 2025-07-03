import pandas as pd

# Load dataset
df = pd.read_csv("../data/3d_printer_data_cleaned.csv")

# Clean and transform
df.dropna(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period("M")
df['Profit Margin %'] = (df['Profit'] / df['Sales']) * 100

# Export cleaned data
df.to_csv("../data/printer_data_final.csv", index=False)
