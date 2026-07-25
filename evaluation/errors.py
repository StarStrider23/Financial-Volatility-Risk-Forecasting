import numpy as np

def rmse(df):

    df = df["result"].copy()

    targ_col = next((col for col in df.columns if col.startswith("target_")), None)

    rmse = np.sqrt( np.mean( (df["prediction"] - df[targ_col])**2 ) )

    return rmse

def mae(df):

    df = df["result"].copy()

    targ_col = next((col for col in df.columns if col.startswith("target_")), None)

    mae = np.mean( np.abs( (df["prediction"] - df[targ_col]) ) )

    return mae

def re(df):

    df = df["result"].copy()

    targ_col = next((col for col in df.columns if col.startswith("target_")), None)

    re = np.mean( (df["prediction"] - df[targ_col]) / df[targ_col] )

    return re
