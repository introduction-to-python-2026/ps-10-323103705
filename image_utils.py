from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    image = Image.open(path)
    image = np.array(image)
    return image

def edge_detection(image):
    # convert into a grayscale
    gray_image = np.mean(image, axis=2)
    # creating a filter for vertical changes
    KernelY= np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    # creating a filter for horizontal changes 
    KernelX = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    # applaying each filter on the grayscale
    edgeY = convolve2d(gray_image, KernelY, mode='same', boundary='fill', fillvalue=0)
    edgeX = convolve2d(gray_image, KernelX, mode="same", boundary='fill', fillvalue=0)
    # new array that combines both edges
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)
    return edgeMAG
