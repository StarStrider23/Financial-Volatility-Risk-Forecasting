# Financial Volatility & Risk Forecasting

Project by Alexsey Chernichenko. July 2026.

# Project Goal

# Methodology

# Background

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

<img width="1075" height="742" alt="Снимок экрана 2026-07-23 в 16 26 57" src="https://github.com/user-attachments/assets/b8f31045-5865-4086-b180-9f2ae14d12af" />

<img width="1080" height="723" alt="Снимок экрана 2026-07-23 в 16 40 35" src="https://github.com/user-attachments/assets/eb1a63af-91e6-4671-a387-42e97bfa9d77" />

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

<img width="1074" height="731" alt="Снимок экрана 2026-07-23 в 16 38 37" src="https://github.com/user-attachments/assets/96e0ced6-1343-4b80-b6c1-0d45929f7c2d" />


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
