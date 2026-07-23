# Financial Volatility & Risk Forecasting

Project by Alexsey Chernichenko. July 2026.

# Project Goal

The goal of the project is twofold. Firstly, to build an end-to-end financial data pipeline that collects historical market data, stores it in a SQL database, performs exploratory data analysis and feature engineering, and finally develops statistical and machine learning models to forecast financial risk. Secondly, to evaluate whether increasingly sophisticated volatility forecasting models lead to more reliable market risk forecasts, as measured not only by prediction accuracy but also by regulatory backtesting tests.

# Methodology

This project evaluates different approaches for forecasting portfolio volatility and assessing the reliability of resulting risk estimates. The workflow consists of data collection, portfolio construction, feature engineering, volatility forecasting and VaR backtesting.

## Data and Portfolio Construction

Historical daily price data was collected using `yfinance` for the period January 2000 to July 2026 (~27.5 years). The data was stored in a SQLite database and analysed using SQL and Python.

Six assets were selected to create a diversified portfolio across multiple sectors. The selected companies represent different sectors, including semiconductors, technology, financial services, healthcare, consumer and energy.

* NVIDIA (NVDA)
* Microsoft (MSFT)
* JPMorgan Chase (JPM)
* UnitedHealth Group (UNH)
* Amazon (AMZN)
* Exxon Mobil (XOM)

Portfolio returns were calculated using equal asset weights. The assets and portfolio were analysed using statistical measures including return distributions, volatility, annualized volatility, correlations, skewness, and kurtosis.

## Feature Engineering

Daily logarithmic returns were calculated and used to construct forecasting features based only on historical information.

The following features were generated:

* lagged returns (`lag_return`)
* exponentially weighted rolling volatility (`roll_vol`)
* rolling mean (`roll_mean`)
* momentum (`momentum`)
* volatility ratio (`vol_ratio`)
* volatility change (`vol_change`)

The first four baseline features were generated for different time horizons such as 1, 5, 20 and 60 days. The last two features were derived from roll_vol_5 and roll_vol_60 metrics. The prediction target was future annualized realized volatility over a five-day horizon.

## Volatility Forecasting

The test period lasted from 2000 to 2020 while the forecasting period covered 2021–2026. Seven models were evaluated:

* Historical average volatility (`historical_average`)
* Persistence model (`persistence`)
* Linear regression (`linear_regression`)
* Ridge regression (`ridge_regression`)
* Random Forest (`random_forest`)
* XGBoost (`xgboost`)
* GARCH(1,1) (`garch`)

The first two models were used as benchmarks, while the remaining models represented statistical and machine learning-based forecasting approaches.

## Risk Estimation and Backtesting

Forecasted volatility was used to calculate Value-at-Risk (VaR) and Expected Shortfall (ES). Model performance was evaluated using both volatility forecasting accuracy and risk metrics.

Forecasting performance was measured using:

* Root Mean Squared Error (RMSE)
* Mean Absolute Error (MAE)
* Relative Error (RE)

Risk performance was evaluated using:

* VaR violation rate
* Kupiec unconditional coverage test
* Christoffersen independence test

Additional analysis included feature importance evaluation for machine learning models and investigation of violation clustering during periods of changing market volatility.

Although a necessary level of background is given below, the reader may also familiarize oneself with the following project: https://github.com/StarStrider23/1-day-Value-at-Risk-Expected-Shortfall-Forecasting-Project. The project includes some further discussion on GARCH(1,1), VaR and ES.

# Background

## Feature Engineering

Forecasting future volatility requires transforming historical returns into informative explanatory variables. All features used in this project were constructed exclusively from past observations to avoid the bias related to future leakage.

The following features are considered:

* **Lagged returns (`lag_return`)** represent previous daily returns and capture short-term dependencies in the return series.
* **Rolling mean (`roll_mean`)** measures the average return over a moving window and provides information about recent market trends.
* **Exponentially weighted rolling volatility (`roll_vol`)** similar to the rolling mean, but for volatility, however it is exponentially weighted which means that it assigns greater importance to more recent observations.
* **Momentum** represents accumulated historical returns and is used to identify persistent upward or downward price movements.
* **Volatility ratio (`vol_ratio`)** compares short-term and long-term volatility and can indicate transitions between different volatility regimes.
* **Volatility change (`vol_change`)** measures the difference between short-term and long-term volatility and reflects the speed at which market uncertainty changes.

Using multiple rolling windows allows the models to capture both short-term market fluctuations and longer-term volatility behaviour.

## Volatility Forecasting Models

Several forecasting approaches are evaluated, ranging from simple benchmark methods to machine learning algorithms and classical econometric models.

### Historical Average

The historical average model forecasts future volatility using the average historical volatility observed during the training period. Although simple, it provides a useful benchmark for evaluating more advanced forecasting methods.

### Persistence Model

The persistence model assumes that future volatility equals the most recently observed volatility. Due to the strong persistence commonly observed in financial volatility, this model often provides a surprisingly competitive baseline.

### Linear Regression

Linear regression models future volatility as a linear combination of the engineered features. The model assumes a linear relationship between historical market characteristics and future realized volatility.

### Ridge Regression

Ridge regression extends linear regression by introducing L2 regularization. The regularization term reduces the influence of highly correlated features and helps improve model stability while reducing the risk of overfitting.

### Random Forest

Random Forest is an ensemble learning algorithm that combines predictions from multiple decision trees. By averaging the outputs of many trees, Random Forest can model nonlinear relationships while reducing prediction variance compared with a single decision tree.

### XGBoost

XGBoost (Extreme Gradient Boosting) is a gradient boosting algorithm that constructs decision trees sequentially. Each new tree attempts to correct the prediction errors of the previous ensemble, enabling the model to learn complex nonlinear relationships between historical features and future volatility. Regularization techniques incorporated within XGBoost also help control model complexity.

### GARCH(1,1)

GARCH (The Generalized Autoregressive Conditional Heteroskedasticity) model is one of the most widely used econometric models for volatility forecasting. Unlike machine learning models, GARCH directly models the conditional variance of financial returns by relating current volatility to previous volatility and previous return shocks. The model is particularly well suited for financial time series because it captures volatility clustering observed in asset returns. 

## Portfolio Risk Measures

Accurate volatility forecasts are essential for estimating portfolio risk. In this project, forecasted volatility is used to calculate two widely applied risk measures, i.e. Value-at-Risk (VaR) and Expected Shortfall (ES).

### Value-at-Risk (VaR)

Value-at-Risk estimates the maximum expected portfolio loss over a specified time horizon for a given confidence level. For example, a one-day 95% VaR of 2% indicates that losses greater than 2% are expected to occur on approximately 5% of trading days.

### Expected Shortfall (ES)

Expected Shortfall measures the average loss conditional on the VaR threshold being exceeded. Unlike VaR, ES provides information about the magnitude of extreme losses and is therefore considered a more informative measure of tail risk.

## Model Evaluation

Besides the error 

The **Kupiec unconditional coverage test** evaluates whether the observed number of VaR violations is consistent with the selected confidence level.

The **Christoffersen independence test** evaluates whether VaR violations occur independently over time. Passing the Kupiec test indicates correct long-run coverage, whereas passing the Christoffersen test additionally requires that violations do not occur in clusters. Together, these tests provide a comprehensive assessment of the reliability of the estimated market risk.


# Structure

# Results

## Explaratory Data Analysis

<img width="1058" height="711" alt="Снимок экрана 2026-07-23 в 16 04 10" src="https://github.com/user-attachments/assets/c31c5772-d0b4-4440-ba93-17548dca517c" />

<img width="1027" height="748" alt="Снимок экрана 2026-07-23 в 16 04 43" src="https://github.com/user-attachments/assets/ce8bfff1-a06b-4ede-b9cb-4ba43653a686" />

<img width="937" height="700" alt="Снимок экрана 2026-07-23 в 16 05 50" src="https://github.com/user-attachments/assets/fa73e704-965e-41bc-a91e-bb1e58405084" />

<img width="1100" height="698" alt="Снимок экрана 2026-07-23 в 16 05 22" src="https://github.com/user-attachments/assets/91cecffd-0efd-49ba-837d-0b8c549ef778" />

<img width="1071" height="724" alt="Снимок экрана 2026-07-23 в 16 05 03" src="https://github.com/user-attachments/assets/52ea6905-05e0-4d87-84a8-6ff18100cb57" />

| Asset |  Mean  | Volatility | Annual Volatility | Min    | Max   | Skew   | Kurtosis |
| ----- | ------ | ---------- | ----------------- | ------ | ----- | ------ | -------- |
| NVDA  | 0.0011 | 0.037      | 0.585             | -0.434 | 0.354 | -0.209 | 12.981   |
| MSFT  | 0.0003 | 0.019      | 0.301             | -0.170 | 0.179 | -0.163 | 9.212    |
| JPM   | 0.0003 | 0.023      | 0.366             | -0.232 | 0.224 | 0.207  | 14.688   |
| UNH   | 0.0006 | 0.020      | 0.320             | -0.253 | 0.298 | -0.531 | 23.015   |
| AMZN  | 0.0006 | 0.030      | 0.481             | -0.285 | 0.296 | 0.419  | 13.105   |
| XOM   | 0.0002 | 0.017      | 0.264             | -0.150 | 0.159 | -0.089 | 8.274    |

## ???

### Historical Average

<img width="1048" height="725" alt="Снимок экрана 2026-07-23 в 16 20 49" src="https://github.com/user-attachments/assets/70785c51-e81e-4e03-a97a-e2b37d11c9f9" />

<img width="1080" height="723" alt="Снимок экрана 2026-07-23 в 16 40 35" src="https://github.com/user-attachments/assets/eb1a63af-91e6-4671-a387-42e97bfa9d77" />

<img width="1075" height="742" alt="Снимок экрана 2026-07-23 в 16 26 57" src="https://github.com/user-attachments/assets/b8f31045-5865-4086-b180-9f2ae14d12af" />

### Persistence

<img width="1065" height="731" alt="Снимок экрана 2026-07-23 в 16 21 41" src="https://github.com/user-attachments/assets/af6dd959-58f4-4df6-9f37-3355bbfc376c" />

<img width="1080" height="730" alt="Снимок экрана 2026-07-23 в 16 40 53" src="https://github.com/user-attachments/assets/457583fe-176b-4d03-80b9-59e87165580a" />

<img width="1073" height="738" alt="Снимок экрана 2026-07-23 в 16 28 23" src="https://github.com/user-attachments/assets/91e52c8b-30e2-4dcf-81c3-60b6b3f7ec61" />

### Linear Regression

<img width="1055" height="736" alt="Снимок экрана 2026-07-23 в 16 28 41" src="https://github.com/user-attachments/assets/5a9449b7-c0fc-451c-91c0-6be588a47b8a" />

<img width="1073" height="731" alt="Снимок экрана 2026-07-23 в 16 41 10" src="https://github.com/user-attachments/assets/e7a6cbbb-51d2-450e-ab27-ee08aee8e460" />

<img width="1074" height="746" alt="Снимок экрана 2026-07-23 в 16 32 46" src="https://github.com/user-attachments/assets/8eaaa189-68dd-45a9-8a5e-be727ba47c57" />

### Ridge Regression

<img width="1051" height="729" alt="Снимок экрана 2026-07-23 в 16 33 04" src="https://github.com/user-attachments/assets/0416eb8b-8a2e-4268-baff-2fe9a3d6f1bb" />

<img width="1076" height="735" alt="Снимок экрана 2026-07-23 в 16 41 27" src="https://github.com/user-attachments/assets/c445b9e8-895a-4faf-bbde-16542b164c02" />

<img width="1075" height="738" alt="Снимок экрана 2026-07-23 в 16 33 46" src="https://github.com/user-attachments/assets/c7437d0f-6f1d-444a-b075-a445dd129d39" />

### Random Forest

<img width="1047" height="733" alt="Снимок экрана 2026-07-23 в 16 34 04" src="https://github.com/user-attachments/assets/4568c035-24ff-4a50-9e53-1b62fbaa4334" />

<img width="1077" height="732" alt="Снимок экрана 2026-07-23 в 16 41 44" src="https://github.com/user-attachments/assets/2c470dba-6a58-45eb-bdd1-1c10f4934575" />

<img width="1082" height="733" alt="Снимок экрана 2026-07-23 в 16 34 47" src="https://github.com/user-attachments/assets/2c3069d4-f63a-42ac-b9bd-690ca5925e30" />

### XGBoost

<img width="1070" height="733" alt="Снимок экрана 2026-07-23 в 16 35 04" src="https://github.com/user-attachments/assets/983ed0ed-9c26-4eb7-b655-d6b57d0dca54" />

<img width="1070" height="725" alt="Снимок экрана 2026-07-23 в 16 42 06" src="https://github.com/user-attachments/assets/04ccce93-0a98-42e4-bbb4-0ea011251e06" />

<img width="1087" height="734" alt="Снимок экрана 2026-07-23 в 16 53 08" src="https://github.com/user-attachments/assets/b8d399f0-d82d-4dca-9886-04deec0ef614" />

### GARCH

<img width="1027" height="723" alt="Снимок экрана 2026-07-23 в 16 38 18" src="https://github.com/user-attachments/assets/64b1d0fc-ec0e-46b3-9ec4-44d9a216a0c2" />

<img width="1069" height="728" alt="Снимок экрана 2026-07-23 в 16 42 28" src="https://github.com/user-attachments/assets/cec152a9-3dc9-43e0-97f1-94ba3378b202" />

<img width="1074" height="731" alt="Снимок экрана 2026-07-23 в 16 38 37" src="https://github.com/user-attachments/assets/d84b77fc-ac05-40d7-abe8-6de96779b0dd" />

### Summary 

|       Model        |  RMSE  |   MAE  |   RE   |  Violation rate |  Kupiec  |  Christoffersen |
| ------------------ | ------ | ------ | ------ | --------------- | -------- | --------------- |
| historical_average | 0.0988 | 0.0825 | 0.505  |     0.0371      |  5.223   |     125.411     |
|     persistence    | 0.0583 | 0.0422 | 0.113  |     0.0488      |  0.0421  |     113.247     |
|  linear_regression | 0.0496 | 0.0352 | 0.0623 |     0.0575      |  1.570   |     138.063     |
|  ridge_regression  | 0.0497 | 0.0353 | 0.0622 |     0.0590      |  2.217   |     139.684     |
|  random_forest     | 0.0507 | 0.0361 | 0.0800 |     0.0539      |  0.428   |     144.441     |
|     xgboost        | 0.0530 | 0.0376 | 0.0544 |     0.0626      |  4.288   |     127.321     |
|      garch         | 0.0574 | 0.0432 | 0.171  |     0.0444      |  0.931   |     136.229     |

# Discussion

# Conclusion
