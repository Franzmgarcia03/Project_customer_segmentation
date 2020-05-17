# Project customer segmentation: Customer segmentation analysis using K-Means in python

Clustering is a way to find common characteristics in a group of data. With clustering we can do partitions in our data, giving to objects similar characteristics to each other and having big dissimilarities with the other clusters. Clustering have such applications in different areas as: marketing, banking, insurance, medicine, etc.

One of the easiest methods is the K-means algorithm. This algorithm divides the data into non-overlapping subsets without any cluster-internal structure or labels. That's how examples within a cluster are very similar, and examples across diffetent clusters are very different. 

K-Means try to minimize the intra-cluster distances and maximize the inter-cluster distances.

In this case I have a [dataset](https://github.com/Franzmgarcia03/Project_customer_segmentation/blob/master/Cust_Segmentation.csv) with different characteristics about some customers.

Here we find:

- Age
- Income
- Level of education (1: high-school, 2: degree, 3: master and 4: PHD) 
- Years employed
- Other data

So we want to make groups of people based on some of the characteristics provided by the dataset. 

To do that, the code was implementing using libraries such as: pandas, scikit-learn, numpy and matplotlib

This model use the K-Means algorithm with 3 clusters, and provide distributions of customers based on their age, income and education:


