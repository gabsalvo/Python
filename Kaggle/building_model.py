import pandas as pd
from sklearn.tree import DecisionTreeRegressor

melb_file_path="/home/gab/Python/Kaggle/melb_data.csv"

melb_data = pd.read_csv(melb_file_path)

melbo_data = melb_data.dropna(axis=0)

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = melbo_data[melbourne_features]

y = melbo_data.Price

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))