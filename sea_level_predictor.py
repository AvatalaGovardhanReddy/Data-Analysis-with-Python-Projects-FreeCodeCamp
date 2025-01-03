import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load data
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data Points', color='blue', alpha=0.6)
    
    # First line of best fit (1880 to 2050)
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_extended = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_extended, label='Best Fit: 1880-2050', color='red')
    
    # Second line of best fit (2000 to 2050)
    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    sea_level_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, sea_level_recent, label='Best Fit: 2000-2050', color='green')
    
    # Add labels, title, and legend
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    # Save plot and return
    plt.savefig('sea_level_plot.png')
    return plt.gca()
