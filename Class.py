import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
import numpy as np

tickers= ['JPM', 'BAC', 'C', 'WFC']

data= yf.download(tickers, start='2010-01-01', end= '2023-08-31')
returns= data.pct_change().dropna()
class HierarchicalRiskParity:
    def __init__(self, returns):
        self.returns = returns
        self.correlation_matrix = None
        self.linkage_matrix = None
        self.weights = None

    def cal_correlation_matrix(self):
        self.correlation_matrix = self.returns.corr()

    def per_clustering(self):
        self.linkage_matrix = linkage(self.correlation_matrix, method="single")

    def all_weights(self):
        inverse_variance = np.diag(np.linalg.inv(self.correlation_matrix))
        risk_contributions = inverse_variance / np.sum(inverse_variance)
        self.weights = risk_contributions / np.sum(risk_contributions)
        # Reshaping the weights.
        self.weights = self.weights.reshape(-1)

    def plot_dendogram(self):
        dendrogram(self.linkage_matrix)
        plt.title('Hierarchical Clustering')
        plt.xlabel('Asset')
        plt.ylabel('Distance')
        plt.show()
