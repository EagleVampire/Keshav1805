import requests
import pandas as pd
import scipy
import numpy as np
import sys

TRAIN_DATA_URL = "https://storage.googleapis.com/kubric-hiring/linreg_train.csv"
TEST_DATA_URL = "https://storage.googleapis.com/kubric-hiring/linreg_test.csv"


def predict_price(areas):
    """
    This method must accept as input an array `area` (represents a list of areas sizes in sq feet) and must return the respective predicted prices (price per sq foot) using the linear regression model that you build.

    You can run this program from the command line using `python3 regression.py`.
    """
    # response = requests.get(TRAIN_DATA_URL)
    # YOUR IMPLEMENTATION HERE
    train_data = pd.read_csv('linreg_train.csv')
    train_arr = np.array(train_data.values,'float')

    x = train_arr[:,0]
    y = train_arr[:,1]
    x = x/(np.max(x)) 

    m = (len(x) * np.sum(x*y) - np.sum(x) * np.sum(y)) / (len(x)*np.sum(x*x) - np.sum(x) ** 2)
    b = (np.sum(y) - m *np.sum(x)) / len(x)

    areas = areas/np.max(x)

    return m*areas + b



if __name__ == "__main__":
    # DO NOT CHANGE THE FOLLOWING CODE
    from data import validation_data
    areas = np.array(list(validation_data.keys()))
    prices = np.array(list(validation_data.values()))
    predicted_prices = predict_price(areas)
    rmse = np.sqrt(np.mean((predicted_prices - prices) ** 2))
    try:
        assert rmse < 170
    except AssertionError:
        print(f"Root mean squared error is too high - {rmse}. Expected it to be under 170")
        sys.exit(1)
    print(f"Success. RMSE = {rmse}")