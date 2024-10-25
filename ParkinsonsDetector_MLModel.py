# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score

parkinsons_data = pd.read_csv('/content/parkinsons.csv')
parkinsons_data.head()
parkinsons_data.shape
parkinsons_data.info()

# missing values
parkinsons_data.isnull().sum()

# stats
parkinsons_data.describe()

# distribution
parkinsons_data['status'].value_counts()

"""*1*  --> YES Parkinson's

0 --> NO Parkinson's

"""

# grouping
parkinsons_data.groupby('status').mean()

"""Data Pre-Processing

[link text](https://)Separating the features & Target
"""

X = parkinsons_data.drop(columns=['name','status'], axis=1)
Y = parkinsons_data['status']

print(X)

print(Y)

"""Splitting the data to training data & Test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Data Standardization"""

scaler = StandardScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)

X_test = scaler.transform(X_test)

print(X_train)

"""Model Training

Support Vector Machine Model
"""

model = svm.SVC(kernel='linear')

# training the SVM model with training data
model.fit(X_train, Y_train)

"""Model Evaluation

Accuracy Scores
"""

# accuracy score on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)

print('Accuracy score (training data): ', training_data_accuracy)

# accuracy score on training data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_prediction)

print('Accuracy score (test data): ', test_data_accuracy)

"""Predictive -----"""

input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)

# changing input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape numpy array
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize data
std_data = scaler.transform(input_data_reshaped)

prediction = model.predict(std_data)
print(prediction)


if (prediction[0] == 0):
  print("This person does not have Parkinson's Disease.")

else:
  print("This person has Parkinson's Disease")
