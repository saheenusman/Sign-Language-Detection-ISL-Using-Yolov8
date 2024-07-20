import streamlit as st
import cv2
from PIL import Image
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO(r'D:\sign language\final\slr_weights.pt')

# Function to start the camera feed and perform object detection
def start_camera():
    cap = cv2.VideoCapture(1)  # Use camera index 0 for the default webcam

    # Create a placeholder in the Streamlit app for the video feed
    image_placeholder = st.empty()

    while st.session_state.run_camera:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to grab frame")
            break

        # Perform object detection with YOLOv8
        results = model(frame)
        
        # Draw bounding boxes and labels
        for result in results:
            boxes = result.boxes
            names = result.names
            for i in range(len(boxes)):
                x1, y1, x2, y2 = map(int, boxes.xyxy[i])
                conf = boxes.conf[i].item()
                cls = int(boxes.cls[i].item())
                label = f'{names[cls]} {conf:.2f}'
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Convert the frame to RGB format for correct color display
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Display the frame in the Streamlit placeholder
        img = Image.fromarray(frame_rgb)
        image_placeholder.image(img, channels="RGB")

    cap.release()

# Main Streamlit application function
def main():
    st.title("Sign Language Detection with YOLOv8 and Camera Feed")

    if "run_camera" not in st.session_state:
        st.session_state.run_camera = False

    # Button to start the camera
    if not st.session_state.run_camera:
        if st.button("Start Camera"):
            st.session_state.run_camera = True
            start_camera()

    # Button to stop the camera
    if st.session_state.run_camera:
        if st.button("Stop Camera"):
            st.session_state.run_camera = False
            cv2.destroyAllWindows()  # Ensure OpenCV windows are closed when stopping

if __name__ == "__main__":
    main()
