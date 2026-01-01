import pandas as pd

df= pd.read_csv("messy.csv")

print(df.head())
print(df.columns)
print(df.dtypes)

df["Price"] = df["Price"].str.replace("£","").astype(float)
print(df.dtypes)
df = df.drop_duplicates()
Rating_map = {
    "One":1,
    "Two":2,
    "Three":3,
    "Four":4,
    "Five":5
}

df["Rating_num"] = df["Rating"].map(Rating_map)

df_sort = df[(df["Price"]>40) & (df["Rating_num"]>=4)]

df_sort = df_sort.sort_values(by="Price",ascending=False)

df_analyse= df.groupby("Rating").agg(Count = ("Book title","count"), Average = ("Price","mean"))
df_analyse["Average"] = df_analyse["Average"].round(2)

df.to_csv("Cleaned_data.csv",index=False)
df_sort.to_csv("Filtered_items.csv",index=False)
df_analyse.to_csv("Groupby_rating.csv")