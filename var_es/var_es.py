import numpy as np
from scipy.stats import norm

def var_es(df, confidence=95):

    new_df = df["result"].copy()

    if not 1 <= confidence <= 100:
        raise ValueError("Please provide a valid confidence interval.")
    
    targ_col = next((col for col in new_df.columns if col.startswith("target_")), None)

    if targ_col is None:
        raise ValueError("No target column found.")
    
    horizon = int(targ_col.split("_")[-1])

    new_df["prediction"] = np.sqrt(horizon) * new_df["prediction"] / np.sqrt(252)

    new_df[targ_col] = np.sqrt(horizon) * new_df[targ_col] / np.sqrt(252)

    mu = np.mean(new_df["log_return"])
    sigma = new_df["prediction"]
    z = norm.ppf(confidence/100)

    new_df[f"var_{confidence}"] = horizon * mu - z * sigma
    new_df[f"es_{confidence}"] = horizon * mu - sigma * norm.pdf(z) / (1 - confidence/100)

    return new_df