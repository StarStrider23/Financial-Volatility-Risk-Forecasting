import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

# Price Histories

def price_history(df):

    assets = df["asset"].unique()

    first_dates = df.groupby(pd.to_datetime(df["date"]).dt.year)["date"].first().values
    first_years = pd.to_datetime(first_dates).year

    plt.figure(figsize=(12,8))

    for asset in assets:
        asset_df = df[df["asset"] == asset].copy()

        price = asset_df["close"]

        t = pd.to_datetime(asset_df["date"])

        plt.plot(t, price, lw=0.75, label=asset)

    plt.xticks(first_dates, first_years, rotation=45)
    plt.xlabel('Year')
    plt.ylabel('Asset Price')
    plt.title("Asset Prices Over Time")
    plt.legend(loc=0)
    plt.grid(True, alpha=0.2, color = "grey", ls='--', lw = 1)    
    plt.show()

# Plotting Histogram with volatility

def histogram(df):

    N = 36

    asset = df["asset"].unique()

    n = len(asset)

    if n > N:
        raise ValueError(f'Too many assets to display ({n}). Maximum supported is {N}')
    
    else:

        ncols = math.ceil(math.sqrt(n))
        nrows = math.ceil(n / ncols)

        fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(12,8))

        axes = ax.ravel()

        for i, ticker in enumerate(asset):
            axes[i].hist(df[df["asset"] == ticker]["log_return"], bins=100)
            vol = np.std(df[df["asset"] == ticker]["log_return"])
            axes[i].set_title(f"{ticker}; $\sigma$ = {vol:.3f}")

        for axis in axes[len(asset):]:
            axis.set_visible(False)

        fig.suptitle('Log Return Distribution Histograms')

        plt.show()

# Cumulative Return

def cum_return(df):

    assets = df["asset"].unique()

    first_dates = df.groupby(pd.to_datetime(df["date"]).dt.year)["date"].first().values
    first_years = pd.to_datetime(first_dates).year

    plt.figure(figsize=(12,8))

    for asset in assets:
        asset_df = df[df["asset"] == asset].copy()

        log_return = asset_df["log_return"]
        cum_return = np.exp(log_return.cumsum())

        t = pd.to_datetime(asset_df["date"])

        plt.plot(t, cum_return, lw=0.75, label=asset)

    plt.xticks(first_dates, first_years, rotation=45)
    plt.xlabel('Year')
    plt.ylabel('Cumulative Investment Return')
    plt.title('Cumulative Investment Return Over Time')

    plt.legend(loc=0)
    plt.grid(True, alpha=0.2, color = "grey", ls='--', lw = 1) 

    plt.show()

# Asset Box Plots

def boxplots(df):

    assets = df["asset"].unique()

    plt.figure(figsize=(12,8))

    plt.boxplot([df[df["asset"] == asset]["log_return"].dropna()
                for asset in assets], tick_labels=assets, showfliers=False, patch_artist=True)
    plt.axhline(0, color="red", ls="--", alpha=0.3)

    plt.xlabel('Assets')
    plt.ylabel('Log returns')
    plt.title('Asset Box Plots')
    plt.grid(axis="y", alpha=0.3)

    plt.show()

# Asset Correlation Heat Map

def corr_heat_map(df):

    returns = (
            [df[df["asset"] == asset][["date", "log_return"]]
             .set_index("date").rename(columns={"log_return" : asset})
                for asset in df["asset"].unique()]
                )

    return_mat = pd.concat(returns, join='outer', axis=1)
    corr_mat = return_mat.corr()

    plt.figure(figsize=(12,8))

    sns.heatmap(corr_mat, annot=True, cmap="coolwarm", fmt=".2f", linewidths=1)
    plt.title("Correlation Heatmap")

    plt.show()

# Plotting rolling volatility 

def roll_vol(df, roll_days=20):

    if roll_days < 1 or not isinstance(roll_days, int):
        raise ValueError('Please enter a valid integer valued rolling period: roll_days => 1.')
    
    else:

        assets = df["asset"].unique()

        first_dates = df.groupby(pd.to_datetime(df["date"]).dt.year)["date"].first().values
        first_years = pd.to_datetime(first_dates).year

        plt.figure(figsize=(12,8))

        for asset in assets:
            asset_df = df[df["asset"] == asset].copy()

            t = pd.to_datetime(asset_df["date"])

            if roll_days == 1:
                vol = [0] * len(t)

            else:
                vol = asset_df["log_return"].rolling(roll_days).std() * np.sqrt(252)

            plt.plot(t, vol, lw=0.75, label=asset)

        plt.title(f"{roll_days}-Day Rolling Annualized Volatility")
        plt.xticks(first_dates, first_years, rotation=45)
        plt.xlabel('Year')
        plt.ylabel("Volatility")
        plt.legend()
        plt.show()

# Summary

def summary(df):

    assets = df["asset"].unique()

    rows = []

    for asset in assets:

        asset_df = df[df["asset"] == asset]["log_return"]

        rows.append({
            "asset": asset,
            "mean": asset_df.mean(),
            "volatility": asset_df.std(),
            "volatility_annual": asset_df.std() * np.sqrt(252),
            "min": asset_df.min(),
            "max": asset_df.max(),
            "skew": asset_df.skew(),
            "kurtosis": asset_df.kurtosis()
        })

    summary_table = pd.DataFrame(rows)

    return summary_table