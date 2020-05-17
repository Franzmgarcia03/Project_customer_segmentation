import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D

# Load the Dataset

cust_df = pd.read_csv("Cust_Segmentation.csv")

# Pre-processing data

df = cust_df.drop('Address',axis=1)

# Normalize the dataset

X = df.values[:,1:]
X = np.nan_to_num(X)
Clus_dataSet = StandardScaler().fit_transform(X)

# Modeling with K-Means in 3 different clusters

clusterNum = 3
k_means = KMeans(init = "k-means++", n_clusters = clusterNum, n_init = 12)
k_means.fit(X)
labels = k_means.labels_

# Now we have 3 different labels, this number could
# change in function of the variable clusterNum

# add the label to each customer
df["Clus_km"]=labels

#Find the centroid values for each variable in the table

df.groupby('Clus_km').mean()

# distribution of customers based on their age and income

area = np.pi * (X[:,1])**2
plt.scatter(X[:, 0], X[:, 3], s=area, c=labels.astype(np.float), alpha=0.5)
plt.xlabel('Age', fontsize=18)
plt.ylabel('Income', fontsize=16)

plt.show()

# Distribution of customers based on their age and education

area = np.pi * (X[:,1])**2
plt.scatter(X[:, 0], X[:, 1], s=area, c=labels.astype(np.float), alpha=0.5)
plt.xlabel('Age', fontsize=18)
plt.ylabel('Education', fontsize=16)

plt.show()

# Distribution of customers based on their education and income

area = np.pi * (X[:,1])**2
plt.scatter(X[:, 1], X[:, 3], s=area, c=labels.astype(np.float), alpha=0.5)
plt.xlabel('Education', fontsize=18)
plt.ylabel('Income', fontsize=16)

plt.show()

# 3Dplot Education, Age and Income

fig = plt.figure(1,figsize=(8,6))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()

ax.set_xlabel('Education')
ax.set_ylabel('Age')
ax.set_zlabel('Income')

ax.scatter(X[:, 1], X[:, 0], X[:, 3], c= labels.astype(np.float))
plt.show()