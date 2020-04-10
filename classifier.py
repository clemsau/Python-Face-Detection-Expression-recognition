from deepface import DeepFace

import cv2
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

img_path = "uploads/surprise.jpg"

image = cv2.imread(img_path)

plt.imshow(image)

result = DeepFace.analyze(img_path)

print(result)
