# License plate recognition

Methodology:
1. Import packages
2. Import image and convert it to grayscale
3. Remove noise (bilateral filtering) and perform edge detection (canny edge detection)
4. Find shapes (contours) from the edged image and filter out best shapes (max area)
5. Get corner points of the license plate
6. Crop out the roi using masking
7. Recognize text using easyocr


<span><img src="https://www.vectorlogo.zone/logos/jupyter/jupyter-ar21.svg" /></span>
<span><img src="https://www.vectorlogo.zone/logos/opencv/opencv-ar21.svg" /></span>
<span><img src="https://www.vectorlogo.zone/logos/numpy/numpy-ar21.svg" /></span>

**Flutter App Link: https://github.com/Yash4900/Test/tree/main/ALPR**
