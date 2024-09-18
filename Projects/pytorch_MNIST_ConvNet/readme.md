# PyTorch MNIST ConvNet

This project implements a Convolutional Neural Network (CNN) to classify handwritten digits from the MNIST dataset using PyTorch.

## Project Overview

The main script `pytorch_MNIST_ConvNet.py` contains a complete pipeline for training and evaluating a CNN on the MNIST dataset. It includes:

- Data loading and preprocessing
- Model definition
- Training loop with validation
- Model evaluation on a test set

## Requirements

- Python 3.6+
- PyTorch
- torchvision
- tqdm

You can install the required packages using:

pip install torch torchvision tqdm

## Model Architecture

The CNN model (`MNIST_MLP`) consists of:

- 2 convolutional layers
- 2 dropout layers
- 2 fully connected layers

The architecture is designed to effectively learn features from the 28x28 pixel MNIST images.

## Usage

To run the script:

python pytorch_MNIST_ConvNet.py

The script will:

1. Download the MNIST dataset (if not already present)
2. Prepare the data (normalization, splitting into train/val/test sets)
3. Train the model for 20 epochs
4. Save the best model based on validation accuracy
5. Evaluate the best model on the test set

## Features

- GPU acceleration (if available)
- Learning rate scheduling
- Model checkpointing (saves best model)
- Progress bar for training visualization
- Validation set to monitor overfitting

## Results

After training, the script will output the accuracy of the model on the 10,000 test images.

## Customization

You can modify various aspects of the training process by adjusting parameters in the script:

- Number of epochs
- Batch size
- Learning rate
- Model architecture

## Acknowledgments

This project uses the MNIST dataset, which is a subset of a larger set available from NIST and was prepared by Yann LeCun, Corinna Cortes, and Christopher J.C. Burges.
