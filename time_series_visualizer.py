import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def page_view_time_series_visualizer():
    # Load the dataset and parse the 'date' column as datetime objects, set 'date' as the index
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    
    # Filter out the top and bottom 2.5% of page views to clean the data
    df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

    # Function to create a line plot for daily page views over time
    def draw_line_plot():
        # Set the size of the plot to 12x6 inches
        plt.figure(figsize=(12, 6))
        
        # Plot the 'value' (page views) against the 'date' (index) with a blue line
        plt.plot(df.index, df['value'], color='blue')
        
        # Set the title of the plot
        plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
        
        # Label the x-axis as 'Date'
        plt.xlabel('Date')
        
        # Label the y-axis as 'Page Views'
        plt.ylabel('Page Views')
        
        # Display gridlines on the plot
        plt.grid(True)
        
        # Adjust layout to make sure everything fits within the figure
        plt.tight_layout()
        
        # Return the generated plot
        return plt

    # Function to create a bar plot showing the average daily page views per month
    def draw_bar_plot():
        # Resample the data by month and calculate the mean (average) page views per month
        df_monthly = df.resample('M').mean()
        
        # Set the size of the bar plot to 12x6 inches
        plt.figure(figsize=(12, 6))
        
        # Create a bar plot of the resampled monthly data, with months as the legend
        df_monthly['value'].unstack().plot(kind='bar', stacked=False)
        
        # Set the title of the bar plot
        plt.title('Average Daily Page Views per Month')
        
        # Label the x-axis as 'Years'
        plt.xlabel('Years')
        
        # Label the y-axis as 'Average Page Views'
        plt.ylabel('Average Page Views')
        
        # Add a legend with the title 'Months'
        plt.legend(title='Months')
        
        # Adjust layout to ensure the plot fits properly
        plt.tight_layout()
        
        # Return the generated plot
        return plt

    # Function to create box plots showing year-wise and month-wise trends
    def draw_box_plot():
        # Create a copy of the original DataFrame
        df_year = df.copy()
        
        # Add a new column 'year' extracted from the index (which is the 'date' column)
        df_year['year'] = df_year.index.year
        
        # Add a new column 'month' extracted from the index (which is the 'date' column)
        df_year['month'] = df_year.index.month
        
        # Set the size of the plot for the year-wise box plot to 12x6 inches
        plt.figure(figsize=(12, 6))
        
        # Create a box plot for year-wise distribution of page views
        sns.boxplot(x='year', y='value', data=df_year)
        
        # Set the title for the year-wise box plot
        plt.title('Year-wise Box Plot (Trend)')
        
        # Adjust layout to ensure the plot fits properly
        plt.tight_layout()
        
        # Set the size of the plot for the month-wise box plot to 12x6 inches
        plt.figure(figsize=(12, 6))
        
        # Create a box plot for month-wise distribution of page views
        sns.boxplot(x='month', y='value', data=df_year)
        
        # Set the title for the month-wise box plot
        plt.title('Month-wise Box Plot (Seasonality)')
        
        # Adjust layout to ensure the plot fits properly
        plt.tight_layout()
        
        # Return the generated plots
        return plt

    # Return the plots from the three functions
    return draw_line_plot(), draw_bar_plot(), draw_box_plot()
