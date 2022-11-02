import pandas as pd
avocado_mean = pd.read_csv("avocado_mean.csv", index_col=0, parse_dates=['Date'])

avocado_mean = avocado_mean.reset_index()

max_avg_price = avocado_mean['AveragePrice'].rolling(3).mean().max().round(2)

print(max_avg_price)