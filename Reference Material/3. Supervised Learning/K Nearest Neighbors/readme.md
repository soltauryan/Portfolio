# What is K Nearest Neighbor?

K Nearest Neighbor (KNN) is a simple, versatile, and easy-to-implement supervised machine learning algorithm used for both classification and regression tasks. It operates on the principle that similar things exist in close proximity. In other words, it assumes that similar data points are near to each other. KNN works by finding the K nearest data points (neighbors) to a query point and makes predictions based on these neighbors.

## Types of Business Questions Answered

KNN can be applied to a wide range of business problems, such as:

- **Customer Segmentation:** Classifying customers into different groups based on purchasing behavior or preferences.
- **Recommendation Systems:** Recommending products or content by finding similar items or users.
- **Credit Scoring:** Predicting whether an individual will default on a loan based on their similarity to previous borrowers.
- **Anomaly Detection:** Identifying fraudulent transactions by detecting patterns that deviate significantly from the norm.

## Types of Data Input

KNN can be used with various types of data:

- **Numerical Data:** For tasks like price prediction or health risk assessment.
- **Categorical Data:** Useful in classification tasks such as determining customer preferences.
- **Mixed Data Types:** KNN can handle datasets with a mix of numerical and categorical data, provided the data is preprocessed correctly.

## Useful Visuals and Metrics

Effective visuals and metrics for KNN include:

- **Scatter Plots:** Visualizing the classification of data points.
- **Confusion Matrix:** Assessing the performance of a classification model.
- **Distance Metrics Visualization:** Understanding how distances between points affect the prediction.
- **Accuracy Score:** Measuring the proportion of correctly predicted instances.

## Small Python Example

Here's a basic example of implementing the KNN algorithm using Python's scikit-learn library:

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Splitting dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creating the KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Making predictions
y_pred = knn.predict(X_test)

# Evaluating the model
print(confusion_matrix(y_test, y_pred))
