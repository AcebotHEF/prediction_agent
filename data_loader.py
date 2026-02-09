import pandas as pd
import numpy as np

def get_revenue_data():
    """
    Generates a realistic revenue dataset with seasonality, trends, 
    and specific market events for AI analysis.
    """
    # Create 24 months of data (2 years)
    dates = pd.date_range(start="2023-01-01", periods=24, freq='ME')
    
    # Base trend: Growing by roughly $500/month
    base_revenue = [12000 + (i * 500) for i in range(len(dates))]
    
    # Add Seasonality: Boost Q4 (Oct, Nov, Dec) by 20%
    seasonality = []
    for date in dates:
        if date.month in [10, 11, 12]:
            seasonality.append(1.2) # 20% boost
        elif date.month in [1, 2]:
            seasonality.append(0.85) # 15% drop (Post-holiday slump)
        else:
            seasonality.append(1.0) # Normal months
            
    # Combine Base * Seasonality
    revenue = [b * s for b, s in zip(base_revenue, seasonality)]
    
    # Add Random Noise (Business fluctuations)
    noise = np.random.randint(-1500, 1500, size=len(dates))
    final_revenue = [r + n for r, n in zip(revenue, noise)]
    
    # --- Inject Anomalies for the AI to find ---
    # 1. Supply Chain Crisis (Dip)
    final_revenue[10] = final_revenue[10] * 0.6 
    
    # 2. Viral Marketing Campaign (Spike)
    final_revenue[16] = final_revenue[16] * 1.5

    df = pd.DataFrame({
        'Month': dates, 
        'Revenue': final_revenue,
        'Event Notes': [''] * len(dates) # Empty column for context
    })
    
    # Label the anomalies so the AI has context (optional, or let AI guess)
    df.loc[10, 'Event Notes'] = "Supply Chain Disruption"
    df.loc[16, 'Event Notes'] = "Viral TikTok Campaign"

    return df