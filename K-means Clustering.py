import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.cluster import	KMeans
from scipy.spatial.distance import cdist 

data = pd.read_excel("EastWestAirlines.xlsx")

data.describe()

# Normalization function 
def norm_func(i):
    x = (i-i.min())	/ (i.max()-i.min()) #min max scaler
    return (x)

# Normalized data frame (considering the numerical part of dataset)
df_norm = norm_func(data.iloc[:,1:])
df_norm.describe()

###### scree plot or elbow curve ############
TWSS = []
k = list(range(2, 12))

for i in k:
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(df_norm)
    TWSS.append(kmeans.inertia_)
    
TWSS

# Scree plot 
plt.plot(k, TWSS, 'ro-');plt.xlabel("No_of_Clusters");plt.ylabel("total_within_SS")

# Selecting 3 clusters from the above scree plot which is the optimum number of clusters 
model = KMeans(n_clusters = 3)
model.fit(df_norm)

model.labels_ # getting the labels of clusters assigned to each row 
mb = pd.Series(model.labels_)  # converting numpy array into pandas series object 
data['clust'] = mb # creating a  new column and assigning it to new column 

data.head()
df_norm.head()

#rearranging columns
data = data.iloc[:,[12,0,1,2,3,4,5,6,7,8,9,10,11]]
data.head()

data.iloc[:, 2:11].groupby(data.clust).mean()

# creating a csv file 
data.to_csv("Kmeans_airlines.csv", encoding = "utf-8")

import os
os.getcwd() #to get path where csv file is stored