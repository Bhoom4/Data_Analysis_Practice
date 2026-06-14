import pandas as pd
import numpy as np

# Load dataset 
reviews = pd.read_csv("pandas/pandas_exercise3/winemag-data-130k-v2.csv")

# -------------------------------
# Q1: Median of points
# -------------------------------
median_points = reviews.points.median()
print("Median Points:", median_points)


# -------------------------------
# Q2: Unique countries
# -------------------------------
countries = reviews.country.unique()
print("\nUnique Countries:\n", countries)


# -------------------------------
# Q3: Reviews per country
# -------------------------------
reviews_per_country = reviews.country.value_counts()
print("\nReviews per Country:\n", reviews_per_country)


# -------------------------------
# Q4: Centered price
# -------------------------------
centered_price = reviews.price - reviews.price.mean()
print("\nCentered Price:\n", centered_price.head())


# -------------------------------
# Q5: Best bargain wine
# -------------------------------
ratio = reviews.points / reviews.price
best_index = ratio.idxmax()
bargain_wine = reviews.title.loc[best_index]
print("\nBest Bargain Wine:\n", bargain_wine)


# -------------------------------
# Q6: Descriptor counts
# -------------------------------
descriptor_counts = pd.Series({
    "tropical": reviews.description.str.contains("tropical",regex=False).sum(),
    "fruity": reviews.description.str.contains("fruity",regex=False).sum()
})
print("\nDescriptor Counts:\n", descriptor_counts)


# -------------------------------
# Q7: Star ratings
# -------------------------------
conditions = [
    (reviews.country == "Canada"),
    (reviews.points >= 95),
    (reviews.points >= 85)
]

choices = [3, 3, 2]

star_ratings = pd.Series(np.select(conditions, choices, default=1))
print("\nStar Ratings:\n", star_ratings.head())