import numpy as np

def features(df, metrics, steps):

    metrics = sorted(set(metrics))
    steps = sorted(set(steps))

    valid_metrics = ['lag_return', 'roll_mean', 'roll_vol', 'momentum', 'vol_ratio', 'vol_change']

    new_df = df[["date", "log_return"]].copy()

    if isinstance(steps, int):
        steps = [steps]

    if isinstance(metrics, str):
        metrics = [metrics]

    if isinstance(steps, list) and isinstance(metrics, list):

        if set(metrics).issubset(valid_metrics):

            if ( all(isinstance(step, int) for step in steps) 
                and all(step > 0 for step in steps) and len(steps) > 0 ):

                for step in steps:

                    if "lag_return" in metrics:

                        new_df[f"lag_return_{step}"] = new_df["log_return"].shift(step)

                    if "roll_mean" in metrics:

                        new_df[f"roll_mean_{step}"] = new_df["log_return"].rolling(step).mean().reset_index(level=0, drop=True)
                    
                    if "roll_vol" in metrics:    
                        
                        if step == 1:
                            
                            pass

                        else:

                            new_df[f"roll_vol_{step}"] = new_df["log_return"].ewm(step).std().reset_index(level=0, drop=True)
                            new_df[f"roll_vol_{step}"] = np.sqrt(252) * new_df[f"roll_vol_{step}"]

                    if "momentum" in metrics:

                        new_df[f"momentum_{step}"] = np.exp(new_df["log_return"].rolling(step).sum().reset_index(level=0, drop=True))
                        
                vol_steps = sorted([step for step in steps if step > 1])

                max_step = max(vol_steps)
                min_step = min(vol_steps)

                if ("roll_vol" in metrics) and ("vol_ratio" in metrics) and (len(steps) >= 2):

                    new_df[f"vol_ratio_{min_step}_{max_step}"] = new_df[f"roll_vol_{min_step}"] / new_df[f"roll_vol_{max_step}"]

                if ("roll_vol" in metrics) and ("vol_change" in metrics) and (len(steps) >= 2):

                    new_df[f"vol_change_{min_step}_{max_step}"] = new_df[f"roll_vol_{min_step}"] - new_df[f"roll_vol_{max_step}"]

            else:
                raise ValueError('Please provide a list of integer valued lags or a single integer valued lag')
        else: 
            raise ValueError('Please provide valid metrics: lag_return, roll_mean, roll_vol, momentum, vol_ratio or vol_change')

    else:
        raise ValueError('Please provide a list of integer valued lags or a single integer valued lag')

    base_cols = ["date", "log_return"]

    feature_cols = [col for col in new_df.columns if col not in base_cols]

    feature_cols = sorted(feature_cols, key=lambda x: ("_".join(x.split("_")[:-1]), 
                                                       int(x.split("_")[-1])))

    new_df = new_df[base_cols + feature_cols]

    return new_df