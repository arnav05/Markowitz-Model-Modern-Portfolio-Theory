from MarkowitzModel import *

start_date = '2017-01-01'
end_date = '2022-01-01'

if __name__ == "__main__":

    # Requesting user to input their portfolio
    print("\nPlease input ticker symbols of stocks/Bonds in your portfolio.\nAccepted example input: AAPL NVDA TSLA GE AMZN\n")
    inputPortfolio = input("Portfolio: ")

    # Splitting input by spaces in between
    portfolio = inputPortfolio.split(' ')

    stock_data = {}

    print("\nFetching information and performing calculations\n")
    # Checking if there is a mistake in the input
    for security in portfolio:
        ticker = yf.Ticker(security)

        if ticker.info['regularMarketPrice'] == None:
            raise NameError(f" {security} ticker is not right! Please Try again.")

        stock_data[security] = ticker.history(start=start_date, end=end_date)['Close']

    dataset = pd.DataFrame(stock_data)

    show_data(dataset)
    # dataset = download_data()
    # show_data(dataset)
    # log_daily_returns = calculate_return(dataset)
    # show_statistics(log_daily_returns)