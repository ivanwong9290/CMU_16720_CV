from alignChannels import alignChannels
import numpy as np
import matplotlib.pyplot as plt
import os

# Problem 1: Image Alignment

# 1. Load images (all 3 channels)
red = np.load('../data/red.npy')
green = np.load('../data/green.npy')
blue = np.load('../data/blue.npy')

# 2. Find best alignment
rgbResult = alignChannels(red, green, blue)
plt.imshow(rgbResult)

# 3. save result to rgb_output.jpg (IN THE "results" FOLDER)
path = os.path.dirname(os.getcwd()) + "/results"
os.chdir(os.path.dirname(os.getcwd()))
if not os.path.isdir(path):
    os.mkdir("results")
    print("Created a folder called results in the main directory to place image.")
os.chdir(path)
plt.savefig('./rgb_output.jpg')
plt.show()