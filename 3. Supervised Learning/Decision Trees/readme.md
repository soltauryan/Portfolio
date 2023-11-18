# What are Decision Trees?

Decision Trees are a type of supervised learning algorithm that are used for both classification and regression tasks. They model decisions and their possible consequences, including chance event outcomes, resource costs, and utility. Decision Trees are a non-linear means of predicting outcomes by creating a model that predicts the value of a target variable based on several input variables. Each internal node of the tree represents a test on an attribute, each branch represents the outcome of the test, and each leaf node represents a class label or a value.

## Table of Contents
- [What are Decision Trees?](#what-are-decision-trees)
  - [Table of Contents](#table-of-contents)
  - [Types of Business Questions Answered](#types-of-business-questions-answered)
  - [Types of Data Input](#types-of-data-input)
  - [Useful Visuals and Metrics](#useful-visuals-and-metrics)
  - [Small Python Example](#small-python-example)
- [Load the iris dataset](#load-the-iris-dataset)
- [Splitting dataset into training and test sets](#splitting-dataset-into-training-and-test-sets)
- [Creating the Decision Tree classifier](#creating-the-decision-tree-classifier)
- [Predicting the labels of the test set](#predicting-the-labels-of-the-test-set)
- [Calculating the accuracy](#calculating-the-accuracy)


## Types of Business Questions Answered

Decision Trees can be applied to a wide range of business problems, such as:

- **Customer Behavior:** Predicting customer choices or responses to marketing campaigns.
- **Risk Assessment:** Evaluating the risk involved in certain business decisions or financial products.
- **Resource Allocation:** Determining optimal decisions for resource allocation and management.
- **Fault Diagnosis:** Identifying the root causes of faults or failures in systems or processes.

## Types of Data Input

Decision Trees can handle various types of data:

- **Categorical Data:** Data that is categorized into discrete groups.
- **Numerical Data:** Continuous data where each value represents a measurement.
- **Mixed Data:** Decision Trees can handle datasets that have a mix of categorical and numerical features.

## Useful Visuals and Metrics

When working with Decision Trees, the following visuals and metrics are particularly useful:

- **Tree Diagram:** Visual representation of the Decision Tree showing nodes, branches, and leaves.
- **Confusion Matrix:** Useful for understanding the performance of classification models.
- **Gini Impurity or Entropy:** Measures used to quantify the purity of a node in the tree.
- **Feature Importance:** Indicates which features are most influential in the decision-making process of the tree.

## Small Python Example

Here is a basic example of building a Decision Tree Classifier using Python:

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Splitting dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creating the Decision Tree classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predicting the labels of the test set
y_pred = clf.predict(X_test)

# Calculating the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
