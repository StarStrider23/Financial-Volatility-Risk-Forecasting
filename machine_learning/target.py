from machine_learning.features import features

def target(df, horizon):

    if f"roll_vol_{horizon}" not in df.columns:
        targ = features(df, metrics="roll_vol", steps=horizon)
    else:
        targ = df.copy()

    if "log_return" not in targ.columns:
        raise ValueError("Please provide a column with logarithmic returns.")

    targ[f"target_{horizon}"] = targ[f"roll_vol_{horizon}"]
    targ[f"target_{horizon}"] = targ[f"target_{horizon}"].shift(-horizon)

    targ["realized_return"] = targ["log_return"].rolling(horizon).sum().shift(-horizon)

    targ = targ.dropna()

    return targ