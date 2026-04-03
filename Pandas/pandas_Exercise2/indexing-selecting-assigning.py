import pandas as pd

# Load dataset (IMPORTANT: change path when running locally)
reviews = pd.read_csv("pandas/pandas_Exercise2/winemag-data-130k-v2.csv")

# -----------------------------------
# Q1: Select description column
# -----------------------------------
desc = reviews.description
# or   desc = reviews.loc[:,'description']
print("Q1:\n", desc.head(), "\n")


# -----------------------------------
# Q2: First description
# -----------------------------------
first_description = reviews.description.iloc[0]
# or    first_description = reviews['description'][0]
print("Q2:\n", first_description, "\n")


# -----------------------------------
# Q3: First row
# -----------------------------------
first_row = reviews.iloc[0]
print("Q3:\n", first_row, "\n")


# -----------------------------------
# Q4: First 10 descriptions
# -----------------------------------
first_descriptions = reviews.loc[:9,'description']
print("Q4:\n", first_descriptions, "\n")


# -----------------------------------
# Q5: Select specific rows
# -----------------------------------
sample_reviews = reviews.loc[[1, 2, 3, 5, 8]]
print("Q5:\n", sample_reviews, "\n")


# -----------------------------------
# Q6: Select rows & columns
# -----------------------------------
df_q6 = reviews.loc[[0, 1, 10, 100], ['country', 'province', 'region_1', 'region_2']]
print("Q6:\n", df_q6, "\n")


# -----------------------------------
# Q7: First 100 rows with selected columns
# -----------------------------------
df_q7 = reviews.loc[0:99, ['country', 'variety']]
print("Q7:\n", df_q7.head(), "\n")


# -----------------------------------
# Q8: Wines from Italy
# -----------------------------------
italian_wines = reviews.loc[reviews.country == 'Italy']
print("Q8:\n", italian_wines.head(), "\n")


# -----------------------------------
# Q9: Complex filtering
# -----------------------------------
top_oceania_wines = reviews.loc[
    (reviews.points >= 95) &
    ((reviews.country == 'Australia') | (reviews.country == 'New Zealand'))
]
print("Q9:\n", top_oceania_wines.head(), "\n")