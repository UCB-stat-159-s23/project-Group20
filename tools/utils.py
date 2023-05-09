import numpy as np

def OSR2(model, X_test, y_test, y_train):
    y_pred = model.predict(X_test)
    SSE = np.sum((y_test - y_pred)**2)
    SST = np.sum((y_test - np.mean(y_train))**2)
    return 1 - SSE/SST

def MAE(model, X_test, y_test, y_train):
    y_pred = model.predict(X_test)
    return sum(abs(y_test - y_pred)) / len(y_test)