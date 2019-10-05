#THIS PROGRAM IS TO GIVE BEGINNER'S BASIC GRASP OF LINEAR REGRESSION IN ML


#1. IMPORT:-

# pandas is used for loading datasets
import pandas as pd

#sklearn is famous Data Science library used for various purposes and sklearn.datasets has many pre-loaded datasets
from sklearn import datasets

#matplotlib is famous for data visualization 
from matplotlib import pyplot as plt

#seaborn is also used for data visualization
import seaborn as sns

#For handling array
import numpy as np

#2. DATASET READING AND UNDERSTANDING

#First we will load the dataset into a dataframe(df)
df=datasets.load_boston()

print(df)

#As we can see df is in format not suitable for anything
#So we arrange in a Dataset
x=df.data
boston=pd.DataFrame(df.data,columns=df.feature_names)
boston.head()

boston['MEDV']=df.target
boston.head()

#Now we'll see if there is any need feature cleaning(beginner should only do if there are null values present
boston.isnull().sum()

#correlation matrix show how dependent various features are to each other(used for extracting important features only)
#1,-1=>highly dependent 0=>not dependent at all
plt.figure(figsize=(10,9))
correlation_matrix=boston.corr()
sns.heatmap(correlation_matrix, annot=True)#annot true for printing value inside square
plt.show()

#3. MODEL

#Here x will be the features(values of different things) and y will be the label(answer that we got from x)
x=boston.drop(columns=['MEDV'],axis=1)
x.head()

y=boston.MEDV

#splitting data into training and testing(but theoritical it's more like training and validation but it's ok for now)
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#making a linear regression model
from sklearn import linear_model
lr=linear_model.LinearRegression()

#train the model -> fitting the model
lr.fit(x_train,y_train)

#now predicting
y_predict=lr.predict(x_test)


#4. EVALUATION

lr.score(x_test,y_test)

#mean squared error
from sklearn.metrics import mean_squared_error as mse
mse(y_predict,y_test)
