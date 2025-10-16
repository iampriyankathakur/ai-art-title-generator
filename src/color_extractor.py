import cv2
import numpy as np
from sklearn.cluster import KMeans

def extract_dominant_colors(image_path, n_colors=3):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.reshape((-1, 3))

    kmeans = KMeans(n_clusters=n_colors, random_state=42)
    kmeans.fit(img)
    colors = kmeans.cluster_centers_.astype(int)
    return colors
