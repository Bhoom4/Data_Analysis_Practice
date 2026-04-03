
import pandas as pd

# -----------------------------------
# Q1: Create DataFrame
# -----------------------------------

fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])
print("Exercise 1:\n", fruits, "\n")


# -----------------------------------
# Q2: Fruit Sales DataFrame
# -----------------------------------

fruit_sales = pd.DataFrame(
    {'Apples': [35, 41], 'Bananas': [21, 34]},
    index=['2017 Sales', '2018 Sales']
)
print("Exercise 2:\n", fruit_sales, "\n")


# -----------------------------------
# Q3: Create Series
# -----------------------------------

ingredients = pd.Series(
    ['4 cups', '1 cup', '2 large', '1 can'],
    index=['Flour', 'Milk', 'Eggs', 'Spam'],
    name='Dinner'
)
print("Exercise 3:\n", ingredients, "\n")


# -----------------------------------
# Q4: Read CSV File
# -----------------------------------
try:
    reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv")
    print("Exercise 4:\n", reviews.head(), "\n")
except FileNotFoundError:
    print("Exercise 4:\n CSV file not found. please add a dataset.")



# -----------------------------------
# Q5: Save DataFrame to CSV
# -----------------------------------

animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]})
animals.to_csv("Pandas/pandas_Exercise1/cows_and_goats.csv")
print("Exercise 5:\n File saved as cows_and_goats.csv")