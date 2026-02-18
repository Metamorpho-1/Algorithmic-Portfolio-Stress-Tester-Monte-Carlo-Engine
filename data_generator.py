
"""
Market History Generator
------------------------
This utility creates a synthetic 2-year historical dataset for Tech, Blue Chip, 
and Gold assets. We use this to establish a 'baseline' for our stress tests.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_market_baseline():
    print("Initiating synthetic market generation sequence...")
    
    # We'll generate a 2-year window (730 days)
    end_date = datetime.today()
    start_date = end_date - timedelta(days=730)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Asset Profiles: (Mean Daily Return, Daily Volatility)
    # These parameters simulate realistic risk/reward profiles for different sectors.
    asset_profiles = {
        'Tech_Growth': {'mu': 0.0008, 'sigma': 0.025}, # Aggressive
        'Blue_Chip':   {'mu': 0.0004, 'sigma': 0.012}, # Stable
        'Gold_Safe':   {'mu': 0.0001, 'sigma': 0.009}  # Conservative
    }
    
    market_data = pd.DataFrame({'Date': dates})
    
    # Using a geometric Brownian motion approach for more 'human' price curves
    for asset_name, params in asset_profiles.items():
        # Generate randomized daily returns based on the asset profile
        daily_returns = np.random.normal(params['mu'], params['sigma'], len(dates))
        
        # Convert returns to a cumulative price series starting at a $100 base
        price_evolution = 100 * np.exp(np.cumsum(daily_returns))
        market_data[asset_name] = price_evolution.round(2)
        
    # Save to CSV for the analyzer to pick up
    market_data.to_csv('market_history.csv', index=False)
    print(f"-> Baseline established. Market data saved to 'market_history.csv' ({len(dates)} days).")

if __name__ == "__main__":
    generate_market_baseline()
    