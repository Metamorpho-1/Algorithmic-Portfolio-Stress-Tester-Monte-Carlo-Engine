"""
Algorithmic Portfolio Stress Tester
-----------------------------------
This engine performs a Monte Carlo simulation to stress-test a given portfolio 
against 1,000 potential future market scenarios.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any

def run_portfolio_simulation() -> None:
    print("System: Loading historical volatility matrices...")
    
    try:
        # Load our synthetic market history
        history_df = pd.read_csv('market_history.csv', parse_dates=['Date'])
    except FileNotFoundError:
        print("CRITICAL ERROR: 'market_history.csv' not found. Run the generator first.")
        return

    # --- Step 1: Data Preparation ---
    # Strip dates to focus on raw price movement
    prices_only = history_df.drop('Date', axis=1)
    
    # Calculate Log Returns: The gold standard for financial statistical analysis
    log_returns = np.log(prices_only / prices_only.shift(1)).dropna()

    # --- Step 2: Define Portfolio Strategy ---
    # Strategy: 50% Aggressive Tech, 30% Stable Blue Chip, 20% Defensive Gold
    allocation_weights = np.array([0.5, 0.3, 0.2])
    initial_capital = 100_000 # Starting with $100,000
    
    # Compute the covariance matrix (how assets move in relation to each other)
    covariance_matrix = log_returns.cov()
    mean_daily_return = log_returns.mean()
    
    # Calculate the portfolio's overall mean and risk (standard deviation)
    expected_portfolio_mean = np.sum(mean_daily_return * allocation_weights)
    portfolio_volatility = np.sqrt(
        np.dot(allocation_weights.T, np.dot(covariance_matrix, allocation_weights))
    )

    # --- Step 3: Monte Carlo Engine ---
    # We simulate 1,000 futures over the next 252 trading days (1 standard year)
    num_sims = 1000
    future_days = 252
    
    # Generate 1,000 random return paths in one high-speed vectorized operation
    future_scenarios = np.random.normal(
        expected_portfolio_mean, 
        portfolio_volatility, 
        (future_days, num_sims)
    )
    
    # Project price paths starting from our initial capital
    value_projections = initial_capital * np.exp(np.cumsum(future_scenarios, axis=0))

    # --- Step 4: Risk Assessment ---
    # We look at the 'Value at Risk' (VaR) at the 5th percentile
    final_day_values = value_projections[-1, :]
    risk_threshold_5pct = np.percentile(final_day_values, 5)
    median_growth = np.median(final_day_values)
    
    print("\n" + "="*40)
    print("PORTFOLIO RISK ASSESSMENT REPORT")
    print("="*40)
    print(f"Initial Investment:  ${initial_capital:,.2f}")
    print(f"Median Prediction:   ${median_growth:,.2f}")
    print(f"5% Risk Threshold:   ${risk_threshold_5pct:,.2f}")
    print(f"Potential Max Loss:  ${(initial_capital - risk_threshold_5pct):,.2f}")
    print("="*40 + "\n")

    # --- Step 5: Visualizing the 'Fan Chart' ---
    plt.style.use('dark_background')
    plt.figure(figsize=(12, 7))
    
    # Plot all 1,000 simulations with very low opacity to show density
    plt.plot(value_projections, color='cyan', alpha=0.03)
    
    # Highlight the key mathematical markers
    plt.axhline(y=initial_capital, color='white', linestyle='--', label='Initial Capital')
    plt.plot(np.median(value_projections, axis=1), color='#10B981', linewidth=2, label='Median Trend')
    plt.axhline(y=risk_threshold_5pct, color='#EF4444', linestyle=':', linewidth=2, label='5% VaR (Risk Level)')

    plt.title("Monte Carlo Stress Test: 1,000 Future Scenarios", fontsize=16, fontweight='bold')
    plt.xlabel("Days into Future")
    plt.ylabel("Portfolio Value ($)")
    plt.legend(frameon=False)
    plt.grid(alpha=0.1)
    
    print("Dashboard: Rendering probabilistic outcomes...")
    plt.show()

if __name__ == "__main__":
    run_portfolio_simulation()