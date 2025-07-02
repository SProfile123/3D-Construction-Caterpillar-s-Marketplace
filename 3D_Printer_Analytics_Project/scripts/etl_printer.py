
import pandas as pd

df = pd.read_csv('../data/3d_printer_data_cleaned.csv')
df.dropna(inplace=True)
df['print_time'] = pd.to_datetime(df['print_time'])

summary = df.groupby('printer_model').agg({
    'success': 'mean',
    'layer_height': 'mean',
    'print_duration': 'mean'
}).reset_index()

summary.to_csv('../data/processed/printer_summary.csv', index=False)
print("ETL complete.")
