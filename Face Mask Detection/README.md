# Face Mask :mask: Detection 

Dataset link: https://data-flair.training/blogs/download-face-mask-data/?ref=morioh.com
The dataset contains images of people with mask (mask clipart added on people's faces) and without mask.

MobileNet is used for this application. It is customized to get a single output which tells if a person has put on a mask or not.
The images are resized to 224 x 224 and scaled to train the model.

Model is trained for 1 epoch and the accuracy achieved is 97%.

OpenCV is used to capture video frames and these frames are preprocessed and given to the model for prediction.
An output greater than 0.5 indicates the person has put on a mask.

**Demo**

<img src="https://github.com/Yash4900/Python-projects/blob/master/Face%20Mask%20Detection/demo/demo.gif?raw=true" />

**Made using**

<span><img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-ar21.svg" /></span>
<span><img src="https://www.vectorlogo.zone/logos/opencv/opencv-ar21.svg" /></span>
<span><img src="https://www.vectorlogo.zone/logos/numpy/numpy-ar21.svg" /></span>
<span><img src="https://www.vectorlogo.zone/logos/jupyter/jupyter-ar21.svg" /></span>
