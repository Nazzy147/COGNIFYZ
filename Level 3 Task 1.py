#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score


# In[2]:


# Load Dataset
data = pd.read_csv("E:\Internship\Dataset.csv")


# In[3]:


# Create additional features
data['Has Wifi_Num'] = np.where(data['Has Wifi'] == "Yes", 1, 0)
data['Is Online store_Num'] = np.where(data['Is Online store'] == "Yes", 1, 0)


# In[4]:


# Define predictors and target variable
features = ["Average Cost", "Votes", "Price Range", "Has Wifi_Num", "Is Online store_Num"]
target = "Overall Rating"


# In[5]:


# Split data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=123)


# In[6]:


# Initialize models
models = {
    "Ridge Regression": Ridge(),
    "Lasso Regression": Lasso(),
    "Gradient Boosting": GradientBoostingRegressor(),
    "Support Vector Regressor": SVR(kernel='rbf')
}

results = {}

for name, model in models.items():
    scores = cross_val_score(model, train_data[features], train_data[target], cv=5, scoring='neg_mean_squared_error')
    model.fit(train_data[features], train_data[target])
    predictions = model.predict(test_data[features])
    rmse = np.sqrt(mean_squared_error(test_data[target], predictions))
    r2 = r2_score(test_data[target], predictions)
    results[name] = {"RMSE": rmse, "R-squared": r2}


# In[7]:


# Print results
for name, result in results.items():
    print(name + " RMSE:", result["RMSE"])
    print(name + " R-squared:", result["R-squared"])
    print()
