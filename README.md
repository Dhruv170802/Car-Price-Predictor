# 🚗 Car Price Prediction App

This is a simple **Machine Learning Web App** built with **Streamlit** that predicts the selling price of a used car based on various features like year, present price, kilometers driven, fuel type, seller type, and transmission type.

---


## 📌 Features

- Interactive web UI with Streamlit
- Predicts car resale price using Linear Regression
- Encodes categorical variables (Fuel Type, Transmission, Seller Type)
- Trained on sample dataset (can be replaced with real data)

---

## 🧠 How It Works

The model uses **Linear Regression** trained on a dataset with the following features:

- `Year`: Year of purchase
- `Present_Price`: Current ex-showroom price (in lakhs)
- `Kms_Driven`: Kilometers driven
- `Owner`: Number of previous owners (0/1/2)
- `Fuel_Type`: Petrol/Diesel/CNG (encoded)
- `Seller_Type`: Dealer or Individual (encoded)
- `Transmission`: Manual or Automatic (encoded)

---

## 📁 Project Structure


---

## ⚙️ Installation


cd car-price-prediction
------
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
------
pip install -r requirements.txt
------
streamlit run app.py

