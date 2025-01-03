import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def medical_data_visualizer():
    # Step 1: Import data
    df = pd.read_csv('medical_examination.csv')

    # Step 2: Add an overweight column
    df['bmi'] = df['weight'] / ((df['height'] / 100) ** 2)
    df['overweight'] = df['bmi'].apply(lambda x: 1 if x > 25 else 0)

    # Step 3: Normalize cholesterol and glucose data
    df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
    df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)

    # Step 4: Draw Categorical Plot
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.rename(columns={'variable': 'feature', 'value': 'value'})
    cat_plot = sns.catplot(x="feature", hue="value", col="cardio", data=df_cat, kind="count")
    fig = cat_plot.fig

    # Step 5: Draw Heat Map
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    corr = df_heat.corr()
    mask = np.triu(corr)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".1f", mask=mask, cmap='coolwarm', linewidths=0.5)

    return fig
