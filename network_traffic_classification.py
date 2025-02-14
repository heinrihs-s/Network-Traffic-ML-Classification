# -*- coding: utf-8 -*-
"""

Automatically generated by Colab.

"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O
import matplotlib.pyplot as plt #visualization
import seaborn as sns #visualization
import tensorflow #ML
import sklearn #ML
from sklearn.preprocessing import LabelEncoder, StandardScaler

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings('ignore')

from google.colab import drive
!cp "/content/drive/My Drive/week1.csv" "week1.csv"

data = pd.read_csv("week1.csv")
data.head()

data.columns

data.isna().sum()

data.dtypes

nRow, nCol = data.shape
print(f'There are {nRow} rows and {nCol} columns')

print("No. of Unique Src Ip Addresses :", data['Src IP Addr'].nunique())
print("No. of Unique Dst Ip Addresses :", data['Dst IP Addr'].nunique())

data.label.value_counts()

data["Flags"].unique()

data["A"]=0
data["P"]=0
data["S"]=0
data["F"]=0
data["R"]=0

def set_flag(data,check):
    val=0;
    if(check in list(data["Flags"])):
        val = 1 ;
    return val;

data["A"] = data.apply(set_flag, check ="A", axis = 1)
data["P"] = data.apply(set_flag, check = "P", axis = 1)
data["S"] = data.apply(set_flag, check ="S", axis = 1)
data["R"] = data.apply(set_flag, check="R", axis = 1)
data["F"] = data.apply(set_flag, check ="F", axis = 1)

sns.countplot(x="S", hue = "label", data=data)

sns.countplot(x="A", hue = "label", data=data)

sns.countplot(x="P", hue = "label", data=data)

sns.countplot(x="F", hue = "label", data=data)

sns.countplot(x="R", hue = "label", data=data)

sns.countplot(x = "Proto", hue = "label", data = data)

data=data.drop(columns = ["Flows","Flags","Tos","attackType","attackID","attackDescription", "Date first seen"])

data.head()

#delete M char and convert to num (Bytes)
import re
def convtonum(data):
    num1 = data["Bytes"]
    if "M" in data["Bytes"]:
        num = re.findall("[0-9].[0-9]",data["Bytes"])
        num1 = np.float128("".join(num))*100000
    num1 = np.float128(num1)
    return num1

data["Bytes"] = data["Bytes"].astype(str)

data["Bytes"] = data.apply(convtonum,axis = 1)

#sns.lmplot(x='Bytes', y="Packets",data=data)

#normalize labels
from sklearn.preprocessing import LabelEncoder

col = ["Dst Pt","Proto","Src IP Addr","Dst IP Addr","label"]
enc = LabelEncoder()
for col_name in col:
    data[col_name]=enc.fit_transform(data[col_name])

corr = data.corr()
corr.style.background_gradient(cmap = 'coolwarm').set_precision(2)

data_y = data["label"]
data_x = data.drop(columns = ["label"])

data.head()

import random
from sklearn.model_selection import train_test_split

data_y.sample(frac=1)
data_x.sample(frac=1)
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(data_x, data_y, test_size=0.3)

#Naive Bayes algorithm

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, classification_report
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import confusion_matrix

gnb = GaussianNB()
gnb.fit(X_train, y_train)
pred = gnb.predict(X_test)
accuracy = accuracy_score(pred, y_test)
precision = precision_score(y_test, pred, average='weighted')
print("Accuracy:", accuracy)
print("Precision:", precision)
print(classification_report(y_test,pred, labels=None))
cm=confusion_matrix(y_test, pred)
print(cm)

# k-neighbors algorithm

from sklearn.neighbors import KNeighborsClassifier

for i in range(3,15,3):

    neigh = KNeighborsClassifier(n_neighbors=i)
    neigh.fit(X_train, y_train)
    pred = neigh.predict(X_test)
    # accuracy
    accuracy = accuracy_score(pred, y_test)
    precision = precision_score(pred, y_test)
    print("kneighbors {}".format(i))
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print(classification_report(pred, y_test, labels=None))
    cm=confusion_matrix(y_test, pred)
    print(cm)

    print("")

# decision tree

from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf.fit(X_train, y_train)
pred = clf.predict(X_test)

print(clf)
print(classification_report(pred, y_test, labels=None))
accuracy = accuracy_score(pred, y_test)
precision = precision_score(pred, y_test, average='micro')
print("Accuracy:", accuracy)
print("Precision:", precision)
cm=confusion_matrix(y_test, pred)
print(cm)

# random forest

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

rdF=RandomForestClassifier(n_estimators=250, max_depth=50,random_state=45)
rdF.fit(X_train,y_train)
pred=rdF.predict(X_test)
cm=confusion_matrix(y_test, pred)

accuracy = accuracy_score(pred,y_test)
precision = precision_score(pred, y_test)

print(rdF)
print(accuracy)
print(classification_report(y_test,pred, labels=None))
print("Accuracy:", accuracy)
print("Precision:", precision)
print(cohen_kappa_score(y_test, pred))
print(cm)

feat_importances = pd.Series(clf.feature_importances_, index=X_train.columns)
feat_importances.nlargest(15).plot(kind='barh')
plt.show()

# most important features from recursive feature elimination with cross-validation

from sklearn.feature_selection import RFECV
from sklearn.pipeline import Pipeline
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from numpy import mean
from numpy import std

# pipeline
rfe = RFECV(estimator=DecisionTreeClassifier())
model = DecisionTreeClassifier()
pipeline = Pipeline(steps=[('s',rfe),('m',model)])
# evaluation
cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=2, random_state=1)
n_scores = cross_val_score(pipeline, X_train, y_train, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
# report performance
print('Accuracy: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))

# report which features were selected by RFE

from sklearn.datasets import make_classification
from sklearn.feature_selection import RFE

# define RFE
rfe = RFE(estimator=DecisionTreeClassifier(), n_features_to_select=5)
# fit RFE
rfe.fit(X_train, y_train)
# summarize all features
for i in range(X_train.shape[1]):
	print('Column: %d, Selected %s, Rank: %.3f' % (i, rfe.support_[i], rfe.ranking_[i]))
