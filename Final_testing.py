import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl

#import csv
data = pd.read_csv('liquor_store_2016-2019.csv')

#bottles sold based on zip code
popular_item = data.groupby('zip_code').bottles_sold.sum()
df_popular_item = popular_item.to_frame()
#percentage of sales per store
store_sales = data.groupby('store_number').bottles_sold.sum()
total_sales = data['bottles_sold'].sum()
percentage = store_sales/total_sales*100
df_storesales = store_sales.to_frame()

store_numbers = data.groupby('store_number')
df_percentage = percentage.to_frame()

plt.plot(store_numbers,percentage)
plt.show()
plt.pause(1)

print(store_numbers.first())

print(df_popular_item)

#group_stores
stores = data.get_group('store_number')


#scatter plot
plt.scatter(df_popular_item.index, df_popular_item, s=200)
plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")
plt.title("Bottles Sold per Zip Code")
plt.show()
plt.pause(1)

#code ends here
##########################################

#Just for tests

#Trying to make a plot where x_axis = store_number and y_axis = percentage of sales
plt.plot(data['store_number'],percentage)
plt.show()
plt.pause(1)



mylabels = data.iterrows('store_name')
plt.pie(percentage, labels = mylabels)

print(percentage)
print(popular_item)
new_table = {'popular_item':[data.groupby('zip_code').bottles_sold.sum()],'percentage':[percentage]}
df = pd.DataFrame(new_table)
df.to_excel("E:\kevre\WORKEARLY DATA ANALYSIS\python\python files\check.xlsx")

#more sales = greener circle
plt.scatter(popular_item.index, popular_item, s=200, c = popular_item, cmap = 'Greens')