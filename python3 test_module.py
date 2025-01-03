import pandas as pd

def demographic_data_analyzer():
    df = pd.read_csv('data.csv')

    race_counts = df['race'].value_counts()

    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_high_salary_advanced = (advanced_education['salary'] == '>50K').mean() * 100

    no_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_high_salary_no_education = (no_advanced_education['salary'] == '>50K').mean() * 100

    min_hours_per_week = df['hours-per-week'].min()

    min_hours_salary = df[df['hours-per-week'] == min_hours_per_week]
    percentage_high_salary_min_hours = (min_hours_salary['salary'] == '>50K').mean() * 100

    country_salary = df[df['salary'] == '>50K'].groupby('native-country').size() / df.groupby('native-country').size() * 100
    highest_salary_country = country_salary.idxmax()
    highest_salary_percentage = country_salary.max()

    india_high_salary = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    most_popular_occupation_india = india_high_salary['occupation'].value_counts().idxmax()

    return {
        'race_counts': race_counts,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_high_salary_advanced': percentage_high_salary_advanced,
        'percentage_high_salary_no_education': percentage_high_salary_no_education,
        'min_hours_per_week': min_hours_per_week,
        'percentage_high_salary_min_hours': percentage_high_salary_min_hours,
        'highest_salary_country': highest_salary_country,
        'highest_salary_percentage': highest_salary_percentage,
        'most_popular_occupation_india': most_popular_occupation_india
    }
