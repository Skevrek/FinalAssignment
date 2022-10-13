#code starts here

import pandas as pd
import matplotlib.pyplot as plt
#import csv
data = pd.read_csv('liquor_store_2016-2019.csv')

#Most popular item sold based on zip code, used groupby + aggregation in one line.
#i would like to ask about the disadvatages of this method since it looks like i have a series and not a DF.
#Could DF the series using df_popular_item = popular_item.to_frame(). Advantages?
popular_item = data.groupby('zip_code').bottles_sold.sum()

#Find the percentage of sales per store. I have my doubts about this one
store_sales = data.groupby('store_number').bottles_sold.sum()
total_sales = data['bottles_sold'].sum()
percentage = store_sales/total_sales*100

#plotting using subplots. i couldn't find a reason to use coloring here. Maybe different color for every store? How can i display that?
#Found a way to display light to dark colour based on the value of Y axis(or certain column).Adding c = popular_item, cmap = 'Greens'
plt.subplot(2,1,1)
plt.scatter(popular_item.index, popular_item, s=200)
plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")
plt.title("Bottles Sold per Zip Code")

plt.subplot(2,1,2)
plt.scatter(store_sales.index,percentage)
plt.xlabel("Store Number")
plt.ylabel("Percentage of Sales")
plt.title("Percentage of Sales per Store")
plt.show()
#using plt.pause() to stop some crushes with matplotlib
plt.pause(1)

#code ends here

#Tried some ways to bring the aggregated data back to csv or excel file with not much success.
#Would like to find a way to bring aggregated data back in a file arranged in columns so i can use it in tableau or powerbi.
new_table = {'popular_item':[data.groupby('zip_code').bottles_sold.sum()],'percentage':[percentage]}
df = pd.DataFrame(new_table)
df.to_excel("E:\kevre\WORKEARLY DATA ANALYSIS\python\python files\check.xlsx")

