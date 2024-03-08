# Pytorch tools
import torch as t
import torch.nn as nn
import torch.nn.functional as F

import matplotlib.pyplot as plt # for plotting
import torch.optim as optim #for gradient descent
import torchvision.transforms as transforms
import torchvision.datasets as datasets

from torch.utils.data import DataLoader

# For plotting
import matplotlib.pyplot as plt
import numpy as np
import time

import torchvision.models

net = torchvision.models.densenet169(pretrained=True)





