import numpy as np

def OSR2(model, X_test, y_test, y_train):
	"""
	Calculates R-squared coefficient of determination

	Inputs:
		model: statsmodels.formula.api model object
		X_test: test features
		y_test: test target variable
		y_train: training target variable

	Outputs:
		R-squared coefficient of determination
	"""
	y_pred = model.predict(X_test)
	SSE = np.sum((y_test - y_pred)**2)
	SST = np.sum((y_test - np.mean(y_train))**2)
	return 1 - SSE/SST

def MAE(model, X_test, y_test, y_train):
	"""
	Calculates mean absolute error

	Inputs:
		model: statsmodels.formula.api model object
		X_test: test features
		y_test: test target variable
		y_train: training target variable

	Outputs:
		mean absolute value
	"""
	y_pred = model.predict(X_test)
	return sum(abs(y_test - y_pred)) / len(y_test)