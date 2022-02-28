import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimization


# Average number of trading days in a year
NUM_TRADING_DAYS = 252
# For generating random portfolio weights
NUM_PORTFOLIOS = 10000


def show_data(data):
    data.plot(figsize=(10, 5))
    plt.show()


# using log for normalization: to measure all variables in comparable metric
def calculate_return(data):
    log_return = np.log(data/data.shift(1))
    return log_return[1:]


# calculating annual return
def show_statistics(returns):
    # Calculates average mean for a year
    print(returns.mean()*NUM_TRADING_DAYS)
    # Calculates covariance between all stocks
    print(returns.cov()*NUM_TRADING_DAYS)


def show_mean_variance(returns, weights):
    # Calculating annual return
    portfolio_return = np.sum(returns.mean()*weights) * NUM_TRADING_DAYS
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov()*NUM_TRADING_DAYS, weights)))
    print(portfolio_return)
    print(portfolio_volatility)


def generate_portfolios(portfolio, log_returns):

        portfolio_weights = []
        portfolio_returns = []
        portfolio_volatility = []

        for _ in range(NUM_PORTFOLIOS):
            w = np.random.random(len(portfolio))
            # Normalizing weight to have sum of weights equal to 1
            w /= np.sum(w)
            portfolio_weights.append(w)
            portfolio_returns.append(np.sum(log_returns.mean()*w)*NUM_TRADING_DAYS)
            portfolio_volatility.append(np.sqrt(np.dot(w.T, np.dot(log_returns.cov()*NUM_TRADING_DAYS, w))))

        return np.array(portfolio_weights), np.array(portfolio_returns), np.array(portfolio_volatility)


def show_portfolios(returns, volatility):
    plt.figure(figsize=(10,6))
    plt.scatter(volatility, returns, c=returns/volatility, marker="o")
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Returns')
    plt.colorbar(label='Sharpe Ratio')
    plt.show()


def statistics(weights, returns):
    portfolio_return = np.sum(returns.mean()*weights)*NUM_TRADING_DAYS
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * NUM_TRADING_DAYS, weights)))

    return np.array([portfolio_return, portfolio_volatility, portfolio_return/portfolio_volatility])


# scipy optimize module can find the minimum of a given function
# maximum of a f(x) is the mimimum of -f(x)
def min_function_sharpe(weights, returns):
    return -statistics(weights, returns)[2]


# The constraint is that sum of edge weights = 1
# f(x) = 0 this is the function to minimize
def optimize_portfolio(portfolio, weights, log_returns):
    constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
    # The weights can be 1 at most: 1 when 100% of money is invested into a single stock
    bounds = tuple((0,1) for _ in range(len(portfolio)))
    return optimization.minimize(fun=min_function_sharpe, x0=weights[0], args=log_returns, method='SLSQP',
                          bounds=bounds, constraints=constraints)


def print_optimal_portfolio(optimum, returns):
    print("Optimal portfolio: ", optimum['x'].round(5))
    print("Expected return, volatility and Sharpe ratio: ",
          statistics(optimum['x'].round(3), returns))


def show_optimal_portfolio(optimum, returns, portfolio_returns, portfolio_volatility):
    plt.figure(figsize=(10, 6))
    plt.scatter(portfolio_volatility, portfolio_returns, c=portfolio_returns / portfolio_volatility, marker="o")
    plt.grid(True)
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Returns')
    plt.colorbar(label='Sharpe Ratio')
    plt.plot(statistics(optimum['x'], returns)[1], statistics(optimum['x'], returns)[0], 'g*', markersize=20.0)
    plt.show()

