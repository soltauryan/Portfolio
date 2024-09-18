# What are Supervised Neural Networks?

Supervised Neural Networks are a subset of neural networks used in machine learning for tasks where the data comes with known labels. These networks are 'trained' on labeled data – they learn to map input data to the correct output. This type of network is used for both classification (predicting discrete labels) and regression (predicting continuous values) tasks. Supervised Neural Networks can vary in complexity and structure, from simple feedforward networks to complex architectures like Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs).

## Types of Business Questions Answered

Supervised Neural Networks can address a wide range of business and analytical questions, such as:

- **Customer Segmentation and Targeting:** How can we categorize customers and predict their behavior?
- **Sales Forecasting:** Can we predict future sales based on historical data?
- **Image Recognition:** How can we identify and classify objects within images?
- **Natural Language Processing:** How can we automatically categorize customer reviews or analyze sentiment?

## Types of Data Input

Supervised Neural Networks can handle a variety of data types, including:

- **Tabular Data:** Data in structured form, like spreadsheets or SQL tables.
- **Image Data:** For tasks like image classification and object detection.
- **Text Data:** For natural language processing tasks.
- **Time-Series Data:** For predicting future values based on past sequences.

## Useful Visuals and Metrics

Key visuals and metrics for Supervised Neural Networks include:

- **Learning Curves:** Graphs showing model performance (accuracy, loss) over epochs.
- **Confusion Matrix:** For classification tasks, to visualize the performance of the algorithm.
- **ROC Curve and AUC:** For binary classification problems.
- **Feature Maps and Filters:** Visualizing what features a CNN learns from image data.

## Small Python Example

Here is a basic example of building a supervised neural network using Python’s TensorFlow and Keras libraries:

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Splitting dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Building the neural network
model = Sequential()
model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))

# Compiling the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Training the model
model.fit(X_train, y_train, epochs=150, batch_size=10)

# Evaluating the model
_, accuracy = model.evaluate(X_test, y_test)
print(f'Accuracy: {accuracy:.2f}')
