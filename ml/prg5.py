# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 09:05:38 2022

@author: VEDANT
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

df = pd.read_csv("./datasets/uber.csv")
df.head()

print(df.shape)
print(df.columns)

print(df.isna().sum())

df = df.dropna(axis=0)
print(df.isna().sum())

df.drop(["Unnamed: 0", "key"], axis=1, inplace=True)
print(df.columns)

print(df.dtypes)

df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])

print(df.dtypes)

df=df.assign(
    hour = df.pickup_datetime.dt.hour,
    day = df.pickup_datetime.dt.day,
    month = df.pickup_datetime.dt.month,
    year = df.pickup_datetime.dt.year,
    dayofweek = df.pickup_datetime.dt.dayofweek,
    )
df = df.drop("pickup_datetime", axis=1)
print(df.columns)

X = df.drop("fare_amount", axis=1)
y = df["fare_amount"]

print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model1 = LinearRegression()
model1.fit(X_train, y_train)
y_pred1 = model1.predict(X_test)

print(metrics.mean_squared_error(y_test, y_pred1))
print(metrics.mean_absolute_error(y_test, y_pred1))

model2 = RandomForestRegressor(n_estimators=100)
model2.fit(X_train, y_train)
y_pred2 = model2.predict(X_test)

print(metrics.mean_squared_error(y_test, y_pred2))
print(metrics.mean_absolute_error(y_test, y_pred2))
