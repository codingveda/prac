# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 08:24:09 2022

@author: VEDANT
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("./datasets/sales_data_sample.csv", encoding="latin1")
df.head()

print(df.columns)
print(df.dtypes)

df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])
df = df.assign(
    day = df.ORDERDATE.dt.day,
    month = df.ORDERDATE.dt.month,
    year = df.ORDERDATE.dt.year,
    dayofweek = df.ORDERDATE.dt.dayofweek,
    )

df["PRODUCTLINE"].unique()

encoder = LabelEncoder()
encoder.fit(df["PRODUCTLINE"])
df["PRODUCTLINE"] = encoder.transform(df["PRODUCTLINE"])
df["PRODUCTLINE"].unique()

df["DEALSIZE"].unique()

#encoder = LabelEncoder()
encoder.fit(df["DEALSIZE"])
df["DEALSIZE"] = encoder.transform(df["DEALSIZE"])
df["DEALSIZE"].unique()

X = df[["QUANTITYORDERED", "PRICEEACH", "SALES", "PRODUCTLINE", "MSRP", "DEALSIZE", "day", "month", "year", "dayofweek"]]

# Elbow Method
wcss = {}
for i in range(1, 11):
    model = KMeans(n_clusters=i, random_state=0)
    model.fit(X)
    wcss[i] = model.inertia_

print(wcss)
plt.title("Elbow method")
plt.xlabel("no. clusters")
plt.ylabel("inertia")
sns.lineplot(list(wcss.keys()), list(wcss.values()))
plt.plot()


kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
label = kmeans.predict(X)

X = X.assign(label=label)
X.head()

label_count = list(X["label"].unique())
for i in label_count:
    plt.scatter(X[label==i].iloc[:, 1], X[label==i].iloc[:, 2], label=i)
plt.legend()
plt.plot()


