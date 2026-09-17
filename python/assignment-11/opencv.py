import cv2
import numpy as np

original_img = cv2.imread("traffic_jam_1050x700.avif")

# Reading, displaying and saving images
cv2.imshow("Image", original_img)
cv2.imwrite("image.jpg", original_img)

# Resizing images
width = 1050
height = 700
img = cv2.resize(original_img, (width, height))
cv2.imshow("Resized Image", img)

# Flipping images (horizontal, vertical, both)
horizontal_flipped_img = cv2.flip(original_img, 1)
cv2.imshow("Horizontal Flipped Image", horizontal_flipped_img)

vertical_flipped_img = cv2.flip(original_img, 0)
cv2.imshow("Vertical Flipped Image", vertical_flipped_img)

both_flipped_img = cv2.flip(original_img, -1)
cv2.imshow("Both Flipped Image", both_flipped_img)

# Drawing shapes (lines, polygons) and adding text on images
cv2.line(original_img, (100, 100), (200, 200), (0, 0, 255), 2)
cv2.imshow("Image with Line", original_img)

cv2.rectangle(original_img, (100, 100), (200, 200), (0, 0, 255), 2)
cv2.imshow("Image with Rectangle", original_img)

polygon = np.array([[100, 100], [200, 100], [200, 200], [100, 200]])
cv2.polylines(original_img, [polygon], True, (0, 0, 255), 2)
cv2.imshow("Image with Polygon", original_img)

text = "Hello, World!"
cv2.putText(original_img, text, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow("Image with Text", original_img)

# Image translation (shifting) using warpAffine
translation_matrix = np.float32([[1, 0, 100], [0, 1, 100]])
translated_img = cv2.warpAffine(original_img, translation_matrix, (width, height))
cv2.imshow("Image with Translation", translated_img)

# Image rotation using getRotationMatrix2D and warpAffine
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
rotated_img = cv2.warpAffine(original_img, rotation_matrix, (width, height))
cv2.imshow("Image with Rotation", rotated_img)

# Thresholding (Binary threshold)
thresholded_img = cv2.threshold(original_img, 127, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("Image with Threshold", thresholded_img)

# Blurring images using Gaussian Blur and Median Blur
blurred_img = cv2.GaussianBlur(original_img, (5, 5), 0)
cv2.imshow("Image with Gaussian Blur", blurred_img)

median_blurred_img = cv2.medianBlur(original_img, 5)
cv2.imshow("Image with Median Blur", median_blurred_img)

# Morphological operations (Tophat, Blackhat)
kernel = np.ones((5, 5), np.uint8)
tophat_img = cv2.morphologyEx(original_img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Image with Tophat", tophat_img)

blackhat_img = cv2.morphologyEx(original_img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("Image with Blackhat", blackhat_img)

# Edge detection using Canny
edges_img = cv2.Canny(original_img, 100, 200)
cv2.imshow("Image with Edges", edges_img)

# Reading and writing video files
video_capture = cv2.VideoCapture("traffic_jam_1050x700.mp4")
cv2.imwrite("video.mp4", video_capture)

# Capturing live video from webcam
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    if not ret:
        break
    cv2.imshow("Video", frame)
    cv2.waitKey(1)

