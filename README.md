# Financial Volatility & Risk Forecasting

Project by Alexsey Chernichenko. July 2026.

# Project Goal

# Methodology

# Background

# Structure

# Results

## Explaratory Data Analysis

<img width="1071" height="724" alt="Снимок экрана 2026-07-23 в 16 05 03" src="https://github.com/user-attachments/assets/52ea6905-05e0-4d87-84a8-6ff18100cb57" />

<img width="1027" height="748" alt="Снимок экрана 2026-07-23 в 16 04 43" src="https://github.com/user-attachments/assets/ce8bfff1-a06b-4ede-b9cb-4ba43653a686" />

<img width="1058" height="711" alt="Снимок экрана 2026-07-23 в 16 04 10" src="https://github.com/user-attachments/assets/c31c5772-d0b4-4440-ba93-17548dca517c" />

<img width="937" height="700" alt="Снимок экрана 2026-07-23 в 16 05 50" src="https://github.com/user-attachments/assets/fa73e704-965e-41bc-a91e-bb1e58405084" />

<img width="1100" height="698" alt="Снимок экрана 2026-07-23 в 16 05 22" src="https://github.com/user-attachments/assets/91cecffd-0efd-49ba-837d-0b8c549ef778" />

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

<img width="1075" height="742" alt="Снимок экрана 2026-07-23 в 16 26 57" src="https://github.com/user-attachments/assets/b8f31045-5865-4086-b180-9f2ae14d12af" />

<img width="1048" height="725" alt="Снимок экрана 2026-07-23 в 16 20 49" src="https://github.com/user-attachments/assets/70785c51-e81e-4e03-a97a-e2b37d11c9f9" />

<img width="1080" height="723" alt="Снимок экрана 2026-07-23 в 16 40 35" src="https://github.com/user-attachments/assets/eb1a63af-91e6-4671-a387-42e97bfa9d77" />

### Persistence



### Linear Regression

### Ridge Regression

### Random Forest

### XGBoost

### GARCH

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
