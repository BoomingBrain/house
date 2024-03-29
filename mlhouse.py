# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FMbTC4VL0CPgNICq8C1vfDvwhRn5LCch
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import gradio as gr

datatrain=pd.read_csv('trainml.csv')
datatest=pd.read_csv('testml.csv')
dfcon=pd.concat([datatrain,datatest])
dfcon.set_index('Id')
df=dfcon.copy()
df.set_index('Id')

df.isnull().sum()

zone=df['MSZoning'].mode()[0]
df['MSZoning'].replace(np.nan,zone,inplace=True)
df['MSZoning'].isnull().sum()

df['Alley'].replace(np.nan,'Not',inplace=True)
df['Alley'].isnull().sum()

frontage=df['LotFrontage'].median()
df['LotFrontage'].replace(np.nan,frontage,inplace=True)
df['LotFrontage'].isnull().sum()

utiletes=df['Utilities'].mode()[0]
df['Utilities'].replace(np.nan,utiletes,inplace=True)
df['Utilities'].isnull().sum()

ex1=df['Exterior1st'].mode()[0]
df['Exterior1st'].replace(np.nan,ex1,inplace=True)
df['Exterior1st'].isnull().sum()

ex2=df['Exterior2nd'].mode()[0]
df['Exterior2nd'].replace(np.nan,ex2,inplace=True)
df['Exterior2nd'].isnull().sum()

df['MasVnrType'].replace(np.nan,df['MasVnrType'].mode()[0],inplace=True)
df['MasVnrArea'].replace(np.nan,0,inplace=True)

df['BsmtQual'].replace(np.nan,'NA',inplace=True)
df['BsmtQual'].isnull().sum()

df['BsmtCond'].replace(np.nan,'NA',inplace=True)
df['BsmtCond'].isnull().sum()

df['BsmtExposure'].replace(np.nan,'NA',inplace=True)
df['BsmtExposure'].isnull().sum()

df['BsmtFinType1'].replace(np.nan,'NA',inplace=True)
df['BsmtFinType1'].isnull().sum()

df['BsmtFinType2'].replace(np.nan,'NA',inplace=True)
df['BsmtFinType2'].isnull().sum()

basement=['BsmtFinSF1','BsmtFinSF2','BsmtUnfSF','TotalBsmtSF','BsmtFullBath','BsmtHalfBath']
for i in basement:
  df[i].replace(np.nan,0,inplace=True)
  df[i].isnull().sum()

df['Electrical'].replace(np.nan,df['Electrical'].mode()[0],inplace=True)

df['KitchenQual'].replace(np.nan,df['KitchenQual'].mode()[0],inplace=True)

fe=['FireplaceQu','PoolQC','Fence','MiscFeature']
for i in fe:
  df[i].replace(np.nan,'NA',inplace=True)

df['Functional'].replace(np.nan,df['Functional'].mode()[0],inplace=True)

df['SaleType'].replace(np.nan,df['SaleType'].mode()[0],inplace=True)

garagech=['GarageType','GarageFinish','GarageQual','GarageCond']
for i in garagech:
  df[i].replace(np.nan,'NA',inplace=True)

garagenum=['GarageYrBlt','GarageCars','GarageArea']
for i in garagenum:
  df[i].replace(np.nan,0,inplace=True)

from pandas.api.types import CategoricalDtype
df['ExterQual']=df['ExterQual'].astype(CategoricalDtype(categories=['Po','Fa','TA','Gd','Ex'],ordered=True)).cat.codes

df['ExterCond']=df['ExterCond'].astype(CategoricalDtype(categories=['Po','Fa','TA','Gd','Ex'],ordered=True)).cat.codes

df['BsmtQual']=df['BsmtQual'].astype(CategoricalDtype(categories=['NA','Po','Fa','TA','Gd','Ex'],ordered=True)).cat.codes

df['BsmtCond']=df['BsmtCond'].astype(CategoricalDtype(categories=['NA','Po','Fa','TA','Gd','Ex'],ordered=True)).cat.codes

df['BsmtExposure']=df['BsmtExposure'].astype(CategoricalDtype(categories=['NA','No','Mn','Av','Gd'],ordered=True)).cat.codes

df['BsmtFinType1']=df['BsmtFinType1'].astype(CategoricalDtype(categories=['NA','Unf','LwQ','Rec','BLQ','ALQ','GLQ'],ordered=True)).cat.codes

df['BsmtFinType2']=df['BsmtFinType2'].astype(CategoricalDtype(categories=['NA','Unf','LwQ','Rec','BLQ','ALQ','GLQ'],ordered=True)).cat.codes

df['HeatingQC']=df['HeatingQC'].astype(CategoricalDtype(categories=['Po','Fa','TA','Gd','Ex'],ordered=True)).cat.codes

df['KitchenQual']=df['KitchenQual'].astype(CategoricalDtype(categories=['Po','Fa','TA','Gd','Ex'],ordered=True)).cat.codes

df['FireplaceQu']=df['FireplaceQu'].astype(CategoricalDtype(categories=['NA','Po','Fa','TA','Gd','Ex'],ordered=True)).cat.codes

df['GarageQual']=df['GarageQual'].astype(CategoricalDtype(categories=['NA','Po','Fa','TA','Gd','Ex'],ordered=True)).cat.codes

df['GarageCond']=df['GarageCond'].astype(CategoricalDtype(categories=['NA','Po','Fa','TA','Gd','Ex'],ordered=True)).cat.codes

df['PoolQC']=df['PoolQC'].astype(CategoricalDtype(categories=['NA','Fa','TA','Gd','Ex'],ordered=True)).cat.codes

df['Functional']=df['Functional'].astype(CategoricalDtype(categories=['Sal','Sev','Maj2','Maj1','Mod','Min2','Min1','Typ'],ordered=True)).cat.codes

df['GarageFinish']=df['GarageFinish'].astype(CategoricalDtype(categories=['NA','Unf','RFn','Fin'],ordered=True)).cat.codes

df['PavedDrive']=df['PavedDrive'].astype(CategoricalDtype(categories=['N','P','Y'],ordered=True)).cat.codes

df['Utilities']=df['Utilities'].astype(CategoricalDtype(categories=['ELO','NoSeWa','NoSewr','AllPub'],ordered=True)).cat.codes

df.info()

onehot=['MSZoning','Street','Alley','LotShape','LandContour','LotConfig','LandSlope','Neighborhood','Condition1','Condition2','BldgType','HouseStyle','RoofStyle','RoofMatl','Exterior1st','Exterior2nd','MasVnrType','Foundation','Heating','CentralAir','Electrical','GarageType','Fence','MiscFeature','SaleType','SaleCondition']

df=pd.get_dummies(df,columns=onehot,prefix=onehot,drop_first=False)

xtrain=df[:1460].drop('SalePrice',axis=1)
ytrain=df['SalePrice'][:1460]
xtest=df[1460:].drop('SalePrice',axis=1)

# prompt: drop first column from xtrain and x test

xtrain = xtrain.drop('Id', axis=1)
xtest = xtest.drop('Id', axis=1)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
xtrain = xtrain.to_numpy()
xtest = xtest.to_numpy()
xtrain[:,:]=sc.fit_transform(xtrain[:,:])
xtest[:,:]=sc.transform(xtest[:,:])

# prompt: using knn model train with xtrain data and predict data of xtest

from sklearn.neighbors import KNeighborsRegressor
knn_model = KNeighborsRegressor(n_neighbors=20)
knn_model.fit(xtrain, ytrain)
y_pred = knn_model.predict(xtest)

# prompt: concatenate the xtest and ypred and change to csv file

df_concat = pd.concat([pd.DataFrame(xtest), pd.DataFrame(y_pred)], axis=1)
df_concat.to_csv('knnreg_predictions.csv', index=False)