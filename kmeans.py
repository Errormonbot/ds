import pandas as pd
from sklearn import datasets
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

# Load the iris dataset
iris = datasets.load_iris()
print(iris.target_names)
print(iris.target)

# Create DataFrames for features and target
x1 = pd.DataFrame(iris.data, columns=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])
y1 = pd.DataFrame(iris.target, columns=['Target'])

# Display the first five rows
print(x1.head(5))
print(y1.head(5))

# Create and fit the KMeans model
model = KMeans(n_clusters=3)
y_kmeans = model.fit_predict(x1)

# Print the cluster labels
print(model.labels_)

# Prepare colors for visualization
colors = np.array(['red', 'green', 'blue'])
predictedY = np.choose(model.labels_, [1, 0, 2]).astype(np.int64)

# Plot the clusters
plt.scatter(x1['Sepal Length'], x1['Petal Width'], c=colors[predictedY])
plt.xlabel('Sepal Length')
plt.ylabel('Petal Width')
plt.title('KMeans Clustering of Iris Dataset')
plt.show()

# Calculate and print the accuracy (this may not be meaningful for clustering)
print("Test Data Accuracy:", accuracy_score(y_true=y1, y_pred=y_kmeans))
