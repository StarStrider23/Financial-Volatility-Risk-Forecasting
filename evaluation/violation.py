def violations(df):

    var_col = next((col for col in df.columns if col.startswith("var_")), None)

    if var_col is None:
        raise ValueError("No VaR column found.")

    violations = df["realized_return"] < df[var_col]

    return violations

def violations_rate(violations):
    
    rate = violations.sum() / len(violations)

    return rate