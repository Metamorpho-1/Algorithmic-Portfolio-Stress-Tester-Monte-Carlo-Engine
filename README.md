## Algorithmic Portfolio Stress Tester (Monte Carlo Engine)

Hey there!  Welcome to my quantitative finance project. 

I built this engine to solve a common problem in personal finance: most people only look at "average" returns, but they don't prepare for "worst-case" volatility. This tool uses **Monte Carlo Simulations** to stress-test a three-asset portfolio (Aggressive Tech, Stable Blue Chip, and Defensive Gold) against 1,000 potential future market scenarios.

## Core Features

* **Vectorized Simulation Engine:** Built with high-performance `numpy` vectorization. Instead of using slow Python loops, the engine generates 1,000 independent futures in milliseconds.
* **Geometric Brownian Motion (GBM):** Implements industry-standard price modeling logic. It ensures the simulated price paths respect the asset's historical mean and volatility "DNA."
* **Risk Metrics (VaR):** Calculates the **5% Value at Risk (VaR)**. This provides a mathematical threshold for the "worst-case scenario," helping investors understand their true downside exposure.
* **Probabilistic Dashboard:** Utilizes a custom-styled "Fan Chart" in `matplotlib` to visualize the density of all possible outcomes, highlighting the median trend versus the risk-zone.

## Getting Started

### Prerequisites
You will need Python installed along with the essential data science stack:
  ```bash
pip install pandas numpy matplotlib

Installation & Usage
Clone the project:

  ```bash
git clone [https://github.com/YOUR-USERNAME/portfolio-stress-tester.git](https://github.com/YOUR-USERNAME/portfolio-stress-tester.git)
cd portfolio-stress-tester
Establish the Market Baseline:

  ```bash
python generate_market_data.py
This creates 730 days of historical pricing data based on asset class volatility.

Run the Stress Test:

 ```bash
python stress_tester.py


🧮 How the Math Works

The engine follows a professional quantitative workflow:

1. Log Returns: Converts raw prices to logarithmic returns to normalize data for statistical modeling.

2. Covariance Mapping: Calculates how assets move in relation to each other using pandas.

3. Random Walk Simulation: Uses a normal distribution of returns to simulate a "Random Walk" for each of the 1,000 scenarios.

4. Compounding: Accumulates those returns over 252 trading days to show the final portfolio value.

## What I Learned

This project solidified my understanding of:

1.Numerical Optimization: Replacing nested loops with vectorized NumPy operations for massive performance gains.

2.Probabilistic Modeling: Using Monte Carlo methods to handle uncertainty in financial data.

3.Clean Architecture: Separating data generation from analysis to create a modular, scalable codebase.
