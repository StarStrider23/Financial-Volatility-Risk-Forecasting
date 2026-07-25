import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from eda.eda_functions import price_history, histogram, cum_return, boxplots, corr_heat_map, roll_vol, summary
from portfolio.assets import download_assets, portfolio
from machine_learning.features import features
from machine_learning.target import target
from machine_learning.predict_vol import predict_vol
from evaluation.errors import re, mae, rmse
from evaluation.violation import violations, violations_rate
from var_es.var_es import var_es
from evaluation.test import kupiec_test, christofferesen_test

# Technology: MSFT, Semiconductors:	NVDA, Financials: JPM, 
# Healthcare: UNH, Consumer: AMZN, Energy: XOM

tickers = ['NVDA', 'MSFT', 'JPM', 'UNH', 'AMZN', 'XOM']

start_date = '2000-01-01'
end_date = '2026-07-01'

df = download_assets(assets=tickers, start_date=start_date, end_date=end_date)

# SQL Exploratory Data Analysis part

conn = sqlite3.connect("market_data.db")
df.to_sql("data", conn, if_exists="replace", index=False)

query1 = """
SELECT asset, COUNT(*) AS observations
FROM data
GROUP BY asset;
"""

obs_per_asset = pd.read_sql_query(query1, conn)

print(obs_per_asset)

query2 = """
SELECT asset, MIN(date) AS first_date, MAX(date) AS last_date
FROM data
GROUP BY asset;
"""

date_range = pd.read_sql_query(query2, conn)

print(date_range)

query3 = """
SELECT asset, AVG(close) AS close_mean, AVG(volume) AS volume_mean
FROM data
GROUP BY asset;
"""

avg = pd.read_sql_query(query3, conn)

print(avg)

query4 = """
SELECT mn.asset, mn.date AS min_date, mn.close AS min_close, 
       mx.date AS max_date, mx.close AS max_close
FROM (
    SELECT asset, date, close
    FROM data
    WHERE (asset, close) IN (
        SELECT asset, MIN(close)
        FROM data
        GROUP BY asset)
        ) AS mn
    JOIN 
    (
    SELECT asset, date, close
    FROM data
    WHERE (asset, close) IN (
        SELECT asset, MAX(close)
        FROM data
        GROUP BY asset)
    ) AS mx
    ON mn.asset = mx.asset
ORDER BY mn.asset;
"""

max_min_close = pd.read_sql_query(query4, conn)

print(max_min_close)

query5 = """
WITH ranked_volume AS
    (
    SELECT ROW_NUMBER() OVER(PARTITION BY asset ORDER BY volume DESC) AS row_num,
           asset, date, volume
    FROM data
    )
SELECT * 
FROM ranked_volume 
WHERE row_num <= 5
ORDER BY asset;
"""

top_volume = pd.read_sql_query(query5, conn)

print(top_volume)

query6 = """
SELECT asset, date, close, (close - prev_close) AS close_diff
FROM (
    SELECT asset, date, close, LAG(close, 1, close) 
           OVER(PARTITION BY asset 
                ORDER BY date) AS prev_close
    FROM data
    ORDER BY asset, date
    )
ORDER BY asset, date
"""

daily_close_change = pd.read_sql_query(query6, conn)

print(daily_close_change)

query7 = """
SELECT asset, date, 
       AVG(close) OVER (PARTITION BY asset 
       ORDER BY date 
       ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) AS five_day_roll_avg
FROM data
ORDER BY asset, date;

"""

roll_avg = pd.read_sql_query(query7, conn)

print(roll_avg)

query8 = """
WITH avg_volumes AS (
    SELECT asset, AVG(volume) AS avg_volume
    FROM data
    GROUP BY asset
)
SELECT asset, avg_volume, 
        RANK() OVER(
            ORDER BY avg_volume DESC
                ) AS volume_rank
FROM avg_volumes 

"""

ord_vol = pd.read_sql_query(query8, conn)

print(ord_vol)

df["log_return"] = df.groupby("asset")["close"].transform(lambda x : np.log(x / x.shift(1)))

cols = ["date", "asset", "log_return"]
returns = df[cols]

returns.to_sql("returns", conn, if_exists="replace", index=False)

query9 = """
SELECT *
FROM returns;
"""

ret = pd.read_sql_query(query9, conn)

print(ret)

# Continuation of Exploratory Data Analysis in Python

price_history(df)

histogram(df)

cum_return(df)

boxplots(df)

corr_heat_map(df)

# roll_vol(df, roll_days=20)

print(summary(df))

# Equal Weigths Portfolio Voaltiltiy & Risk Forecasting

weights = [1/len(tickers)] * len(tickers)

portfolio_df = portfolio(df, weights)

feature_df = features(df=portfolio_df, metrics=['roll_vol', 'momentum', 'vol_ratio', 'vol_change', 'roll_mean', 'lag_return'], steps=[1, 5, 20, 60])

target_df = target(df=feature_df, horizon=5)

models = ["historical_average", "persistence", "linear_regression",
          "ridge_regression", "random_forest", "xgboost", "garch"]

summary, predictions = [], {}

for model in models:

    predict_vol_df = predict_vol(df=target_df, train_dates=[start_date, "2020-12-31"], test_dates=["2021-01-01", end_date], model=model)

    predictions[model] = predict_vol_df.copy()

    rmse_df = rmse(predict_vol_df)
    mae_df = mae(predict_vol_df)
    re_df = re(predict_vol_df)

    var_es_df = var_es(predict_vol_df)

    viol = violations(var_es_df)
    viol_rate = violations_rate(viol)

    kupiec = kupiec_test(viol)
    chris = christofferesen_test(viol)

    summary.append({"Model": model, "RMSE": rmse_df, "MAE": mae_df, "RE": re_df,
        "Violation rate": viol_rate, "Kupiec": kupiec, "Christoffersen": chris[0]})

summary = pd.DataFrame(summary)

print(summary)

for model in models:

    model_data = predictions[model]["result"]

    first_dates = model_data.groupby(pd.to_datetime(model_data["date"]).dt.year)["date"].first().values
    first_years = pd.to_datetime(first_dates).year

    # Volatiltiy Prediction vs Actual Data Plot

    targ_col = next((col for col in model_data.columns if col.startswith("target_")), None)

    plt.figure(figsize=(12,8))
    plt.plot(model_data["date"], model_data["prediction"], lw=0.75, color='red', label=f"{model} prediction")
    plt.plot(model_data["date"], model_data[targ_col], lw=0.75, color='blue', label='historical data')

    plt.title(f"Volatility Prediction vs Actual Data, {model}")
    plt.ylabel("Volatiltiy")
    plt.xlabel("Year")
    plt.xticks(first_dates, first_years, rotation=45)
    plt.legend(loc=0)
    plt.grid(True, alpha=0.2, color = "grey", ls='--', lw = 1)
    plt.show()

    # VaR Violations Plot

    model_data = predictions[model]

    var_data = var_es(df=model_data, confidence=95)

    var_col = next((col for col in var_data.columns if col.startswith("var_")), None)

    plt.figure(figsize=(12, 8))

    plt.plot(var_data["date"], var_data["realized_return"], lw= 0.75, label="Realized return")
    plt.plot(var_data["date"], var_data[var_col], lw= 0.75, label=f"{model}, {var_col}")

    viol = violations(var_data)

    plt.scatter(var_data.loc[viol, "date"], var_data.loc[viol, "realized_return"], 
                color="red", s=10, label="Violation")
    
    plt.title(f"VaR Violations, {model}")
    plt.ylabel("Log Return")
    plt.xlabel("Year")
    plt.xticks(first_dates, first_years, rotation=45)
    plt.legend(loc=0)
    plt.grid(True, alpha=0.2, color = "grey", ls='--', lw = 1)
    plt.show()

    # Rolling Violation Plot

    window = 60

    viol = viol.rolling(window=window, min_periods=1).mean().dropna()

    plt.figure(figsize=(12,8))
    plt.plot(var_data["date"], viol, label=f'{window}-Day Rolling Violation Rate')

    plt.title(f"{window}-Day Rolling Violation Rate, {model}")
    plt.ylabel("Violation Rate")
    plt.xlabel("Year")
    plt.xticks(first_dates, first_years, rotation=45)
    plt.legend(loc=0)
    plt.grid(True, alpha=0.2, color = "grey", ls='--', lw = 1)
    plt.show()