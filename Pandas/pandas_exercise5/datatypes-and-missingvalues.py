import pandas as pd

# Load dataset
reviews = pd.read_csv("pandas/pandas_exercise3/winemag-data-130k-v2.csv")


# -----------------------------------
# Q1: Data type of points column
# -----------------------------------
dtype = reviews.points.dtype
print("Q1 - Data Type of points column:")
print(dtype)


# -----------------------------------
# Q2: Convert points to strings
# -----------------------------------
point_strings = reviews.points.astype('str')
print("\nQ2 - Points as strings:")
print(point_strings.head())


# -----------------------------------
# Q3: Count missing prices
# -----------------------------------
n_missing_prices = reviews.price.isnull().sum()
print("\nQ3 - Number of missing prices:")
print(n_missing_prices)


# -----------------------------------
# Q4: Replace missing region values
# -----------------------------------
reviews_per_region = (
    reviews.region_1
    .fillna("unknown")
    .value_counts()
    .sort_values(ascending=False)
)

print("\nQ4 - Reviews per region:")
print(reviews_per_region.head())