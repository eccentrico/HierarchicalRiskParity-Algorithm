import Class
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
import numpy as np

tickers= ['MSFT', 'AAPL', 'GOOG', 'V']

data= yf.download(tickers, start='2010-01-01', end= '2023-08-31')['Adj Close']
returns= data.pct_change().dropna()

hrp= Class.HierarchicalRiskParity(returns)

hrp.cal_correlation_matrix()
hrp.per_clustering()
hrp.all_weights()
hrp.plot_dendogram()

#BACKTESTING
#Mean returns and Cov matrix
mean_returns= returns.mean()
cov_matrix= returns.cov()

#Weights for Mean-Variance portfolio 
weights_mean_variance = np.array([0.25, 0.25, 0.25, 0.25])

#cal mean-var returns
mean_var_returns = np.dot(mean_returns, weights_mean_variance)

#Risk for Mean_Var Portf
mean_var_risk = np.sqrt(np.dot(weights_mean_variance, np.dot(cov_matrix, weights_mean_variance)))

#Returns for HRP portf
hrp_returns= np.dot(mean_returns, hrp.weights)
#Cal HRP portf risk
hrp_risk = np.sqrt(np.dot(hrp.weights, np.dot(cov_matrix, hrp.weights)))

#Printing the results
print('Mean Var Portfolio')
print(f'Returns= {mean_var_returns}')
print(f"Risk: {mean_var_risk}")
print('HRP Portfolio')
print(f"Returns: {hrp_returns}")
print(f'Risk: {hrp_risk}')