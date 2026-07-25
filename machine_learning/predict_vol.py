import numpy as np
import pandas as pd

import warnings

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from arch import arch_model

def predict_vol(df, train_dates, test_dates, model, baseline_feature="roll_vol_20"):

    estimator = None

    df_dates = df["date"].unique()

    if (baseline_feature not in df.columns) and model in ["histroical_average", "persistence"]:
        raise ValueError('Provide a valid baseline_feature argument that is present in the data.')

    if train_dates[0] < df_dates.min():
        warnings.warn(f"The date {train_dates[0]} is not present in the data. The earliest date available is {df_dates.min()}.", 
                      DeprecationWarning, stacklevel=2)
        train_dates[0] = df_dates.min()

    if test_dates[1] > df_dates.max():
        warnings.warn(f"The date {test_dates[1]} is not present in the data. The latest date available is {df_dates.max()}.",
                       DeprecationWarning, stacklevel=2)
        test_dates[1] = df_dates.max()   

    if ( len(train_dates) == 2 and len(test_dates) == 2 
        and train_dates[0] < train_dates[1] and train_dates[1] < test_dates[0]
        and test_dates[0] < test_dates[1]):

        targ_col = next((col for col in df.columns if col.startswith("target_")), None)

        train = df[df["date"].between(f"{train_dates[0]}", f"{train_dates[1]}")].copy().reset_index(drop=True)
        x_train = train.drop(columns=["date", targ_col, "realized_return"]).copy().reset_index(drop=True)
        y_train = train[targ_col].copy().reset_index(drop=True)

        test = df[df["date"].between(f"{test_dates[0]}", f"{test_dates[1]}")].copy().reset_index(drop=True)
        x_test = test.drop(columns=["date", targ_col, "realized_return"]).copy().reset_index(drop=True)
        y_test = test[targ_col].copy().reset_index(drop=True)

        if train.empty:
            raise ValueError("No training observations available in the specified period.")
        elif test.empty:
            raise ValueError("No test observations available in the specified period.")

    else:
        raise ValueError('Please provide a set of valid train and test dates: ' \
        'two train and two test dates that do not overlap and are in the chronological order.')

    estimators = {
        "linear_regression": Pipeline([("scaler", StandardScaler()), ("linear", LinearRegression())]),

        "ridge_regression": Pipeline([("scaler", StandardScaler()), ("ridge", Ridge(alpha=1.0))]),

        "random_forest": RandomForestRegressor(n_estimators=1500, max_depth=4,
                        min_samples_leaf=10, max_features=0.7, random_state=42, n_jobs=-1),

        "xgboost": XGBRegressor(n_estimators=1500, learning_rate=0.05, max_depth=4, min_child_weight=5,
                    subsample=0.7, colsample_bytree=0.7, reg_alpha=0.1, reg_lambda=5,
                    objective="reg:squarederror", random_state=42)
    }

    if model in estimators:
        estimator = estimators[model]
        estimator.fit(x_train, y_train)

        predictions = estimator.predict(x_test)
        
    elif model == "historical_average":
        mean_vol = np.mean(train[baseline_feature])
        predictions = np.repeat(mean_vol, len(y_test))
        
    elif model == "persistence":
        predictions = test[baseline_feature]

    elif model == "garch":

        predictions = []
        history = train["log_return"].copy()
        horizon = int(targ_col.split("_")[-1])

        for i in range(len(test)):

            garch = arch_model(history * 100, mean="Constant", vol="GARCH", p=1, q=1, dist="t")

            fitted = garch.fit(disp="off")

            forecast = fitted.forecast(horizon=horizon, reindex=False)

            variance = forecast.variance.iloc[-1]

            volatility = np.sqrt(variance.mean())

            volatility = np.sqrt(252) * volatility / 100

            predictions.append(volatility)

            history = pd.concat([history, test["log_return"].iloc[i:i+1]])

    else:
        raise ValueError('Please provide a valid model: historical_average, persistence, ' \
                            'linear_regression, ridge_regression, random_forest, xgboost or garch')
    
    prediction = pd.DataFrame({"prediction": predictions, targ_col: y_test})

    if isinstance(estimator, Pipeline):
        estimator = estimator[-1]

    if hasattr(estimator, "coef_"):
        extra = pd.Series(estimator.coef_, index=x_train.columns, name="importance")

    elif hasattr(estimator, "feature_importances_"):
        extra = pd.Series(estimator.feature_importances_, index=x_train.columns, name="importance")

    elif model == "garch":
        extra = fitted.params

    else:
        extra = None

    prediction["date"] = test["date"]
    prediction["log_return"] = test["log_return"]
    prediction["realized_return"] = test["realized_return"]

    result = {"model": model, "result": prediction, "model_info": extra}
    
    return result