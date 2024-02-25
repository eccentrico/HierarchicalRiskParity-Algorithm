Hierarchical Risk Parity Algorithm

This repository contains an implementation of the Hierarchical Risk Parity (HRP) algorithm.

 Overview

The Hierarchical Risk Parity (HRP) algorithm is a portfolio optimization technique that seeks to maximize portfolio diversification by considering the hierarchical structure of the assets in the portfolio. It allocates weights to assets based on their covariance matrix, aiming to achieve a balanced risk-return profile.

 Features

- Implementation of the HRP algorithm in Python.
- Efficient computation of the optimal portfolio weights.
- Support for various asset classes and data sources.

 Usage

To use the HRP algorithm in your project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/eccentrico/HierarchicalRiskParity-Algorithm.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Import the `HierarchicalRiskParity` class and instantiate it with your asset data.

   from hrp import HierarchicalRiskParity
   
   # Initialize HRP with asset data
   hrp = HierarchicalRiskParity(asset_returns)
   ```

4. Compute the optimal portfolio weights using the `compute_weights` method.

   ```python
   # Compute portfolio weights
   weights = hrp.compute_weights()
   ```

5. Use the computed weights to construct your portfolio.


Contributions to this project are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request.

