# Sign-Language-Detection-ISL-Using-Yolov8


# 🔍 Problem Statement:
Effective communication is essential, yet it poses significant challenges for individuals who are deaf or mute. These individuals rely on sign language to convey their messages, which can be difficult for others to interpret. This communication barrier highlights the need for innovative solutions to foster better understanding between specially-abled individuals and the wider community.

# 🌟 Project Overview:
Sign language is crucial for connecting the deaf community with the hearing world, facilitating communication and understanding through hand articulations and non-manual gestures. To bridge the communication gap, I developed an end-to-end deep learning framework using the YOLOv8 object detection algorithm. The dataset, labeled and annotated with Roboflow, underwent extensive pre-processing and post-processing to ensure high performance. The system demonstrates exceptional performance with a precision of 98.5%, recall of 99.0%, and a mean Average Precision (mAP) of 99.5% at IoU=0.50.

# 🚀 Implementation:

* Collected and labeled images for various Indian sign language representations.
* Used Roboflow for the annotation task.
* Used the YOLOv8 Object Detection algorithm to recognize sign language.
* Prepared a dataset of 1,200 labeled images, split into training, validation, and testing sets.
* Trained the model in Google Colab for 200 epochs, achieving a mean Average Precision (mAP) score above 90%.
* Enabled real-time recognition by integrating the trained model with a webcam, allowing it to capture and process sign gestures, display bounding boxes with labels, and confidence scores.
* Developed a Streamlit application for an interactive and user-friendly experience.

# 📸 Environment Considerations:
The quality of results may be affected by environmental factors such as lighting conditions and the quality of the camera used. Ensuring good lighting and using a high-quality camera can enhance the accuracy and reliability of the sign language detection system.

