import numpy as np
import pandas as pd

df = pd.read_csv("./Exs_7_6_w1/advertising.csv")
# how can i get index columns sales
# NOTE: index column destination
sales_index = df.columns.get_loc("Sales")
tv_index = df.columns.get_loc("TV")
radio_index = df.columns.get_loc("Radio")
newspaper_index = df.columns.get_loc("Newspaper")

# NOTE: convert df to numpy
data = df.to_numpy()

max_prices = np.max(data[:, sales_index])
max_prices_index = np.argmax(data[:, sales_index])
print(max_prices)
print(max_prices_index)


df_tv = data[:, tv_index]
tv_max = np.sum(df_tv) / np.count_nonzero(df_tv)
print(tv_max)

df_sale = data[:, sales_index]
arg_sale_higher_20 = df_sale[df_sale >= 20]
print(arg_sale_higher_20)
print(arg_sale_higher_20.shape)


df_radio = data[:, radio_index]
index_sale_higher_15 = df_sale >= 15
arg_radio_higher_15_respective = df_radio[index_sale_higher_15]
average_argradio_higher_15 = np.mean(arg_radio_higher_15_respective)
print(average_argradio_higher_15)

df_newspaper = data[:, newspaper_index]
average_newspaper = np.mean(df_newspaper)
df_higher_average_newspaper = df_newspaper > average_newspaper
sum_df_higher_average_sale = np.sum(df_sale[df_higher_average_newspaper])
print(sum_df_higher_average_sale)



