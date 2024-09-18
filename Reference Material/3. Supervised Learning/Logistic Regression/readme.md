# What is Logistic Regression?

Logistic Regression is a statistical method used for binary classification. It models the probability of a binary response based on one or more predictor variables. Unlike linear regression, which predicts a continuous outcome, logistic regression predicts the likelihood of occurrence of an event by fitting data to a logistic curve. It is particularly useful when the dependent variable is categorical and binary (e.g., yes/no, true/false, success/failure).

## Types of Business Questions Answered

Logistic Regression can help answer a variety of binary classification questions in business, such as:

- **Customer Churn:** Will a customer leave or stay with a service?
- **Credit Approval:** Will a customer default on a loan?
- **Marketing Response:** Will a customer respond positively to a marketing campaign?
- **Disease Diagnosis:** Will a patient develop a particular disease based on certain symptoms or tests?

## Types of Data Input

Logistic Regression can handle various data types:

- **Binary or Dichotomous Data:** For the dependent variable (e.g., 0 or 1, yes or no).
- **Continuous Data:** As independent variables (e.g., age, income).
- **Categorical Data:** Can be converted into numerical form through encoding techniques like one-hot encoding.

## Useful Visuals and Metrics

Some common visuals and metrics for Logistic Regression include:

- **ROC Curve and AUC:** To evaluate the model's ability to distinguish between the classes.
- **Confusion Matrix:** To assess the number of correct and incorrect predictions.
- **Coefficient Values:** To understand the influence of each predictor.
- **Probability Distributions:** To visualize the probability of class membership for observations.

## Small Python Example

Here's a simple Python example using Logistic Regression:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix

# Load the iris dataset
iris = load_iris()
X = iris.data
y = (iris.target != 0) * 1  # Binary classification

# Splitting dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creating and training the Logistic Regression model
model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)
