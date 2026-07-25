import yfinance as yf
import pandas as pd

# Downloading historical data from Yahoo Finance

def download_assets(assets, start_date, end_date):

    full_prices = []

    for asset in assets:
        prices = yf.download(tickers=asset, start=start_date, end=end_date, auto_adjust=False)
        prices.columns = prices.columns.get_level_values(0)
        prices.columns = [c.lower() for c in prices.columns]
        prices["date"] = prices.index.values
        prices["date"] = pd.to_datetime(prices["date"]).dt.strftime("%Y-%m-%d")
        prices["asset"] = asset
        full_prices.append(prices)

    data = pd.concat(full_prices, ignore_index=True)

    cols = data.columns.tolist()
    l = len(cols) - 1
    data = data[cols[l-1:] + cols[:l-1]]

    return data

# Portfolio constructor

def portfolio(df, weights):

    df_pivot = df.pivot(index='date', columns='asset', values='log_return')

    portf = df_pivot @ weights

    portf = portf.reset_index()
    portf = portf.rename(columns={portf.columns[-1] : 'log_return'})

    return portf