from torch import nn, flatten
from math import sqrt

class DigitClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super().__init__()
        #Convolutional and MaxPool Layer 1
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1)
        self.maxp1 = nn.MaxPool2d(kernel_size=2, stride=2)
        #Convolutional and MaxPool Layer 2
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1)
        self.maxp2 = nn.MaxPool2d(kernel_size=2, stride=2)

        final_spatial = int(sqrt(input_size) // 4)
        flattened_size = 32 * (final_spatial**2)
        
        #Linear Layers
        self.lin1 = nn.Linear(in_features=flattened_size, out_features=hidden_size)
        self.lin2 = nn.Linear(in_features=hidden_size, out_features=16)
        
        #Output Layer
        self.output = nn.Linear(in_features=16, out_features=num_classes)

        #Activation Function
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.maxp1(x)
        x = self.conv2(x)
        x = self.relu(x)
        x = self.maxp2(x)
        x = flatten(x, start_dim=1)
        x = self.lin1(x)
        x = self.relu(x)
        x = self.lin2(x)
        x = self.relu(x)
        x = self.output(x)
        return x