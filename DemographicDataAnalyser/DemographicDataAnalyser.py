import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    #How many people are included in the dataset?
    total_people = len(df)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of males?
    average_age_men = round(df.loc[df['sex']=='Male']['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = df.loc[df['education']=='Bachelors']['education'].count()
    percentage_bachelors = round((bachelors/total_people)*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education_condition = (df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')
    higher_education = df.loc[higher_education_condition,['education','salary']]
    lower_education = df.loc[~higher_education_condition,['education','salary']]

    # percentage with salary >50K
    higher_education_rich = round((len(higher_education.loc[higher_education['salary']=='>50K'])/len(higher_education))*100,1)
    lower_education_rich = round((len(lower_education.loc[lower_education['salary']=='>50K'])/len(lower_education))*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df.loc[df['hours-per-week']==min_work_hours,['salary']]
    num_min_workers = len(min_workers)
    rich_percentage = round((len(min_workers.loc[min_workers['salary']=='>50K'])/num_min_workers)*100,1)

    # What country has the highest percentage of people that earn >50K?
    people_per_country = df['native-country'].value_counts()
    rich_people_per_country = df.loc[(df['salary']=='>50K')]['native-country'].value_counts()
    rich_country_percentage = round((rich_people_per_country/people_per_country)*100,1)
    highest_earning_country = rich_country_percentage.idxmax()
    highest_earning_country_percentage = rich_country_percentage.max()

    # Identify the most popular occupation for those who earn >50K in India.
    rich_in_india = df.loc[(df['salary']=='>50K') & (df['native-country']=='India')]['occupation']
    occupations_in_india = rich_in_india.value_counts()
    top_IN_occupation = occupations_in_india.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()