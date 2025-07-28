import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample data (replace with your own CSV or values if needed)
data = {
    'Year': [2010, 2012, 2015, 2018, 2020],
    'Present_Price': [5.59, 9.54, 8.35, 15.00, 12.00],
    'Kms_Driven': [27000, 43000, 69000, 52000, 31000],
    'Owner': [0, 0, 0, 0, 0],
    'Fuel_Type_Diesel': [0, 1, 1, 0, 0],
    'Fuel_Type_Petrol': [1, 0, 0, 1, 1],
    'Seller_Type_Individual': [0, 1, 1, 0, 0],
    'Transmission_Manual': [1, 1, 0, 1, 1],
    'Selling_Price': [3.35, 5.50, 4.75, 10.00, 9.00]
}

df = pd.DataFrame(data)

X = df.drop(['Selling_Price'], axis=1)
y = df['Selling_Price']

X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model saved as model.pkl")
