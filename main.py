from image_utils import load_image, edge_detection
from skimage.filters import median
from skimage.morphology import ball
import plotly.express as px
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

image = load_image('japan_img.jpg')

# supress the noise
clean_image = median(image, ball(3))

# create a new array after edge detection
edgeMAG = edge_detection(clean_image)

# convert edgeMAG array into a binary array
px.imshow(edgeMAG, color_continuous_scale='gray')
edge_binary = np.where(edgeMAG < 180, 0, 1)
plt.imshow(edge_binary, cmap="gray")

# save the new image
edge_image = Image.fromarray((edge_binary * 255).astype(np.uint8))
edge_image.save('my_edges.png')
