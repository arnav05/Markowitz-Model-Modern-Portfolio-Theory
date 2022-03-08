from MarkowitzModel import *
import yfinance as yf
import pandas as pd

# Historical data - define start and end date
start_date = '2020-01-01'
end_date = '2022-01-01'

if __name__ == "__main__":

    # Requesting user to input their portfolio
    print("\nPlease input ticker symbols of stocks/Bonds in your portfolio.\nAccepted example input: AAPL NVDA Tsla ge AMZN\n")
    inputPortfolio = input("Portfolio: ")

    # Splitting input by spaces in between
    portfolio = inputPortfolio.split(' ')

    # Dictionary for storing stock information with their ticker
    stock_data = {}

    print("\nFetching information and performing calculations\n")
    # Checking if there is a mistake in the input, if not downloading data
    for security in portfolio:
        ticker = yf.Ticker(security)

        if ticker.info['regularMarketPrice'] == None:
            raise NameError(f" {security} ticker is not right! Please Try again.")

        stock_data[security] = ticker.history(start=start_date, end=end_date)['Close']

    dataset = pd.DataFrame(stock_data)
    log_daily_returns = calculate_return(dataset)

    p_weights, p_returns, p_volatility = generate_portfolios(portfolio, log_daily_returns)
    show_portfolios(p_returns, p_volatility)

    optimum = optimize_portfolio(portfolio, p_weights, log_daily_returns)

    print_optimal_portfolio(optimum, log_daily_returns)
    show_optimal_portfolio(optimum, log_daily_returns, p_returns, p_volatility)