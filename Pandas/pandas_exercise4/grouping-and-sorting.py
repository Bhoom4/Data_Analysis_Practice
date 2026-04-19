import pandas as pd

# Load dataset (make sure file is in same folder or give correct path)
reviews = pd.read_csv("pandas/pandas_exercise3/winemag-data-130k-v2.csv")

#----------------------------------------
# Q1: Reviews written per taster
#----------------------------------------
reviews_written = reviews.groupby('taster_twitter_handle').size()
print("\nQ1:\n", reviews_written)


#----------------------------------------
# Q2: Best rating per price
#----------------------------------------
best_rating_per_price = reviews.groupby('price').points.max()
print("\nQ2:\n", best_rating_per_price)



#----------------------------------------
# Q3: Price extremes by variety
price_extremes = reviews.groupby('variety').price.agg([min, max])
print("\nQ3:\n", price_extremes)
#----------------------------------------


#----------------------------------------
# Q4: Average rating by country and variety
country_variety_means = reviews.groupby(['country', 'variety']).points.mean()
print("\nQ4:\n", country_variety_means)
#----------------------------------------


#----------------------------------------
# Q5: Sorted by highest rating
sorted_country_variety_means = country_variety_means.sort_values(ascending=False)
print("\nQ5:\n", sorted_country_variety_means)
#----------------------------------------


#----------------------------------------
# Q6: Sorted by index
sorted_index = country_variety_means.sort_index()
print("\nQ6:\n", sorted_index)
#----------------------------------------