import numpy as np
import pandas as pd
import math
import statsmodels.formula.api as smf
from tools import utils

data_train = {
  "X": [0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
  "Y": [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    }
df_train = pd.DataFrame(data_train)
model = smf.ols(formula = 'Y ~ X', data=df_train).fit()
data_test = {
  "X": [0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
  "Y": [0.0, 1.0, 2.0, 3.5, 4.0, 5.0]
    }
df_test = pd.DataFrame(data_test)

y_train = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
OSR2 = 0.98
MAE = 0.083

def test_OSR2():
    assert math.isclose(utils.OSR2(model, df_test["X"], df_test["Y"], df_train["Y"]), OSR2, abs_tol = 0.01)

def test_MAE():
    assert math.isclose(utils.MAE(model, df_test["X"], df_test["Y"], df_train["Y"]), MAE, abs_tol = 0.01)