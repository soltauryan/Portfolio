import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import random_split
from tqdm import tqdm

# Define the Convolutional Neural Network (CNN) model
class MNIST_ConvNet(nn.Module):
    def __init__(self):
        super(MNIST_ConvNet, self).__init__()
        # Convolutional layers
        self.conv1 = nn.Conv2d(1, 32, 3, 1)  # Input: 1 channel, Output: 32 channels, 3x3 kernel, stride 1
        self.conv2 = nn.Conv2d(32, 64, 3, 1)  # Input: 32 channels, Output: 64 channels, 3x3 kernel, stride 1
        # Dropout layers for regularization
        self.dropout1 = nn.Dropout2d(0.25)
        self.dropout2 = nn.Dropout2d(0.5)
        # Fully connected layers
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)  # 10 output classes for digits 0-9

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)  # Apply ReLU activation
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)  # Apply max pooling
        x = self.dropout1(x)
        x = torch.flatten(x, 1)  # Flatten the tensor
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)  # Apply log softmax for classification
        return output
    
# Move all the training and evaluation code into a main function
def main():
    # Data preparation
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    # Load MNIST dataset
    train_dataset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    test_dataset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

    # Split training data into train and validation sets
    train_size = int(0.8 * len(train_dataset))
    val_size = len(train_dataset) - train_size
    train_dataset, val_dataset = random_split(train_dataset, [train_size, val_size])

    # Create data loaders
    train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)
    val_loader = torch.utils.data.DataLoader(dataset=val_dataset, batch_size=1000, shuffle=False)
    test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=1000, shuffle=False)

    # Device configuration
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Initialize model, loss function, and optimizer
    model = MNIST_ConvNet().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Learning rate scheduler
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.5)

    # Training loop
    num_epochs = 20
    best_val_accuracy = 0.0

    for epoch in range(num_epochs):
        model.train()  # Set model to training mode
        running_loss = 0.0
        
        # Use tqdm for progress bar
        with tqdm(train_loader, unit="batch") as tepoch:
            for images, labels in tepoch:
                tepoch.set_description(f"Epoch {epoch+1}/{num_epochs}")
                
                images, labels = images.to(device), labels.to(device)
                
                optimizer.zero_grad()  # Zero the parameter gradients
                outputs = model(images)
                loss = criterion(outputs, labels)
                loss.backward()  # Backpropagation
                optimizer.step()  # Update weights
                
                running_loss += loss.item()
                tepoch.set_postfix(loss=running_loss/len(train_loader))
        
        # Validation
        model.eval()  # Set model to evaluation mode
        correct = 0
        total = 0
        with torch.no_grad():  # Disable gradient calculation
            for images, labels in val_loader:
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
        
        val_accuracy = 100 * correct / total
        print(f"Validation Accuracy: {val_accuracy:.2f}%")
        
        # Save the best model
        if val_accuracy > best_val_accuracy:
            best_val_accuracy = val_accuracy
            torch.save(model.state_dict(), 'best_model.pth')
        
        scheduler.step()

    # Load the best model for testing
    model.load_state_dict(torch.load('best_model.pth'))

    # Evaluation on the test set
    model.eval()  # Set model to evaluation mode
    correct = 0
    total = 0
    with torch.no_grad():  # Disable gradient calculation
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f'Accuracy of the model on the 10,000 test images: {100 * correct / total:.2f}%')

# Add the if __name__ == '__main__': block
if __name__ == '__main__':
    main()