from timeit import timeit

import pandas as pd

counter = 0
df_cache = None
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"


def read_data():
    global counter, df_cache

    if df_cache is None:
        counter += 1
        df_cache = pd.read_csv(url)

    return df_cache


print(f"Average time taken to read data: {timeit(read_data, number=100)}")
print(f"Number of API calls: {counter}")

# Average time taken to read data: 0.07319640000059735s
# Number of API calls: 1
