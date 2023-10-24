import pandas as pd

melb_file_path="/home/gab/Python/Kaggle/melb_data.csv"

melb_data = pd.read_csv(melb_file_path)

print(melb_data.columns)

melbo_data = melb_data.dropna(axis=0)

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = melbo_data[melbourne_features]

y = melbo_data.Price

print(melbo_data.columns)
print(y)

print(X.describe())
print(X.head())