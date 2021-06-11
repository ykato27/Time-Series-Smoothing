import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_log_error


def _mape(true, pred):  
    """
    MAPEを計算する
    
    Args:
        true (np.array) : 実測値
        pred (np.array) : 予測値

    Returns:
        np.array        : mapeの計算結果
    
    """
    
    return np.mean(np.abs((true - pred) / true)) * 100


def _smape(true, pred):
    """
    SMAPEを計算する
    
    Args:
        true (np.array) : 実測値
        pred (np.array) : 予測値

    Returns:
        np.array        : smapeの計算結果
    
    """
    
    return 100/len(true) * np.sum(2 * np.abs(pred - true) / (np.abs(pred) + np.abs(true)))


def eval_metric(true, pred):
    """
    各評価指標を計算する
    
    Args:
        true (np.array) : 実測値
        pred (np.array) : 予測値

    Returns:
        (pd.DataFrame)  :
            R2    : R2
            MAE   : MAE
            MSE   : MSE
            RMSE  : RMSE
            RMSLE : RMSLE
            MAPE  : MAPE
            SMAPE : SMAPE            
    
    """
    
    r2 = r2_score(true, pred)
    
    mae = mean_absolute_error(true, pred)
    
    mse = mean_squared_error(true, pred, squared=True)
    
    rmse = mean_squared_error(true, pred, squared=False)
    
    # RMSLEは、実測値<0 or 予測値<0 の場合は計算対象外とする
    rmsle_sample = (true >= 0) & (pred >= 0)
    
    # RMSLEの計算対象外のサンプルが一つも残らない場合はNaNを返す
    if rmsle_sample.sum() != 0:
        rmsle = np.sqrt(
            mean_squared_log_error(
                true[rmsle_sample], pred[rmsle_sample]
            )
        )
    else:
        rmsle = np.nan
    
    mape = _mape(true, pred)
    
    smape = _smape(true, pred)
    
    return pd.DataFrame(
        [[r2, mae, mse, rmse, rmsle, mape, smape]],
        columns=['R2', 'MAE', 'MSE', 'RMSE', 'RMSLE', 'MAPE', 'SMAPE'],
    )