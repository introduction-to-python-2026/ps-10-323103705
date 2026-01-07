from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    image = Image.open(path)
    image = np.array(image)
    return image

def edge_detection(image):
    pass # Replace the `pass` with your code
