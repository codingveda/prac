# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 07:59:01 2022

@author: VEDANT
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

df = pd.read_csv("./datasets/diabetes.csv")
df.head()

print(df.columns)
print(df.isna().sum())

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print(metrics.accuracy_score(y_test, y_pred))
tn, fp, fn, tp = metrics.confusion_matrix(y_test, y_pred).ravel()
print(tn, fp, fn, tp)

print("accurary", (tn+tp)*100/(tn+fp+fn+tp))
print("Precision", (tp)/(tp+fp))
print("recall", tp/(tp+fn))
print("error rate", (fp+fn)/(fp+fn+tp+tn))