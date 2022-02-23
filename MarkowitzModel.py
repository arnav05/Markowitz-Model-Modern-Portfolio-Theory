import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as optimization


# Average number of trading days
NUM_TRADING_DAYS = 252


def show_data(data):
    data.plot(figsize=(10, 5))
    plt.show()


# using log for normalization: to measure all variables in comparable metric
def calculate_return(data):
    log_return = np.log(data/data.shift(1))
    return log_return[1:]


# calculating annual metrics
def show_statistics(returns):
    print(returns.mean()*NUM_TRADING_DAYS)
    print(returns.cov()*NUM_TRADING_DAYS)